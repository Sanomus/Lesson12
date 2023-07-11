
def check_types(func):
    def wrapper(*args):
        try:
            for elem in args:
                if type(elem) not in list(func.__annotations__.values()):
                    raise TypeError(f'Argument a must be int, not {type(elem)}') 
            result = print(func(*args))
        except TypeError as exception:
            result = print(f'{exception}')
        return result
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
add("1", "2")