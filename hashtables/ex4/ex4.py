def has_negatives(a):
    """
    YOUR CODE HERE
    """
    negatives = {}
    result = []
    for num in a:
        if num < 0:
            negatives[-1 * num] = num

    for num in negatives:
        if num in a:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
