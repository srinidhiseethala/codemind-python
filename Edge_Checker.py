a,b=map(int,input().split())
if a-b==-1 and b-a==1:
    print("Yes")
elif a-b==1 and b-a==-1:
    print("Yes")
elif a-b==-9 and b-a==9:
    print("Yes")
elif a-b==9 and b-a==-9:
    print("Yes")
else:
    print("No")