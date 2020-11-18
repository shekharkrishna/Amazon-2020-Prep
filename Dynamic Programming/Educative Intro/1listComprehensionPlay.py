print('\n Regular List Comprehension: ')
a = [(x, y) for x in range(1, 6) for y in range(3, 6)]
print(a)

print('\n Parellel/zipped List Comprehension: ')
zippedComp = [x for x in zip(range(1,6),range(3,6))]
print(zippedComp)
