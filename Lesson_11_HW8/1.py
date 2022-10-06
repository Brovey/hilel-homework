import functools


def expected(expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args = [a for a in args]
            kwargs = [v for v in kwargs.values()]
            for i in args:
                if not isinstance(i, expected_types):
                    raise TypeError(f"Was expected {expected_types} but {type(i)} is given")
            for i in kwargs:
                if not isinstance(i, expected_types):
                    raise TypeError(f"Was expected {expected_types} but {type(i)} is given")
        return wrapper
    return decorator


@expected((int, list, str, float))
def input_value(*args):
    return args


input_value(3333, "test", [], (),  a=4, b="stttttt")
