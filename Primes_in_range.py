def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def count_primes_between(m, n):
    count = 0
    for num in range(m, n + 1):
        if is_prime(num):
            count += 1
    return count
m=int(input())
n=int(input())
result = count_primes_between(m, n)
print(result)