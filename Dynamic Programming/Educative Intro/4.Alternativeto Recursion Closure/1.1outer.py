def outer():
    x = 1
    def inner():
        print(f'x in outer function: {x}')
    return inner

print('Outer Function return: ', outer())
print('\n Inner function print: ')
outer()()

# We usually want to define another function to hold the function returned by the closure
f = outer()
print('\n Inner function print better way: ')
f()

