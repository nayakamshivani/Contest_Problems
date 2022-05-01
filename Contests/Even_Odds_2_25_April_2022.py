'''Being a nonconformist, Volodya is displeased with the current state of things, particularly with the order of natural numbers (natural number is positive integer number). He is determined to rearrange them. But there are too many natural numbers, so Volodya decided to start with the first n. He writes down the following sequence of numbers: firstly
all odd integers from 1 to n (in ascending order), then all even integers from 1 to n (also in ascending order). Help our hero to find out which number will stand at the position number k.'''

l=list(map(int,input().split()))
n=l[0]
k=l[1]


sum1=n//2
if(n%2!=0):
    if(k<=(sum1+1)):
        res=2*k-1
    else:
        k=k-(sum1+1)
        res=2*k
    print(res)
else:
    if(k<=(sum1)):
        res=2*k-1
    else:
        k=k-(sum1)
        res=2*k
    print(res)
