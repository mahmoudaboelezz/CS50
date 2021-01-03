height = int(input("Height: "))
for row in range(height):
    for space in range(height - (row + 1)):
        print(" ", end="")
    for brick in range(row + 1):
        print("#", end="")
    print("  ", end="")
    for brick in range(row + 1):
        print("#", end="")
    for space in range(height - (row + 1)):
        print(" ", end="")
    print()

