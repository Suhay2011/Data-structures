print("n & (n-1) clears the rightmost set bit")
print(" 12 & 11 =", 12 & 11)
print(" 8 & 7", 8 & 7)

n = int(input("Enter a number to check if it is a power of 2 or not"))

if n > 0 and (n & (n - 1)) == 0:
    print(n, "Is a power of 2")
else:
    print(n, "is not a power of 2")