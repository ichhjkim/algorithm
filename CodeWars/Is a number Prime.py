def is_prime(num):
    if num < 2:
        return False
    else:
        t = int(num ** (1 / 2))
        for i in range(2, t + 1):
            if not num%i: return False

    return True

print(is_prime(75))