# List Comprehension with Walrus Operator
def fibo(n):
    return n if n <= 1 else (fibo(n-1) + fibo(n-2))

print('Fib number for 6: ', fibo(6))

# List Comprehension could be a game changer for testing!
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 30] # This is the largest I could enter 38 WITH A LAG OF ABOUT 45
                                                            # SECONDS IN THE IDE.
print('List Comp. to test fibo(): ', [fibo(x) for x in nums])

# Walrus Operator
print('Test Fibo, Walrus Operator Use (Filter is even only): ', [y for x in nums if (y := fibo(x)) % 2 == 0])
# Used y here smartly to Walrus Operator to the the value using () in filter condition of even only
