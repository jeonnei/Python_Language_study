#time_utils.py
import time

def current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def sleep_for(seconds):
    time.sleep(seconds)

def time_elapsed(start_time):
    return time.time() - start_time
