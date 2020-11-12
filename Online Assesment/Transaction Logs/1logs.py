def transactionThreashold(logs): 
    return logs

# Test
logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = transactionThreashold(logs)
print(threshold)