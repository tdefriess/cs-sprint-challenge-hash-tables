def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    results = []
    indices = {}
    i = 0
    for weight in weights:
        difference = limit - weight
        if difference in indices:
            results.append(i)
            results.append(indices[difference])
            print(results)
            return results
        else:
            indices[difference] = i
            print(indices)
            i += 1

    if len(results) > 0:
        return results
    else:
        return None
