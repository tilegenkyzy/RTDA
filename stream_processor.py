import pandas as pd
import numpy as np
from config import ERROR_RATE_THRESHOLD, RESPONSE_TIME_WARNING

class MoodleStreamProcessor:
    def __init__(self, window_size=15):
        self.window_size = window_size
        self.buffer = pd.DataFrame()

    def process_event(self, event_dict):
        # Append incoming event as a new row
        new_row = pd.DataFrame([event_dict])
        self.buffer = pd.concat([self.buffer, new_row], ignore_index=True)
        
        # Maintain a sliding window of recent records
        recent_window = self.buffer.tail(self.window_size)

        # 1. Compute real-time rolling indicators using Pandas & NumPy
        avg_response_time = np.mean(recent_window['response_time_ms'])
        std_response_time = np.std(recent_window['response_time_ms'])
        error_rate = np.mean(recent_window['error_flag'].astype(int))
        active_users = recent_window['user_id'].nunique()

        # 2.Rule-Based Anomaly Detection
        anomalies = []
        if error_rate > ERROR_RATE_THRESHOLD:
            anomalies.append(f"CRITICAL: High Error Rate ({error_rate*100:.1f}%)")
            
        if avg_response_time > RESPONSE_TIME_WARNING:
            anomalies.append(f"WARNING: High Response Time ({avg_response_time:.0f} ms)")

        metrics = {
            'timestamp': event_dict['timestamp'],
            'student_name': event_dict['student_name'],
            'action_type': event_dict['action_type'],
            'response_time_ms': event_dict['response_time_ms'],
            'avg_response_time': avg_response_time,
            'std_response_time': std_response_time,
            'error_rate': error_rate,
            'active_users': active_users,
            'anomalies': anomalies
        }
        return metrics