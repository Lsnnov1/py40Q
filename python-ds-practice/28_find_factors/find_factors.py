def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []
    for current_number in range(1,num +1):
        if num % current_number == 0:
            factors.append(current_number)
    return factors

print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(321421))