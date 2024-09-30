import time


def decorator_function(func):
    def wrapper(*args, **kwargs):
        stat = time.time()
        func(*args, **kwargs)
        end = time.time() - stat
        print(f'Время работы функции {end}(сек)')
    return wrapper


@decorator_function
def test_function(value):
    try:
        print(float(value))
        time.sleep(1)
    except ValueError:
        print('Не верный тип переданного параметра ')



if __name__ == '__main__':
    test_function(1)
