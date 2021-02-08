def decorator(func):
    def wrapper(numbers):
        new_numb = []
        for a in numbers:
            if not a % 2 == 0:
                new_numb.append(a)
        return func(new_numb)
    return wrapper

@decorator
def show(x):
    print(x)

show([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])



