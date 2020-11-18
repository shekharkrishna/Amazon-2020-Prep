def find_pairs(a, b, target):
    """
    :type a: List(List(Int))
    :type b: List(List(Int))
    :type target: Integer
    :rtype: List(List(Int))
    """
    best = 0
    pairs = list()
    for a_element in a:
        for b_element in b:
            if a_element[1] + b_element[1] <= target:
                if a_element[1] + b_element[1] == best:
                    pairs.append([a_element[0], b_element[0]])
                if a_element[1] + b_element[1] > best:
                    best = a_element[1] + b_element[1]
                    pairs = list()
                    pairs.append([a_element[0], b_element[0]])

    return pairs

    # Test
    # Driver
a = [[1, 20], [2, 15], [3, 5]]
b = [[1, 80], [2, 11], [3, 1]]
target = 17
print(find_pairs(a, b, target))