import math

def countTeams(num, skills, minSize, minL, maxL):
    k = len([L for L in skills if minL <= L <= maxL])
    res = 0
    # there are always k possible associates, but we can pick minSize <= size <= k of these associates to form possible teams.
    for i in range(minSize, k+1): 
        res += math.factorial(k) // (math.factorial(k - i) * math.factorial(i))
    return res    

print(countTeams(6, [12,4,6,13,5,10], 3, 4, 10))