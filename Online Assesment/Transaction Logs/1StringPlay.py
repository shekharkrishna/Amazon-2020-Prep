string = "88 99 200"
string = string.split(' ')
print(string)
print(string[0])



print('\n\n')

for i in range(0, len(string)-1):
    print(string[i])
    
    map = dict.fromkeys(string[:-1], 1)
    print(str(map))





print('\n\n')

