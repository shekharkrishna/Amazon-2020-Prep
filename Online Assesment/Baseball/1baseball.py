# https://aonecode.com/amazon-online-assessment-baseball-scorekeeping
# (?<=\s|^)\d+(?=\s|$)


def baseball_scorekeeping(blocks):
    list = [] # to use as stack for scores manupulation
    total_score = 0
    current_score = 0

    for block in blocks:
        if block != 'X' or '+' or 'Z': 
            pass
        else: 
            pass

    return total_score



# Driver Code

blocks = ["10", "20", "X", "+"]
total_score = baseball_scorekeeping(blocks)
print(total_score)