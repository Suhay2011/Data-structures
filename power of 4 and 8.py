n = int(input("Enter a number to check power of 4: "))

if n > 0 and (n & (n - 1)) == 0 and n % 3 == 1:
    print(n,"is a power if 4 ")

else:
    print(n,"is not a power of 4")