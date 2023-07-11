def cached_result(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args in cache:
            print('cached')
            return cache[args]
        elif kwargs:
            print('cached')
            return cache[tuple(kwargs.values())]
        else:
            res = func(*args)
            cache[args] = res
        return res
    return wrapper


@cached_result
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))
print(add(a=1, b=2))