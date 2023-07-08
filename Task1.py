def is_admin(func):
    def wrapper(**kwargs):
        for i in kwargs.values():
            if i == 'admin':
                result = func(**kwargs)
            else:
               result = print('D')
        return result
    return wrapper
           

@is_admin
def show_customer_receipt(user_type: str):
    print('Granny cake show_customer_receipt')

show_customer_receipt(user_type='admin')


