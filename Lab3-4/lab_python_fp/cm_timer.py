from time import time, sleep
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.start = 0
        self.stop = 0

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time()
        print(f'Time: {self.stop - self.start}')

@contextmanager
def cm_timer_2():
    start_time = time()
    yield None
    end_time = time()
    print(f'Time: {end_time - start_time}')

if __name__ == '__main__':
    with cm_timer_1():
        sleep(2.5)

    with cm_timer_2():
        sleep(2.5)




