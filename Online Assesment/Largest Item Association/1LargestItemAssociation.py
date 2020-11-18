
# Most if not all of the top upvoted solutions on here are broken because you are not guaranteed that 
# the order of the elements given in items array is in a way such that the root elements of a group are given first. 
# Because most of the below solutions don't create a back edge from the 2nd item in the group to the first, 
# if the items array is out of the specified order, their code will not work whereas mine does and it's truly a simple fix. 
# This code is easily extensible to multiple association inputs as well, 
# but you'll need to just loop through those lists and change up the code a bit (useless for this q tho obviously). 
# Also, a mostly similar problem in LC: https://leetcode.com/problems/accounts-merge -- 
# this LC problem is also more general because it doesn't limit each input association to a pair.
#  The idea is the same, YOU NEED TO CREATE BACK EDGES TO THE FIRST ELEMENT WHILE LOOPING!!! 
#  Think of it like a tree, if you don't create back edges to the first element in each input subarray,
#   then you will never be able to go back up a tree in case the input is not ordered perfectly which 
#   will cause you to miss out on some nodes that are part of the same group (tree).

# One small detail, since your code does not use the values (just the keys) on the item_map dictionary, you could just loop on the keys() instead of items().

# for key in item_map.keys():

from collections import deque, defaultdict

def largest_item_association(item_association):

    item_map = defaultdict(set)

    for item_pair in item_association:
        item_map[item_pair[0]].add(item_pair[1])
        item_map[item_pair[1]].add(item_pair[0])

    largest_group = []
    visited = set()

    for key in item_map.keys():
        if key not in visited:
            curr_group = []
            q = deque()
            q.append(key)
            while q:
                curr = q.popleft()
                visited.add(curr)
                curr_group.append(curr)
                for neighbor in item_map[curr]:
                    if neighbor not in visited:
                        q.append(neighbor)
            if len(curr_group) > len(largest_group):
                largest_group = curr_group
            elif len(curr_group) == len(largest_group): 
                if largest_group > curr_group:
                    largest_group = curr_group

    largest_group.sort()
    return largest_group

print(largest_item_association([['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5'], ['item5', 'item6']]))
print(largest_item_association([['item6', 'item7'], ['item3', 'item4'], ['item4', 'item5'], ['item7', 'item8']]))
print(largest_item_association([['item1', 'item2'], ['item4', 'item5'], ['item3', 'item4'], ["item1","item4"]]))