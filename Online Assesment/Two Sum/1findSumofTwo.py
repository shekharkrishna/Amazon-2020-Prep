def find_sum_of_two(A, val):
    found_values = set()
    for a in A:
        if val - a in found_values:
            return True

        found_values.add(a)
    
    return False

#Test
A = [5, 7, 1, 2, 8, 4, 3]
val  = 10
print(find_sum_of_two(A, val))

# Runtime Complexity: Linear, O(n)O(n)

# Memory Complexity: Linear, O(n)O(n)