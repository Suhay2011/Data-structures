n = int(input("Enter a number (try 5 or 12):"))
guess = input("Guess its binary: ")
print(" decimal", n, "-> binary", bin(n)[2:1])
print(" Your guess: ", guess) 

print("BITWISE AND")
print(" 12 = ", bin(12)[2:])
print(" 10 = ", bin(10)[2:])
print(" 12 & 10 = ", 12 & 10)

print("BITWISE OR")
print(" 12 | 10 = ", 12 | 10)
