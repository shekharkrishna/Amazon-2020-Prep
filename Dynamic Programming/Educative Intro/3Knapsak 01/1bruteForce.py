# Knapsack Brute force is recursive: Yes
# 01 means either we can pic the item or not
def solve_knapscak(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, currentIndex):
    # base case
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # We can either choose or not at the currentIndex

    # recursive call after CHOOSING the element at the currentIndex
    # if the weight of the element at the currentIndex exceeds the cpapcity, 
    # we shouldnt process this
    profitAtChoosing = 0
    if weights[currentIndex] <= capacity: 
        profitAtChoosing = profits[currentIndex] + knapsack_recursive(
            profits, weights, capacity - weights[currentIndex], currentIndex+1)

    # NOT CHOOSING: Excluding the element at the currentIndex, recursive call would be unchanged 
    # except the we move the pointer to next element. Here we start from index 0 so 
    # technically 0+1 
    profitAtNotChoosing = knapsack_recursive(profits, weights, capacity, currentIndex+1)

    return max(profitAtChoosing, profitAtNotChoosing)



def main():
    profits = [1, 6, 10, 16]
    weights = [1, 2,  3,  5]
    capacity = 7
    print(solve_knapscak(profits, weights, capacity))
main()