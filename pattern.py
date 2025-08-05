def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return 2
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

num = int(input())
for j in range(num + 1):
    if is_prime(j):
        print(j, end=' ')

