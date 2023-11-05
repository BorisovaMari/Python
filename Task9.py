import threading
import time

numbers = list(reversed(range(1, 11)))

class NumThread(threading.Thread):
    def __init__(self, num, interval, flow_lock):
        super().__init__()
        self.daemon = True
        self.num = num
        self.interval = interval
        self.flow_lock = flow_lock

    def run(self):
        while True:
            self.flow_lock.acquire(1)
            print("Поток", self.num, ":", numbers, ". Поток", self.num, "завершил работу")
            self.flow_lock.release()
            time.sleep(self.interval)

flow_lock = threading.Lock()

t1 = NumThread(1, 1, flow_lock)
t2 = NumThread(2, 1, flow_lock)
t1.start()
t2.start()
t1.join()
t2.join()
