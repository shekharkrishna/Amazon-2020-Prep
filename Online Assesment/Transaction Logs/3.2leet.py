from collections import defaultdict
def getFrauds(logs, threshold):
    data = defaultdict(int)
    for log in logs:
        for user in set(log[:2]):
            data[user] += 1
    return sorted([key for key in data if data[key] >= threshold])


# Test
logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = getFrauds(logs, 1)
print(threshold)