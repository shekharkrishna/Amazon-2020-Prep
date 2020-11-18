def fresh_promo(c, s):
    if c == []:
        return 1
    si = 0
    for i in c:
        for j in i:
            if j == "anything" or s[si] == j:
                si += 1
            else:
                while si < len(s) and j != s[si]:
                    si += 1
            if si == len(s):
                return 0
    return 1


codeList = [['apple', 'apple'], ['banana', 'anything', 'banana']] 
shoppingCart = ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']
print(fresh_promo(codeList, shoppingCart))

codeList=[['anything', 'apple'], ['banana', 'anything', 'banana']] 
customerPurchasedList=["orange", "grapes", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]
print(fresh_promo(codeList, shoppingCart))

# 1
print(fresh_promo([["apple", "apple" ], ["banana", "anything", "banana"]],  ["apple", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]))

#1 but breaking here with 0
codeList=[["anything", "anything", "anything", "apple"], ["banana", "anything", "banana"]] 
customerPurchasedList=["orange", "apple", "banana", "orange", "apple", "orange", "orange", "banana", "apple", "banana"]
print(fresh_promo(codeList, shoppingCart))