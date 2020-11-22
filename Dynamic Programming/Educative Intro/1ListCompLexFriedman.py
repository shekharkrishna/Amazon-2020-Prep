#[f(x) for x in nums]

#[f(x) for x in nums if g(x)] if g(x) passes

nums = [1, 2, 3, 4]
print('\n Original list for List Comprehension: ', nums)

result = [x*x for x in nums]
print('''\n List Comprehension to compute multiplication of every element f(x*x) 
for all items in the original list: ''', result)

# lets take one more function g() to filter out only even numbers 
result = [x*x for x in nums if x % 2 == 0]
print('''\n List Comprehension to compute multiplication of every element f(x*x) 
for all items in the original list but with the condition = only even numbers(x % 2): ''', result)

# List comprehension creates the list objects and computes all the elements in the list and stores the entire list
# ini the memory.

# Generator Expression stores just the iterable ojects and computes every elements in the list one at a time as it is
# being queried.

print('\n Generator Expression : Use when range is large/infinite')
print('Using Generator Expression: ', list(x*x for x in nums))


