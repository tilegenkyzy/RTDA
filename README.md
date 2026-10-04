# AITU Moodle Real-Time Analytics & Anomaly Detection System

**Subject:** Real-Time Data Collection and Stream Processing System  
**Author:** Tilegenkyzy Nazar  
**Group:** BDA-2406  
**Institution:** Astana IT University 
**Academic Year:** 2026–2027  

---

## Project Overview
This project implements a Python-based real-time stream processing pipeline designed to acquire, process, and analyze user activity logs from the AITU Moodle educational platform. 

The system simulates a live event stream of student interactions, calculates streaming metrics using Pandas and NumPy, and detects system performance anomalies via a rule-based detection engine.

---

## System Architecture & File Structure

```text
RTDA/
├── config.py             # System thresholds, action types, and student metadata 
├── data_generator.py     # Real-time event generator simulating Moodle activity logs
├── stream_processor.py   # Streaming analytics module (rolling statistics & anomaly detector)
├── main.py               # Main execution script (stream runner, CLI logger, visualization)
├── requirements.txt      # External dependencies
├── README.md             # Project documentation and run instructions
├── data/
│   └── moodle_stream_log.csv     # Exported stream history log
└── plots/
    └── moodle_stream_analysis.png # Generated analytical plots

Key Features & Indicators
1. Streaming Indicators 
Instant & Rolling Mean Response Time (ms): Tracking server latency trends using numpy.mean().

Rolling Error Rate (%): Monitoring HTTP error response codes across recent steps.

Active User Count: Tracking unique active students within the sliding window using pandas.Series.nunique().

2. Rule-Based Anomaly Detectors
CRITICAL Alert: Triggered if Error Rate > 20%.

WARNING Alert: Triggered if Rolling Average Response Time > 600 ms.

How to Run
Install dependencies:

Bash
python -m pip install -r requirements.txt
Execute the stream processor:

Bash
python main.py
Check outputs:

Processed stream logs are stored in data/moodle_stream_log.csv.

Real-time analytical plots are saved in plots/moodle_stream_analysis.png.
