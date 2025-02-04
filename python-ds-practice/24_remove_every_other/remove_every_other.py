def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    new_lst = []
    counter = 0
    for item in lst:
        if counter == 0:
            new_lst.append(item)
            counter += 1
        elif counter == 1:
            counter = 0
    return new_lst

lst = [1, 2, 3, 4, 5]
print(remove_every_other(lst))