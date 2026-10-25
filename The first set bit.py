n = int(input("Enter a number: "))
if n == 0:
    print("No set bit")
else:
    pos = 1
    while n > 0:
        if n & 1:
            print("First set bit position:", pos)
            break
        n = n >> 1
        pos += 1 
