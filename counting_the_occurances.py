a=str(input())
b=str(input())
c=0
for i in a:
    if i==b:
        c+=1
if c==0:
    print(-1)
else:
    print(c)