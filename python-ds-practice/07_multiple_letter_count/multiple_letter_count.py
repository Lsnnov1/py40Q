def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # create counter to store values
    counter = {}
    
    # for each letter in phrase
    for letter in phrase:
        # set keys and vals
        counter[letter] = counter.get(letter, 0) +1
    return counter


# str = 'hello'
# for letter in str:
#     print(str.count(letter))

print(multiple_letter_count('yay'))