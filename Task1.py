def is_admin(func):
    def wrapper(**kwargs):
            try:
                if 'admin' not in kwargs.values():
                    raise ValueError('Permission denied')
                else:
                    result = func(**kwargs)
            except ValueError as exception:
                result = print(exception)
            return result
    return wrapper
           

@is_admin
def show_customer_receipt(user_type: str):
    print('Granny cake show_customer_receipt')

show_customer_receipt(user_type='user')
show_customer_receipt(user_type='admin')