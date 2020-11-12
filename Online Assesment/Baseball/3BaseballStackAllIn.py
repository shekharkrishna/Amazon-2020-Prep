# https://aonecode.com/amazon-online-assessment-baseball-scorekeeping
# Solution Similar : https://leetcode.com/problems/baseball-game/
# (?<=\s|^)\d+(?=\s|$)

# this is a way better solution that I initially thought about it. Catch : Didnt know sum existed for list queue python thing

def baseball_scorekeeping(blocks):
    list_stack = [] # Creating list to implement stack

    for block in blocks:                   
        if block == 'X': 
            list_stack.append(2*list_stack[-1])            
        elif block == '+':
            list_stack.append(list_stack[-1] + list_stack[-2])            
        elif block == 'Z':
            list_stack.pop()                     
        else:
            list_stack.append(int(block))

    return sum(list_stack)

# Driver Test Code

blocks = ["10", "20", "X", "+"]
total_score = baseball_scorekeeping(blocks)
print(total_score)

# Example 2:

blocks = ["10", "20", "Z", "30", "+"]
total_score = baseball_scorekeeping(blocks)
print(total_score)

blocks = ['5', '-2', '4', 'Z', 'X', '9', '+', '+']
total_score = baseball_scorekeeping(blocks)
print(total_score)

blocks = ['1', '2', '+', 'Z']
total_score = baseball_scorekeeping(blocks)
print(total_score)