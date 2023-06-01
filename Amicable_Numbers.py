def sum_proper_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)
def are_amicable_numbers(a, b):
    sum_a = sum_proper_divisors(a)
    sum_b = sum_proper_divisors(b)
    return sum_a == b and sum_b == a
num1 = int(input())
num2 = int(input())
if are_amicable_numbers(num1, num2):
    print("Amicable")
else:
    print("Not Amicable")