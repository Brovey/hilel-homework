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
                raise UnexpectedTypeException(f"UnexpectedType! Expected"
                                              f" {expected_types} but {type(function)} given")
            return function
        return wrapper
    return decorator


@expected((int, str))
def input_value():
    value = []
    return value


print(input_value())
