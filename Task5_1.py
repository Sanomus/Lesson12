import time


def rate_limiter(func, times_per_minute=10):
    last_call = [0.0]
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count, last_call
        if count == times_per_minute:
            need_to_wait = 60 - (sum(last_call))
            time.sleep(need_to_wait)
            count = 0
            return count
        else:
            count += 1
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            elapsed = end - start
            last_call.append(elapsed)
        return result
    return wrapper



@rate_limiter
def add(a: int, b: int) -> int:
    return a + b


for i in range(100):
    print(i,add(1, 2))