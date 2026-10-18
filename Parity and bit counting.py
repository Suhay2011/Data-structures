for n in [2, 3, 4, 5, 6, 7, 8, 9]:
    if n & 1:
        print("  ", n, "-> odd")
    else:
        print("  ", n, "-> even")

n = int(input("Enter a number (try 13 or 7):" ))
temp = n
while temp > 0:
    print("  binary:", bin(temp)[2:], "last bit:", temp & 1)
    temp >>= 1
print(" Total 1's in", n, "=", bin(n).count('1'))