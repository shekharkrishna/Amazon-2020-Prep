stringList = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
# stringList = stringList.split(' ')
# print(stringList)
# print(stringList[0])



print('\n\n')

for i in range(0, len(stringList)):
    print(stringList[i])

    for j in range(0, len(stringList[i])-1):
    
        map = dict.fromkeys(stringList[:-1], 1)
        print(str(map))





print('\n\n')