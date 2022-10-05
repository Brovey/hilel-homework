import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args = [i for i in args]
        kwargs = [f"{k}={v!r}" for k, v in kwargs.items()]
        print (type(args),args)
        print(type(kwargs), kwargs)
        for i in args:

            if not isinstance(i, str):
                print(i, "NOT")
        else:
            print(i, "YES")

       # func(*args, **kwargs)
            # записати результат функції у змінну
            # зробити перевірку типу змінної з expected_types
            # якщо результат фунції не є чимось переліченим у expected_type
            # викликати свою помилку або просто raise Exception
    return wrapper





@decorator
def input_value(a,b):
    print(a,b, c , d)

input_value(3333, 'dfsdfs', )






