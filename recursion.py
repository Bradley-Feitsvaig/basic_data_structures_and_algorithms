# Implementation of some basic recursion exercises

# 1) Two functions that finds the factorial of any number.
#     One should use recursion, the other should just use for loop

def find_factorial_recursive(number):
    if number == 1 :
        return 1
    return number * find_factorial_recursive(number-1)

def find_factorial_iterative(number):
    answer = 1
    for i in range(2,number+1):
        answer *=i
    return answer

# 2) Given a number N return the index value of the Fibonacci sequence, where the sequence is:
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
#   the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3
#   For example: fibonacci_recursive(6) should return 8
#   2 functions, one recirsive and one iterative

def fibonacci_recursive(n):  #O(2^n)
    if n < 2:
        return n
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

def fibonacci_iterative(n): #O(n)
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

def reverse_string_recursive(string):
    if len(string) == 0:
        return ""
    return string[-1]+reverse_string_recursive(string[0:-1])


def main():
    print(find_factorial_recursive(5))
    print(find_factorial_iterative(5))
    print(fibonacci_recursive(12))
    print(fibonacci_iterative(12))
    print(reverse_string_recursive("Bradley"))

if __name__ == "__main__":
    main()