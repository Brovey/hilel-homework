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
            if not isinstance(function, expected_types):
                raise UnexpectedTypeException(f"UnexpectedType! Was expected {expected_types} but"
                                              f" {type(function)} is given")
            return function
        return wrapper
    return decorator


@expected((int, str))
def input_value():
    value = []
    return value


print(input_value())
