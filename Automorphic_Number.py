def is_automorphic_number(n):
    sq = n ** 2
    while n > 0:
        if n % 10 != sq % 10:
            return False
        n //= 10
        sq //= 10
    return True
n = int(input())
if is_automorphic_number(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")