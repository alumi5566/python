import threading
import time

sem = threading.Semaphore(4)

def gothread():
    with sem:
        for i in range(8):
            print(threading.current_thread().name, i, "\n")
            time.sleep(2)

for i in range(5):
    threading.Thread(target=gothread).start()