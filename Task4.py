def cashed_result(func):
    cashe = {}
    def wrapper(*args):
        if args in cashe:
            print('cashed')
            return cashe[args]
        else:
            res = func(*args)
            cashe[args] = res
        return res
    return wrapper


@cashed_result
def add(a: int, b: int) -> int:
    return a + b

print(add(1,2))
print(add(1,2))