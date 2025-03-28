def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [x for x in range(limit + 1) if is_prime[x]]

primes = sieve_of_eratosthenes(99)
prime_square_dict = {p: p * p for p in primes}

print(prime_square_dict)