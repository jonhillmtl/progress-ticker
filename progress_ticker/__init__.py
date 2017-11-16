from functools import wraps
from threading import Thread, Event
from time import sleep

def flip(event):
    chars = ['|', '/', '-', '\\']
    char_length = len(chars)
    index = 0

    while event.is_set() == False:
        print("\b{}".format(chars[index]), end='', flush=True)
        index = (index + 1 ) % char_length
        sleep(0.1)

def progress_ticker():
    def _impl(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("starting {}...  ".format(func.__name__), end='', flush=True)
            
            event = Event()
            t = Thread(target=flip, args=(event, ))
            t.start()
            
            return_value = func(*args, **kwargs)
            
            event.set()
            t.join()
            
            print("\b...done")
            return return_value
            
        return wrapper
    return _impl