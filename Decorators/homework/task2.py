import time
class Timer:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = time.time() - t1
            print(f'{func.__name__} ran in: {t2} sec')
            print(f"{self.name} finished work")
            return result
        return wrapper

@Timer('timer_class')
def my_func():
    time.sleep(1)


if __name__ == '__main__':
   my_func()