import math


def prime_factors(n):
    prime_list = []
    while n % 2 == 0:
        n = n // 2
        prime_list.append(2)
    for i in range(3, int(math.sqrt(n) + 1), 2):
        while n % i == 0:
            n //= i
            prime_list.append(i)
    if n > 2:
        prime_list.append(n)
    return prime_list


if __name__ == "__main__":
    print(prime_factors(10))
