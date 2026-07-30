# 跟目录下utils/utils.py

from datetime import datetime


def generate_time_student_id():
    now = datetime.now()
    year   = now.strftime('%Y')
    month  = now.strftime('%m')
    millis = f'{now.microsecond//1000:03d}'
    return f'{year}{month}{millis}'
