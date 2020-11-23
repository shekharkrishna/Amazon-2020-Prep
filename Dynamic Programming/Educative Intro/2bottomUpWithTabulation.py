def calculateFibo(n):
    dp = [0, 1]
    for i in range(2, n+1):
        #dp[i] = dp[i-1] + dp[i-2] Initial thought. Avoid it.
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]



def main():
    print('Fibonacci : ', calculateFibo(4))
    # nums = [1,2, 5,6,7,8,9,10,19]
    # print('Testing using List Comp: Test Case - [1,2, 5,6,7,8,9,10,19]:---', [calculateFibo(x) for x in nums])
    #
    # print("5th Fibonacci is ---> " + str(calculateFibo(5)))
    # print("6th Fibonacci is ---> " + str(calculateFibo(6)))
    # print("7th Fibonacci is ---> " + str(calculateFibo(7)))

main()



