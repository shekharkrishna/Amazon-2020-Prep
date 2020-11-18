def fresh_promo(codeList, shoppingCart):
    for code in codeList:
        


codeList = [['apple', 'apple'], ['banana', 'anything', 'banana']] 
shoppingCart = ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']
print(fresh_promo(codeList, shoppingCart))

# breaking here 1 is op
codeList=[['anything', 'apple'], ['banana', 'anything', 'banana']] 
customerPurchasedList=["orange", "grapes", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]
print(fresh_promo(codeList, shoppingCart))

# breaking here 1 is op
codeList=[["anything", "anything", "anything", "apple"], ["banana", "anything", "banana"]] 
customerPurchasedList=["orange", "apple", "banana", "orange", "apple", "orange", "orange", "banana", "apple", "banana"]
print(fresh_promo(codeList, shoppingCart))