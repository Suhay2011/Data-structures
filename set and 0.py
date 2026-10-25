print(" 5=", bin(5)[2:])
print("5 | 2="
      , 5 | 2, " binary:", bin(5 | 2)[2:])

input("Zero a bit - AND turns it OFF. Press Enter ")
print("7 =", bin(7)[2:])
print(" 7 & 5 =", 7 & 5, " binary:", bin(7 & 5)[2:])

n = int(input("Enter a number   "))

if n > 0 and (n & (n - 1)) == 0:
    print("It's a power of 2")
else:
    print("It's not a power of 2! Try again")
