from collections import deque
def maxSlidingWindow(num_computer, hard_disk_space, segment_length):
    if segment_length > len(hard_disk_space) or not hard_disk_space:
        return []
    
    ret = []
    q = deque()
    
    for i in range(len(hard_disk_space)):
        # remove everything from the back that is >= the current num
        while q and q[-1][0] >= hard_disk_space[i]:
            q.pop()
        # add the new num to the back
        q.append((hard_disk_space[i], i))
        # remove everything from the front if it's not in the window
        while q[0][1] <= i - segment_length:
            q.popleft()
        # start adding results to output array once we have our first size k window
        if i >= segment_length - 1:
            ret.append(q[0][0])
    
    return max(ret)

print(maxSlidingWindow(3, [8,2,4], 2))