#Examples
A = [8, 4, 6, 12]
#Ans 58
B = [20, 4, 8, 2]
#Ans: 54
C = [1, 2, 5, 10, 35, 89]
#Ans: 224
D = [2, 2, 3, 3]
#Ans: 20

#Testing cases change per example
test = A
#Temp List
hello = []
#Sum List
sumList = []

#Loop to iterate 
while (len(test) > 0):
    hello.append(min(test))
    x = test.index(min(test))
    test.pop(x)

    if len(hello) > 1:
        test.append(sum(hello))
        sumList.append(sum(hello))
        hello = []
        
print(sum(sumList))