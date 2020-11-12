def baseball_scorekeeping(blocks):
    list = [] # to use as stack for scores manupulation
    list_total = []
    total_score = 0
    current_score = 0

    for block in blocks:
        if block != 'X' and block != '+' and block != 'Z':        
            current_score = int(block)
            list.append(current_score)
            total_score +=current_score      
            list_total.append(total_score)      
        elif block == 'X': 
            current_score = 2 * list[-1]
            list.append(current_score)
            total_score += current_score
        elif block == '+':
            current_score = list[-1] + list[-2]
            list.append(current_score)
            total_score += current_score
        elif block == 'Z':
            list.pop()
            current_score = list[-1]           
            total_score += current_score

    return total_score

# Driver Test Code

# blocks = ["10", "20", "X", "+"]
# total_score = baseball_scorekeeping(blocks)
# print(total_score)


# Example 2:

blocks = ["10", "20", "Z", "30", "+"]
total_score = baseball_scorekeeping(blocks)
print(total_score)
