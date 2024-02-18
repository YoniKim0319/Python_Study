# Task1 :  If-Else
'''Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n %2 != 0:
        print('Weird')
    elif 2<=n<=5:
        print('Not Weird')
    elif 6<=n<=20:
        print('Weird')
    elif 20<=n:
        print('Not Weird')

# Task2 :  Arithmetic Operators
'''The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.'''
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Task3: Loops (문제 해석 때문에 해맴)
'''The provided code stub reads and integer, n , from STDIN. For all non-negative integers i<n , print i**2.'''
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
