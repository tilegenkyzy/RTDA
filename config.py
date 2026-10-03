STUDENTS_BDA2406 = [
    {"user_id": "BDA_01", "name": "Askar Abilkhay"},
    {"user_id": "BDA_02", "name": "Sayat Agzam"},
    {"user_id": "BDA_03", "name": "Said Aidar"},
    {"user_id": "BDA_04", "name": "Nazerke Akhpanbayeva"},
    {"user_id": "BDA_05", "name": "Zhaniya Askarkyzy"},
    {"user_id": "BDA_06", "name": "Abdanur Ayazbek"},
    {"user_id": "BDA_07", "name": "Shapagat Bolatbek"},
    {"user_id": "BDA_08", "name": "Madiyar Gabit"},
    {"user_id": "BDA_09", "name": "Takhmina Iztileuova"},
    {"user_id": "BDA_10", "name": "Dana Karymsakova"},
    {"user_id": "BDA_11", "name": "Almat Kobeibek"},
    {"user_id": "BDA_12", "name": "Olzhas Kolzhabay"},
    {"user_id": "BDA_13", "name": "Rizat Litfullin"},
    {"user_id": "BDA_14", "name": "Zhanerke Murat"},
    {"user_id": "BDA_15", "name": "Nazar Nurzhankyzy"},
    {"user_id": "BDA_16", "name": "Ramazan Rakhmettula"},
    {"user_id": "BDA_17", "name": "Symbat Salim"},
    {"user_id": "BDA_18", "name": "Aiym Samakova"},
    {"user_id": "BDA_19", "name": "Amir Sarsenbaev"},
    {"user_id": "BDA_20", "name": "Assanali Shakhmetov"},
    {"user_id": "BDA_21", "name": "Nazar Tilegenkyzy"},
    {"user_id": "BDA_22", "name": "Anastassiya Yashenkova"},
    {"user_id": "BDA_23", "name": "Aryn Yklas"}
]

#user action types on the Moodle portal
ACTION_TYPES = [
    'quiz_submit', 
    'video_view', 
    'assignment_download', 
    'page_view', 
    'login_attempt'
]

#Thresholds for rule-based anomaly detection
TRAFFIC_SPIKE_THRESHOLD = 40   # Request count threshold in a rolling window
ERROR_RATE_THRESHOLD = 0.20    # Allowable error rate limit 
RESPONSE_TIME_WARNING = 600    # Server response time warning limit 