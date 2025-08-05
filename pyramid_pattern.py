def starcase(n):
    for i in range(1, 1+n):
        print(' ' * (n-i), end = '')
        print('* ' * i)
n = int(input("Enter the height of the pyramid: "))
starcase(n)