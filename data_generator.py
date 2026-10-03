import random
from datetime import datetime
from config import STUDENTS_BDA2406, ACTION_TYPES

def generate_moodle_event(force_anomaly=None):
  
    student = random.choice(STUDENTS_BDA2406)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    action = random.choice(ACTION_TYPES)
    
    if force_anomaly == 'server_error':
        status_code = random.choice([500, 502, 403])
        response_time = random.randint(1000, 2500)
        error_flag = True
    elif force_anomaly == 'slow_response':
        status_code = 200
        response_time = random.randint(700, 1500)
        error_flag = False
    else:
        # Standard operational status
        status_code = 200 if random.random() > 0.05 else 500
        response_time = int(random.gauss(180, 30))
        response_time = max(60, response_time)
        error_flag = (status_code != 200)

    return {
        'timestamp': timestamp,
        'user_id': student['user_id'],
        'student_name': student['name'],
        'action_type': action,
        'response_time_ms': response_time,
        'status_code': status_code,
        'error_flag': error_flag
    }