import threading

def start_thread(func):
    ret = threading.Thread(target=func)
    ret.daemon = True
    ret.start()