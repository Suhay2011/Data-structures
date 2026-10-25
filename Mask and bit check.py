n = int(input("Enter a number: "))
k = int(input("Enter bit position (starting from 0): "))
mask = 1 << k
if n & mask:
    print("Bit is set")
else:
    print("Bit is not set")
print("After setting bit:", n | mask)
print("After clearing bit:", n & ~mask)
