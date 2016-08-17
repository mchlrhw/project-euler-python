
def mult_of_3_and_5(limit):
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            yield i


def sum_multiples(limit):
    return sum(m for m in mult_of_3_and_5(limit))
