a,b,c,d,e=map(int,input().split())
p=(a+b+c+d+e)/5
if p>=90:
    print("Grade A")
elif p>=80:
    print("Grade B")
elif p>=70:
    print("Grade C")
elif p>=60:
    print("Grade D")
elif p>=40:
    print("Grade E")
else:
    print("Grade F")

