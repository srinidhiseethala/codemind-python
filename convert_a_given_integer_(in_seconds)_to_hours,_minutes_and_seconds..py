sc=int(input())
h=int(sc/3600)
m=int((sc-(h*3600))/60)
s=int((sc-(h*3600))-(m*60))
print(f'H:M:S-{h}:{m}:{s}')