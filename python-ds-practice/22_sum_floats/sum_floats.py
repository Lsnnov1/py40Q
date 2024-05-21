def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    # previous_num = 0
    # total = 0
    # for item in nums:
    #     if type(item) == float:
    #         total = item + previous_num
    #         previous_num = item
    # return total

    return sum([num for num in nums if isinstance(num, float)])



    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

print(sum_floats([1.5, 2.4, 'awesome', [], 1]))
print(sum_floats([1, 2, 3]))

print(sum_floats([1.5, 1.5, 4.5, 2.5]))