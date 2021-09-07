import random
mainLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
mainNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
mainSymbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
lettersNum = int(input("How many letters would you like in your password?\n"))
symbolsNum = int(input(f"How many symbols would you like?\n"))
numbersNum = int(input(f"How many numbers would you like?\n"))

letters = []
symbols = []
numbers = []

if lettersNum != 0:
    for i in range(lettersNum):
        randLetters = random.randint(0, len(mainLetters)-1)
        letters.append(mainLetters[randLetters])

if symbolsNum != 0:
    for i in range(symbolsNum):
        randSymbols = random.randint(0, len(mainSymbols)-1)
        symbols.append(mainSymbols[randSymbols])

if numbersNum != 0:
    for i in range(numbersNum):
        randNumbers = random.randint(0, len(mainNumbers)-1)
        numbers.append(mainNumbers[randNumbers])

easyPass = letters + symbols + numbers
print(easyPass)

hardPass = easyPass
random.shuffle(hardPass)
print(hardPass)

hardString = ''.join(hardPass)
print("Your Password:", hardString)
