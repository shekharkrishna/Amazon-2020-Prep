from collections import defaultdict

def transactionThreashold(logs): 
    threasholdMap = defaultdict(int)
    threashold = 2
    user_id = []

    for log in logs:
        #print(type(log)) # log is string type
        log.split(' ')  # PJ: transaction is List which now has individual data(key) within one transaction. 
                                      # This has been possible with list's split by " " property.     
        for tran in set(log[:2]): # PJ: 1. to get last element ignored in loop Plus the set concept to avoid duplicate
                                    # removed extra placeholder
            threasholdMap[tran] += 1   

    for key in threasholdMap:
        if threasholdMap[key] >= threashold:
            user_id.append(key)   

    return sorted(user_id)
    # Alt way :
    # return sorted([key for key in threasholdMap if threasholdMap[key] >= threashold])    

# Test
logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = transactionThreashold(logs)
print(threshold)

logs = [
        "345366 89921 45",
        "029323 38239 23",
        "38239 345366 15",
        "029323 38239 77",
        "345366 38239 23",
        "029323 345366 13",
        "38239 38239 23"
    ]
threshold = transactionThreashold(logs)
print(threshold)