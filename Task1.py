def is_admin(func):
    def wrapper(**kwargs):
            try:
                result = func(**kwargs)
            except ValueError as exception:
                result = print(exception)
            return result
    return wrapper
           

@is_admin
def show_customer_receipt(user_type: str):
    if user_type != 'admin': 
        raise ValueError('Permission denied')
    else:
        print('Granny cake show_customer_receipt')

show_customer_receipt(user_type='user')
show_customer_receipt(user_type='admin')