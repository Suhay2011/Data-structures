input("Bit Probe - (n >> j) & checks if bit j is ON. Press Enter")
print("12 = binary", bin(12)[2:], "bin 2:", (12 >> 2) & 1, "bin 1:", (12 >> 1) & 1)

n = int(input("Enter a number try(7 or 4): "))
print("binary:", bin(n)[2:])
guess = input("What is bit 2 of " + str(n) + "? (0 or 1)")

print(" ", n, "bit 2 = ", (n >> 2) & 1, "your guess: ", guess)
