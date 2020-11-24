nums = [1, 2, 3, 4]
print('\n Original list for List Comprehension: ', nums)

print('\n List Comprehension Lambda and Map: ', list(map(lambda x: x*x, nums)))



# https://medium.com/better-programming/lambda-map-and-filter-in-python-4935f248593
print(' \n Lambda, map, filter Deep Dive: ')

# Normal Funcition:
def sum(x, y):
    return x+y

print('\n Sum(Normally Using Function) :', sum(5, 5))


sum = lambda x, y : x + y

print('\n Sum(Using Lambda Function) :', sum(5, 5))
print(type(sum))

print('''\n Map functions expect a function object. 
    It executes the function_object for each element in the sequence and 
    returns a list of the elements modified by the function object.''')

def double(x):
    return 2 * x
print('\n Map map(function_object, iterable1, iterable2,...) : ', list(map(double, [1, 2, 3, 4])))
# map executes the double function for each element in the list, [1, 2, 3, 4]

print('\n Map using Lambda for the same: ', list(map(lambda x : 2 * x, [1, 2, 3, 4])))

print('\n Iterating Over a Dictionary Using Map and Lambda:')
dict_a = [{'Name':'Python', 'Points': 9},{'Name': 'Java', 'Points' : 8}]
print('Get Names Only: ', list(map(lambda x : x['Name'], dict_a)))
print('Points in the dict_a: ', list(map(lambda x: x['Points']*10 , dict_a)))
print('''Boolean Op 'Python' in Map: ''', list(map(lambda x: x['Name'] == 'Python', dict_a)))


print('\n Multiple Iterables to the Map Function')
to_add_1 = [1, 2, 3]
to_add_2 = [10, 20, 30]

sum = map(lambda x, y : x + y, to_add_1, to_add_2)
print('Sum of two liste iterables using Map and Lambda: ', list(sum))
print('''We can’t access the elements of the map object 
with index nor we can use len() to find the length of the map object.
We can, however, force convert the map output, i.e. the map object, to list by list()''')

print('''\n Filter \n
Basic Syntax : filter(function_object, only one iterable)
function_object returns a boolean value 
filter returns only those elements for which the function_object returns True.''')

numbers = [1, 2, 3, 4, 5, 6]
print('\n Filter even numbers only: ',list(filter(lambda x : x % 2 == 0 ,numbers)))

#print(dict_a)
print('''Filter all that have key--> Name as value --> python'''
        ,list(filter(lambda x : x['Name'] == 'Python' , dict_a)))

print("list() Converts the filer obj to a list")