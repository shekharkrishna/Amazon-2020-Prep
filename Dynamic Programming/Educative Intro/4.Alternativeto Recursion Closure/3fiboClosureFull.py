# https://towardsdatascience.com/dont-use-recursion-in-python-any-more-918aad95094c
def fibo():
    x1 = 0
    x2 = 1

    def get_next_number():
        nonlocal x1, x2
        x3 = x1 + x2 # Algo
        x1, x2 = x2, x3 # shifting for next computation
        return x3
    return get_next_number # make sure not to return get_next_number() which returns int but as an object which is not
                            # callable
def fibo_closure(n):
    fibonacci = fibo()
    # To get the Fibo of i we can loop in
    for i in range(2, n+1):
        num = fibonacci() # now we need this placeholder to get the nth Fibo
        #print(f'Fib of {i + 1} is: {fibonacci()}')
    return num


# Test
print('Fibo(1000): ', fibo_closure(1000)) # this is impossible with recursion 
                                        # max recursion depth exceeded in comparision






