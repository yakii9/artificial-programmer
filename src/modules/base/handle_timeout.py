from threading import Thread
import functools


def timeout(timeout_in_seconds):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, timeout_in_seconds))]

            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                    res[0] = e
            t = Thread(target=newFunc)
            try:
                t.start()
                t.join(timeout_in_seconds)
            except Exception as je:
                print('error starting thread')
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                pass
            return ret
        return wrapper
    return deco
