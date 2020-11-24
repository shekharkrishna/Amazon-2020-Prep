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
print('''Outer Function is just as object that holds the inner function
 and the local values that might be helpful for dynamism \n''', fibo())

f = fibo()
print('''\n Default Logic will compute the smallest fib number. 
        \t Inner Function Logic is for Fib of 1: ''', f())


# Fib of n can only be achieved using the loop till n.
fibonacci = fibo()

# To get the Fibo of i we can loop in
for i in range (20):
    # num = fibonacci() # waist of placeholder
    print(f'Fib of {i+1} is: {fibonacci()}')

# this loop above is just like an engine for power to repetatively preform the 
# main logic that is defined in inner function of outer function. 
print('Seperation of logic and power is cool')



