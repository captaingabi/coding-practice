#!/bin/python3

def isPalindrome(x: int) -> bool:
    x_str:str = str(x)
    i:int = 0
    while i < len(x_str)/2:
        if x_str[i] != x_str[-(i+1)]:
            return False
        i += 1
    return True

print(isPalindrome(121))
print(isPalindrome(1331))
print(isPalindrome(14641))
print(isPalindrome(0))
print(isPalindrome(10))
print(isPalindrome(-121))
