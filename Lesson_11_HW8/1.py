import functools


class CustomError(Exception):
    pass


class UnexpectedTypeException(CustomError):
    pass


def expected(expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            function = func(*args, **kwargs)
            try:
                if not isinstance(function, expected_types):
                    raise UnexpectedTypeException
            except UnexpectedTypeException:
                print(f"UnexpectedType! Was expected {expected_types} but {type(function)} is given")
            return function
        return wrapper
    return decorator


@expected((int, str))
def input_value():
    a = 4.5
    return a


print(input_value())



