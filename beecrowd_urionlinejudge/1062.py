"""
Read an integer value X (1 <= X <= 1000).  Then print the odd numbers from 1 to X, each one in a line, including X if is the case.

Input
The input will be an integer value.

Output
Print all odd values between 1 and X, including X if is the case.
"""

x = int(input())

for i in range(x+1):
    if (i%2 != 0):
        print(i)
