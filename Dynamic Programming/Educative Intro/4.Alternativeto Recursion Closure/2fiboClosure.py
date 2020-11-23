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


# Test
print('Fibo(1): ', fibo())
fibonacci = fibo()

# To get the Fibo of i we can loop in
for i in range (20):
    # num = fibonacci() # waist of placeholder
    print(f'Fib of {i+1} is: {fibonacci()}')



