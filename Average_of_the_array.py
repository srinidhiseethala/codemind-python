n = int(input())
p = list(map(int,input().split()))
s=0
for i in range(n):
    s+=p[i]
    q=s/n
print("%0.2f"%q)