import collections
from typing import Collection, List 


class Solution(object):
    # def maxSlidingWindow(nums, k):

    #     arr = []
    #     q = Collection.deque()
    #     for i in range(k):

    #         while q and nums[i] > nums[q[-1]]:
    #             q.pop()
    #         q.append(i)
    #     arr.append(nums[q[0]])

    #     for i in range(k, len(nums)):
    #         # print(q,i)
    #         if i-q[0] == k:
    #             q.popleft()

    #         while q and nums[i] > nums[q[-1]]:
    #             q.pop()
    #         q.append(i)
    #         arr.append(nums[q[0]])
    #     return arr

    # This is not O(N), it is O(NK) for any decreasing sequence.
    def maxSlidingWindow2(nums: List[int], k: int) -> List[int]:
        initial_max = max(nums[0:k])
        res = [initial_max]
        for i in range(k,len(nums)):
            if nums[i-k] == initial_max:
                initial_max = max(nums[i-k+1:i+1])
            elif nums[i] > initial_max:
                initial_max = nums[i]
            
            res.append(initial_max)
        
        return res

class Test:
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution.maxSlidingWindow2(nums, k))
