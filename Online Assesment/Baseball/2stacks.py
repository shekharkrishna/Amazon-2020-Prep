from collections import deque

myStack = deque()
print(myStack)

myStack.append("10")
myStack.append('20')
myStack.append('30')

print(myStack)

poped = myStack.pop()
print('Poped: ', poped)
print(myStack)

print('Top Item: ', myStack[-1])


print('\n##################List Implementation for small problems##########')

list=[]
list.append(1) # append 1
print("push:",list)
list.append(2) # append 2
print("push:",list)
list.append(3) # append 3
print("push:",list)
sum = sum(list)
print(sum) # i had no information that the list elements sum had a library built in to python that could sum it up and 
# the thought process went in the way it did with solution 1baseball_my_working.py
list.pop() # pop 3
print("pop:",list)
print("peek:",list[-1]) # get top most element
list.pop() # pop 2
print("pop:",list)
print("peek:",list[-1]) # get top most element
