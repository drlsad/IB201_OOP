def check_password(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_input = input("Введите пароль: ")
            if user_input != password:
                print("В доступе отказано")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator


@check_password('password')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    parts = [typeOfMeat]
    if withOnion:
        parts.append('лук')
    if withTomato:
        parts.append('помидор')
    burger = 'Бургер из ' + ', '.join(parts)
    return burger

print(make_burger('говядина', withOnion=True))