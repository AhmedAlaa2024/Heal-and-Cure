from datetime import datetime

def get_time_now_as_text():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")