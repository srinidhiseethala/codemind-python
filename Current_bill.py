n=int(input())
if n<=199:
    c=1.20
elif n>=200 and n<400:
    c=1.50
elif n>=400 and n<600:
    c=1.80
else:
    c=2.00
b=n*c
if b>400:
    sc=b*0.15
else:
    sc=100
tb=b+sc
print("%0.2f" %tb)