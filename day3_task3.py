def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(17))
print(is_prime(21))