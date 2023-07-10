import time


#def rate_limiter():
   

def rate_limiter(func, time_per_minute=10):
    interval = 60/time_per_minute
    last_call = [0.0]

    def wrapper(*args, **kwargs):
        passed = time.perf_counter() - last_call[0]
        need_to_wait = interval - passed
        if need_to_wait > 0:
            time.sleep(need_to_wait)
        result = func(*args, **kwargs)
        last_call[0] = time.perf_counter()
        return result
    return wrapper



@rate_limiter
def add(a: int, b: int) -> int:
    return a + b


for i in range(10):
    print(i,add(1, 2))