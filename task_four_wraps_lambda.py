from functools import wraps


# Смотрел из примера. Сам не догадался.
def val_checker(lambda_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(num):
            if lambda_func(num):
                print(func(num))
            else:
                raise ValueError(f"wrong val: {num}")

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(10)
    print(calc_cube.__name__)
except Exception as e:
    print(e)
