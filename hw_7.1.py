def my_func(*args):
    for key in args:
        if len(key) % 2 == 0:
            print(key)

my_func('eres', 'weqwe','213213213213213','23232323')