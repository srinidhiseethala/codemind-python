a=int(input())
b=int(input())
for n in range(a,b):
    t=n
    r=0
    c=0
    while n:
        r=n%10
        c=c*10+r
        n=n//10
    if t==c:
        print(t,end=' ')