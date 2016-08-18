
def fib(limit):
    x_1 = 0
    x_2 = 1
    while True:
        x_1, x_2 = x_2, x_2 + x_1
        if x_2 >= limit:
            break
        yield x_2


def evens(numbers):
    return (n for n in numbers if n % 2 == 0)


def sum_even_fibs(limit):
    return sum(evens(fib(limit)))
