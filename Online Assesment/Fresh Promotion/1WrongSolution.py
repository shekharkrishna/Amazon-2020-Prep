def fresh_promo(codeList, shoppingCart):
                # flatten the codeList
                codeListFlat = []
                for group in codeList:
                        for fruit in group:
                                codeListFlat.append(fruit)
                
                # If secret code list (not flattened) is empty then it is assumed that the customer is a winner.
                if not codeListFlat:
                        return 1

                code_len = len(codeListFlat)
                cart_len = len(shoppingCart)

                # if the customer has less fruits than the winning code, they'll never win.
                if code_len > cart_len:
                        return 0

                # use 2 pointers now, one points to track codeListFlat (code_ptr) and another is for loop
                code_ptr = 0
                for fruit in shoppingCart:
                        # if we see "anything", we don't care what fruit we're accessing.
                        # we just increment the code_ptr and continue
                        if codeListFlat[code_ptr] == 'anything':
                                code_ptr += 1
                        
                        elif fruit != codeListFlat[code_ptr]:
                                # the flow of secret list is broken, reset the code_ptr to 0
                                code_ptr = 0
                        
                        else:  # this is when the fruit == codeListFlat[code_prt]
                                code_ptr += 1

                        # if code_ptr reaches the end of codeListFlat, the customer has WON.
                        if code_ptr == code_len:
                                return 1
                else:
                        # if we come out of the for loop, we know the customer has lost.
                        return 0



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