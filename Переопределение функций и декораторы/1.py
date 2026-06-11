original_print = print

def print(*args):
    uppercased_args = [str(arg).upper() for arg in args]
    original_print(*uppercased_args)

print('Нельзя ли потише?')
