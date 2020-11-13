def transactionThreashold(logs): 
    threasholdMap = {}

    for log in logs:
        transaction = log.split(' ')
        for i in range(0, len(transaction)-1):
            #threasholdMap.update([(i, 1)])
            pass
        print(transaction)
# Test
logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = transactionThreashold(logs)
#print(threshold)