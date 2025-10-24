string =  input("Enter a string: ")
result = ""
for i in range (len(string)):
    character = string[i]
    if character.isupper():
        character = character.lower()
        result += " "
    result += character
print(result)