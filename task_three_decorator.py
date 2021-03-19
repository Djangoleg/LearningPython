from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for el in [x for x in (*args, *kwargs.values())]:
            print(f"{func.__name__}({el}: {type(el)}),")

        print(*func(*args, *kwargs), sep=", ")

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    number_list = [x for x in (*args, *kwargs.values()) if isinstance(x, int) or isinstance(x, float)]
    return [x ** 3 for x in number_list]


calc_cube(5, 6, 7, 8)
print(calc_cube.__name__)
