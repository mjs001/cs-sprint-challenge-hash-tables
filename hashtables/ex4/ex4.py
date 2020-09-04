def has_negatives(a):
    """
    YOUR CODE HERE
    """
   
    negatives_by_number = {}

    for num in a:
        negatives_by_number[num] = -num # this is our negative number to check

    result = [] # array for nums with pos and neg

    for num in negatives_by_number.keys(): # 
        if num > 0 and negatives_by_number[num] in negatives_by_number:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
