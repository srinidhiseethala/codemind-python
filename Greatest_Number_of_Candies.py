n=int(input())
lst=list(map(int,input().split()))
c=int(input())
for i in lst:
    k=i+c
    if max(lst)<=k:
        print(True,end=' ')
    else:
        print(False,end=' ')