def check_types(func):
    def wrapper(*args):
        try:
            args[0]*args[1]
            result = print(func(*args))
        except TypeError:
           result = print(f'TypeError: Argument a must be int, not {type(args[0])}')
        return result
    return wrapper



@check_types
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)


add("1", "2")
