from collections import Counter
def find_frauds(transactions, threshold):
    frauds = []
    if not transactions:
        return frauds
    user_counts = Counter()
    for transaction in transactions:
        users = transaction[0].split()[0:2]
        curr_users = Counter()
        for user in users:
            if user not in curr_users:
                curr_users[user] += 1
        for user in curr_users:
            user_counts[user] += curr_users[user]
    for user in user_counts:
        if user_counts[user] >= threshold:
            frauds.append(user)
    return frauds


def main():
    transactions1 = [
        ["345366 89921 45"],
        ["029323 38239 23"],
        ["38239 345366 15"],
        ["029323 38239 77"],
        ["345366 38239 23"],
        ["029323 345366 13"],
        ["38239 38239 23"]
    ]
    print("The fradulent users are ", find_frauds(transactions1, 2))

    logs = [["88 99 200"], ["88 99 300"], ["99 32 100"], ["12 12 15"]]
    print("The fradulent users are ", find_frauds(logs, 2))


main()