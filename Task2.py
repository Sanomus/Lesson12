def catch_errors(func):
    def wrapper(*args):
        try:
            result = func(*args)
        except KeyError:
            #'key' in kwargs
            counter = 0
            err_list = []
            for elem in args:
                for key in elem.keys(): 
                    if 'bar'!= key:
                        counter +=1
                        err_list.append(key)

            result = print(f'Found {counter} error during execution of your function: KeyError no such keys as {err_list}')
        return result
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})

some_function_with_risky_operation({'key': 'bar'})
