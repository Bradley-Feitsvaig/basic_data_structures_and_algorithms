# Implementation of some basic recursion exercises

# 1) Two functions that finds the factorial of any number.
#     One should use recursion, the other should just use for loop

def findFactorialRecursive(number):
    if number == 1 :
        return 1
    return number * findFactorialRecursive(number-1)

def findFactorialIterative(number):
    answer = 1
    for i in range(2,number+1):
        answer *=i
    return answer

# 2) Given a number N return the index value of the Fibonacci sequence, where the sequence is:
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
#   the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3
#   For example: fibonacciRecursive(6) should return 8
#   2 functions, one recirsive and one iterative

def fibonacciRecursive(n):  #O(2^n)
    if n < 2:
        return n
    return fibonacciRecursive(n-1)+fibonacciRecursive(n-2)

def fibonacciIterative(n): #O(n)
    if n < 2:
        return n
    first = 0
    second = 1
    answer=first+second
    for i in range (2,n+1):
        answer=first+second
        first = second
        second = answer
    return answer


#3) Reverse String With Recursion

def reverseStringRecursive(string):
    if len(string) == 0:
        return ""
    return string[-1]+reverseStringRecursive(string[0:-1])


def main():
    print(findFactorialRecursive(5))
    print(findFactorialIterative(5))
    print(fibonacciRecursive(12))
    print(fibonacciIterative(12))
    print(reverseStringRecursive("Bradley"))

if __name__ == "__main__":
    main()