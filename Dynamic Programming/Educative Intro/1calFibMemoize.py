def calculateFibonacci(n):
    memoize = [-1 for x in range(n + 1)]
    return calculateFibonacciRecursive(memoize, n)


def calculateFibonacciRecursive(memoize, n):
    if n < 2:
        return n

    # if we have already solved this sub problem, simply return the result from the cache
    # This line will make sure we dont go extra step
    if memoize[n] >= 0:
        return memoize[n]

    memoize[n] = calculateFibonacciRecursive(memoize, n - 1) + calculateFibonacciRecursive(memoize, n - 2)
    return memoize[n]


def main():
    print('Fibonacci : ', calculateFibonacci(4))
    nums = [1,2, 5,6,7,8,9,10,19]
    print('Testing using List Comp: Test Case - [1,2, 5,6,7,8,9,10,19]:---', [calculateFibonacci(x) for x in nums])

    # print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
    # print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
    # print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()

# There is alot of redundent task evenif we broke it to smaller parts. 
# My initial thoguht was to store it to some variable so that it would not have to compute it
# again and again like when fib(2) and fib(3) which seems to 
# go recompute fib(1) and fib(0) again and again.
