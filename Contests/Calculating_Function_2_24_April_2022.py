'''For a positive integer n let's define a function f:

f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn

Your task is to calculate f(n) for a given integer n.'''
from sys import stdout,stdin
n=int(stdin.readline())
if(n%2==0):
    print((n+1)//2)
else:
    print(-(n+1)//2)
