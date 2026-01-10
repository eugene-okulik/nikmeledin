def finish_me(func):
    def wrapper(text):
        print('finished')
        func(text)
    return wrapper


@finish_me
def example(text):
    print(text)
example('print me')
