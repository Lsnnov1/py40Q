def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_lst = []
    for item in lst:
        if item:
            new_lst.append(item)
    return new_lst

# return [val for val in lst if val]
# RETURN THE VALUE FROM EVERY VALUE IN THE LIST IF THE VALUE IS TRUTHY


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))