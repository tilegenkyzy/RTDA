import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from data_generator import generate_moodle_event
from stream_processor import MoodleStreamProcessor

#Create required directories for output storage
os.makedirs('data', exist_ok=True)
os.makedirs('plots', exist_ok=True)

def run_simulation(total_steps=50):
    processor = MoodleStreamProcessor(window_size=15)
    processed_history = []

    print("STARTING AITU MOODLE REAL-TIME STREAM PROCESSING")
    print(f"{'Time':<20} | {'Student':<20} | {'Action':<20} | {'Resp(ms)':<8} | {'AvgResp':<8} | {'ErrRate':<8} | {'Alerts'}")
    print("-" * 110)

    for step in range(total_steps):
        # Inject deliberate anomalies for demonstration testing
        if 20 <= step <= 25:
            event = generate_moodle_event(force_anomaly='server_error')
        elif 35 <= step <= 38:
            event = generate_moodle_event(force_anomaly='slow_response')
        else:
            event = generate_moodle_event()

        metrics = processor.process_event(event)
        processed_history.append(metrics)

        alerts_str = " | ".join(metrics['anomalies']) if metrics['anomalies'] else "OK"
        print(f"{metrics['timestamp']:<20} | {metrics['student_name']:<20} | {metrics['action_type']:<20} | "
              f"{metrics['response_time_ms']:<8} | {metrics['avg_response_time']:<8.1f} | "
              f"{metrics['error_rate']*100:<7.1f}% | {alerts_str}")

        time.sleep(0.1) # Simulate continuous stream delay

    # Export processed stream log to CSV
    df_results = pd.DataFrame(processed_history)
    df_results.to_csv('data/moodle_stream_log.csv', index=False)
    print("\n[SUCCESS] Stream log saved to 'data/moodle_stream_log.csv'")

    # Generate and save analytical plots
    plot_results(df_results)

def plot_results(df):
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    # Plot 1: Instant vs Rolling Mean Response Time
    axes[0].plot(df.index, df['response_time_ms'], label='Instant Response Time (ms)', color='lightgray', linestyle='--')
    axes[0].plot(df.index, df['avg_response_time'], label='15-step Rolling Mean (ms)', color='blue', linewidth=2)
    axes[0].axhline(y=600, color='red', linestyle=':', label='Warning Threshold (600 ms)')
    axes[0].set_title('AITU Moodle Server Performance Real-Time Tracking')
    axes[0].set_ylabel('Response Time (ms)')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    #Plot 2: Error Rate Tracking over Stream Steps
    axes[1].plot(df.index, df['error_rate'] * 100, label='Error Rate (%)', color='red', linewidth=2)
    axes[1].set_title('Moodle Error Rate & System Stress Events')
    axes[1].set_xlabel('Stream Step Index')
    axes[1].set_ylabel('Error Rate (%)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('plots/moodle_stream_analysis.png', dpi=300)
    print("[SUCCESS] Plots saved to 'plots/moodle_stream_analysis.png'")
    plt.show()

if __name__ == "__main__":
    run_simulation(total_steps=50)