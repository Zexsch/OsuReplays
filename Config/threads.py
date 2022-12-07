from threading import Thread
from time import sleep
from .config import THREAD_TIMER

def count() -> None:
    x = 1
    while True:
        sleep(THREAD_TIMER)
        print(f'{x*THREAD_TIMER} seconds have passed.')
        
        x += 1
    
def start_thread() -> None:
    thread = Thread(target=count, daemon=True)
    thread.start()