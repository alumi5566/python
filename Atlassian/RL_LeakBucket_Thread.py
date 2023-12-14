from threading import Lock, Thread
from datetime import datetime
from _collections import deque
import time
import sys

lock = Lock()
queue = deque()
BUCKET_CAPACITY = 100
LEAK_PER_SECOND = 1
REQUEST_PER_SECOND = 10
# https://medium.com/@avocadi/rate-limiter-leaky-bucket-be68c6476385

def process():
    if not len(queue):
        return None
    with lock:
        return queue.popleft()

def request():
    if len(queue) >= BUCKET_CAPACITY:
        return False
    with lock:
        queue.append(datetime.now())
        return True

def process_in_seq():
    while True:
        time.sleep(1 / LEAK_PER_SECOND)
        res = process()
        if res:
            print(f'{datetime.now(): %H:%M:%S} / request processed original request: {res: %H:%M:%S}')

def request_in_seq():
    while True:
        time.sleep(1 / REQUEST_PER_SECOND)
        request()

process_thread = Thread(target=process_in_seq)
process_thread.start()

request_thread = Thread(target=request_in_seq)
request_thread.start()