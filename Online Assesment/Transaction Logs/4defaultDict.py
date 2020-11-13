from collections import defaultdict
#from typing import DefaultDict
#https://docs.python.org/3/library/collections.html#collections.defaultdict


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print('s[] ===>',s )

d = defaultdict(list)
print(d)

for key, value in s:
    d[key].append(value)
    print(d)


print("Weird mapping: ", d)
print("Again: ", d.items())


# Use Case
print('\n\n Setting the default_factory to int makes the defaultdict useful for counting')
word = 'KrishnaShekhar'
dic = defaultdict(int)
print(dic)
for key in word: 
    dic[key] += 1

print("Key count: ", dic.items())


