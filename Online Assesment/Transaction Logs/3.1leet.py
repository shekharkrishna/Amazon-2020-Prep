import collections
def find_frauds(log_data, threshold):
    if not log_data:
        return []

    user_list = []

    for log in log_data:
        user_list += set(log[0].split()[:-1])

    count = collections.Counter(user_list)

    return sorted([int(userid) for userid, appear in count.items() if appear >= threshold])


# Test
logs = [["88 99 200"], ["88 99 300"], ["99 32 100"], ["12 12 15"]]
#logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = find_frauds(logs, 2)
print(threshold)