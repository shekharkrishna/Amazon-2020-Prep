import unittest


def get_closes_pairs_to_target(a, b, target):
    """
    Using 2 pointers technique to run from left of a and from right of b
    Store pairs in a dictionary, keep track closest_to_target. Return dict[closest_to_target]
    T(n): O(m + n)
    """
    if not a or not b:
        return []

    # sort by value
    a = sorted(a, key=lambda tup: tup[1])
    b = sorted(b, key=lambda tup: tup[1])

    dict = {}
    closest_to_target = 0
    min = float("Inf")
    # 2 pointers:
    # - i run from left -> right of a
    # - j run from right -> left of b
    i, j = 0, len(b) - 1

    while i < len(a) and j >= 0:
        sum = a[i][1] + b[j][1]

        if sum <= target:
            if sum in dict:
                dict.get(sum).append([a[i][0], b[j][0]])
            else:
                dict[sum] = [[a[i][0], b[j][0]]]

            i += 1

            if target - sum < min:
                min = target - sum
                closest_to_target = sum
        else:
            j -= 1

    # sort to satisfies test cases, we can return unsorted list
    return sorted(dict[closest_to_target], key=lambda tup: tup[0])

    
# Driver
a = [[1, 20], [2, 15], [3, 5]]
b = [[1, 80], [2, 11], [3, 1]]
target = 17
print(get_closes_pairs_to_target(a, b, target))




class Test(unittest.TestCase):
    def test_get_closes_pairs_to_target(self):
        a = [[1, 20], [2, 15], [3, 5]]
        b = [[1, 80], [2, 11], [3, 1]]
        target = 17
        self.assertEqual([[2, 3], [3, 2]], get_closes_pairs_to_target(a, b, target),
                         "Should return correct list of closes pairs to target when input is unsorted lists")

        a = [[1, 2], [2, 4], [3, 6]]
        b = [[1, 2]]
        target = 7
        self.assertEqual([[2, 1]], get_closes_pairs_to_target(a, b, target), "Should return correct list of closes pairs to target")

        a = [[1, 3], [2, 5], [3, 7], [4, 10]]
        b = [[1, 2], [2, 3], [3, 4], [4, 5]]
        target = 10
        self.assertEqual([[2, 4], [3, 2]], get_closes_pairs_to_target(a, b, target),
                         "Should return correct list of closes pairs to target")

        a = [[1, 8], [2, 7], [3, 14]]
        b = [[1, 5], [2, 10], [3, 14]]
        target = 20
        self.assertEqual([[3, 1]], get_closes_pairs_to_target(a, b, target),
                         "Should return correct list of closes pairs to target")

        a = [[1, 8], [2, 15], [3, 9]]
        b = [[1, 8], [2, 11], [3, 12]]
        target = 20
        self.assertEqual([[1, 3], [3, 2]], get_closes_pairs_to_target(a, b, target),
                         "Should return correct list of closes pairs to target")

        a = [[1, -8], [2, 15], [3, -9]]
        b = [[1, 8], [2, -11], [3, -12]]
        target = 1
        self.assertEqual([[1, 1]], get_closes_pairs_to_target(a, b, target),
                         "Should return correct list of closes pairs to target when inputs have negative numbers")

        a = []
        b = [[1, 8], [2, 11], [3, 12]]
        target = 20
        self.assertEqual([], get_closes_pairs_to_target(a, b, target),
                         "Should return empty list when a is empty list")

        a = [[1, 8], [2, 15], [3, 9]]
        b = []
        target = 20
        self.assertEqual([], get_closes_pairs_to_target(a, b, target),
                         "Should return empty list when b is empty list")

        a = []
        b = []
        target = 20
        self.assertEqual([], get_closes_pairs_to_target(a, b, target),
                         "Should return empty list when a and b is empty list")