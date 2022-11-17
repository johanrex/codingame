import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def test_is_prime():
    for i in range(100):
        if is_prime(i):
            print(i)


def sieve_of_eratosthenes(num):
    is_prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:

        # If prime[p] is not
        # changed, then it is a prime
        if is_prime[p] == True:

            # Updating all multiples of p
            for i in range(p * p, num + 1, p):
                is_prime[i] = False
        p += 1

    return is_prime
