def countItems(s, startIndices, endIndices):
    totalStars = []
    for start, end in zip(startIndices, endIndices):
        seenVerticalBar = 0
        countStars = 0
        tempCountStars = 0
        for c in s[start-1:end]:
            if c == '*':
                tempCountStars += 1
            elif c == '|':
                seenVerticalBar += 1
                if seenVerticalBar == 2:
                    countStars += tempCountStars
                    seenVerticalBar = 1
                    tempCountStars = 0
                elif seenVerticalBar == 1:
                    tempCountStars = 0
        
        print(s[start-1:end], countStars)

        totalStars.append(countStars)

    return totalStars

# Code from @ymuwes
def check(s, starts, ends):
    valid_range =[s.find('|'), s.rfind('|')]                                                                                                                                                             

    if valid_range[0] == valid_range[1]:
        return [0] * len(starts)

    ans = []

    for i in range(len(starts)):
        counter = 0

        to_search = [max(starts[i]-1,valid_range[0]),min(ends[i]-1,valid_range[1])]

        for j in range(to_search[0],to_search[1]):
            if s[j] == '*':
                counter+=1
        ans.append(counter)

    return ans

if __name__ == "__main__":

    testcases = [
        ['|**|*|*', [1,1], \
        [5,6]],['*|*|', [1], [3]], \
        ['|***|*****|**|****|***|***', [1, 5, 8, 9, 11, 13], [26, 23, 21, 19, 21, 26]],\
        ['**||**|', [1, 4, 10, 5, 7, 3, 2], [8, 10, 4, 9, 10, 7, 5]]
    ]

    for i, tests in enumerate(testcases):
        print("================= Test Case %d ================" %(i+1))
        print('My output: ', countItems(tests[0], tests[1], tests[2]))
        print('Output from user @ymunwes ', check(tests[0], tests[1], tests[2]))
        print("============================================================")
        print('\n\n\n')

# Solution to Items in Containers, Time Complexity: 0(mn) where m = size(starts) 
# and n = size(s), Space Complexity: O(1) .
# I don't know if this solution can be further improved. 
# Most solutions claiming Time Complexity as O(n) here are actually O(mn). 
# Please correct me if I am wrong, and also suggest further changes to improve this code.