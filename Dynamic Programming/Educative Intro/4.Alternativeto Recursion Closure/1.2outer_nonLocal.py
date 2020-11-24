def outer():
    x = 1
    def inner():
        # we can tell the inner function of a closure that the variable should not be considered 
        # as a “local variable”, by using the nonlocal keyword
        nonlocal x
        print(f'x in outer function (before modifying): {x}')
        x += 1
        print(f'x in outer function (after modifying): {x}')
    return inner


print('Outer Function return: ', outer())
print('\n Inner function print: ')
outer()()

# We usually want to define another function to hold the function returned by the closure
f = outer()
print('\n Inner function print better way: ')
f()

# Reset the function by creating a new placeholder
g = outer()
print('\n\t To add the variable x by 1 for five times: ')
for i in range(5):
    g()

