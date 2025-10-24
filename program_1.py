fullName = input("Enter full legal name: ")
name = fullName.split()
for string in name:
    print(string[0].upper(), sep=' ', end=' ')
    print(".", sep=' ', end=' ')
