# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    results = []
    result = []
    index = {}
    for address in files:
        path = address.split('/')
        filename = path[len(path) - 1]

        if filename in index:
            index[filename] = [index[filename]] + [address]
        else:
            index[filename] = address

    for query in queries:
        if query in index:
            results.append(index[query])

    for arr in results:
        if isinstance(arr, str):
            result.append(arr)
        else:
            for string in arr:
                result.append(string)

    print(result)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
