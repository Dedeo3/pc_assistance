import time
from datetime import datetime

def getTime():
    timeNow= datetime.now()
    current_time= timeNow.strftime("%H:%M:%S")
    return current_time

def validationTime():
    while True:
        if getTime()>="01:33:00":
            return "turu"
        print("count each 10s")
        time.sleep(10)
        