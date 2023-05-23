a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
s=0
for i in range(len(b)):
    if b[i]<c or  b[i]>d:
        s=s+b[i]
print(s)