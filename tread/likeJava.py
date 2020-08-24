from threading import Thread, Lock

def synchronized(f):
    lock = Lock()

    def ret(*args , **kargs):
        lock.acquire()
        f(*args , **kargs)
        lock.release()
    
    return ret