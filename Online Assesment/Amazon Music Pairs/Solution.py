#from collections import *
import collections
from typing import List


def numPairsDivisibleBy60(time: List[int]) -> int:
    ans, cnt = 0, collections.Counter()
    for t in time:
        theOther = -t % 60
        ans += cnt[theOther]
        cnt[t % 60] += 1
    return ans


time = [30,20,150,100,40]
print(numPairsDivisibleBy60(time))




# Analysis: - credit to @since2020's space analysis correction.

# Time: O(n), space: O(60) (or O(1) if the time duration of 60 is regarded as a constant), where n = time.length.