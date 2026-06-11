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


@check_password("secret123")
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

print(fibonacci(10))  
