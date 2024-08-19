numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for a in numbers:
    if a > 1:
        for n in range(2, (a//2)+1):
            if a % n == 0:
                not_primes.append(a)
                break
        else:
            primes.append(a)

print(primes)
print(not_primes)
