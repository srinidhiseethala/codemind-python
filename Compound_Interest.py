P=int(input())
R=int(input())
T=int(input())
a=(1+(R/100))**T
b=P*a-P
print("%.2f" %b)