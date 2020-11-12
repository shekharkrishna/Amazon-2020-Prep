# https://aonecode.com/amazon-online-assessment-baseball-scorekeeping
# Solution Similar : https://leetcode.com/problems/baseball-game/
# (?<=\s|^)\d+(?=\s|$)


def baseball_scorekeeping(blocks):
   list_stack = []

    for block in blocks:
        if block != 'X' and block != '+' and block != 'Z':        
            current_score = int(block)            
            list_stack_current_score.append(current_score)            
            total_score += current_score
            list_stack_total_score.append(total_score)           
        elif block == 'X': 
            current_score = 2 * list_stack_current_score[-1]
            list_stack_current_score.append(current_score)
            total_score += current_score
            list_stack_total_score.append(total_score) 
        elif block == '+':
            current_score = list_stack_current_score[-1] + list_stack_current_score[-2]
            list_stack_current_score.append(current_score)
            total_score += current_score
            list_stack_total_score.append(total_score) 
        elif block == 'Z':
            list_stack_current_score.pop()
            current_score = list_stack_current_score[-1]     
            list_stack_total_score.pop()      
            total_score = list_stack_total_score[-1]
            list_stack_total_score.append(total_score) 
        else:
            


    return total_score

# Driver Test Code

# blocks = ["10", "20", "X", "+"]
# total_score = baseball_scorekeeping(blocks)
# print(total_score)

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