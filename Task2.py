def catch_errors(func):
    def wrapper(*args):
        try:
            result = func(*args)
        except KeyError as exception:
            result = print(f'Found 1 erro during execution of your function: {exception}')
        return result
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    if 'key' not in data:
        raise KeyError(f'no such key as {list(data.keys())[0]}')
    else:
        print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})

some_function_with_risky_operation({'key': 'bar'})
