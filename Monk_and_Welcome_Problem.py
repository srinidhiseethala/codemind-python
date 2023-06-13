n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i,j in zip(l1,l2):
    print(i+j,end=' ')