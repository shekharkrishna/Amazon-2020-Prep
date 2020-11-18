def calculateFibonacci(n):
   
    if (n < 2):
        return n        
    return calculateFibonacci(n-1) + calculateFibonacci(n-2)
  

def main():
    print('Fibonacci : ', calculateFibonacci(4))

    print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
    print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
    print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))

    

main()

# There is alot of redundent task evenif we broke it to smaller parts. 
# My initial thoguht was to store it to some variable so that it would not have to compute it
# again and again like when fib(2) and fib(3) which seems to 
# go recompute fib(1) and fib(0) again and again.
