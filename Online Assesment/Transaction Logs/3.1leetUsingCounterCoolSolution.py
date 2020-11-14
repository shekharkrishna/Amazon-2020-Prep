import collections
def find_frauds(log_data, threshold):
    if not log_data: # Always a nice check 
        return []

    user_list = []

    for log in log_data:
        user_list += set(log[0].split()[:-1])

    count = collections.Counter(user_list) # We count the transactions as string and not int and its value count
                                           # Nice little collections to count the occurance of any string element. 

    print(count.items()) # dict_items([('88', 2), ('99', 3), ('32', 1), ('12', 1)])

    user_id = []
    for appear in count.items():
        if appear[1] >= threshold:
            user_id.append(appear[0])
    return sorted(user_id)  
    # I donno how the below one liner is working. PJ: Investigate it later when time.  

    #return sorted([int(userid) for userid, appear in count.items() if appear >= threshold]) # similar to looping in dict before


# Test
logs = [["88 99 200"], ["88 99 300"], ["99 32 100"], ["12 12 15"]]
#logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = find_frauds(logs, 2)
print(threshold)