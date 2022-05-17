# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


# def log_errors(func):
#     log_name = 'function_errors.log'
#
#     def func_fact(*args, **kwargs):
#         try:
#             res = func(*args, **kwargs)
#             return res
#         except (ZeroDivisionError, ValueError) as exc:
#
#             param = []
#             param.extend([arg for arg in args])
#             param.extend([f'{key}={value}' for key, value in kwargs.items()])
#
#             with open(file=log_name, mode='a', encoding='utf8') as file:
#                 file.write(f'{func.__name__:<15} {param.__str__():<40} {exc.__class__.__name__:<20} {str(exc):<10}\n')
#             raise exc
#
#     return func_fact


def write_errors_to_file(file_path='func_errors.log'):
    def write_errors_to_file_wrap(func):
        def write_errors(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ZeroDivisionError, ValueError) as exc:
                param = []
                param.extend([arg for arg in args])
                param.extend([f'{key}={value}' for key, value in kwargs.items()])

                with open(file=file_path, mode='a', encoding='utf8') as file:
                    file.write(f'{func.__name__:<15} '
                               f'{param.__str__():<40} '
                               f'{exc.__class__.__name__:<20} '
                               f'{str(exc):<10}\n')
                raise

        return write_errors
    return write_errors_to_file_wrap


# Проверить работу на следующих функциях
@write_errors_to_file()
def perky(param):
    return param / 0


@write_errors_to_file(file_path='my_func_errors.log')
def perky_with_fn(param):
    return param / 0


@write_errors_to_file(file_path='my_func_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

try:
    perky(param=42)
except Exception as exc:
    print(exc)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла

try:
    perky_with_fn(param=55)
except Exception as exc:
    print(exc)