def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def next_prime_palindrome(num):
    while True:
        num += 1
        if is_prime(num) and is_palindrome(num):
            return num
num=int(input())
result = next_prime_palindrome(num)
print(result)