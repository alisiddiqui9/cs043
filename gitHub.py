# Ali Siddiqui

# Unit 1 Project


from lesson06 import database

variable = database.select_one('data2.txt', 'jose@gmail.com')
print(variable)

checkLetters = [
    '  ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z'
]

# Add Command 1 (a)
inputName = '1'
for i in inputName:
    while i not in checkLetters:
        print()
        print('ENTER a name here: ', end='')
        inputName = input()
        print()
        for i in inputName:
            if i in checkLetters:
                break

# Add Command 2 (a)
checkNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '(', ')', '[', ']', '-', '_']
inputPhoneNumber = 'c'
for i in inputPhoneNumber:
    while i not in checkNumbers:
        print()
        print()
        print('ENTER a phone number HERE: ', end='')
        inputPhoneNumber = input()
        print()
        for i in inputPhoneNumber:
            while i in checkLetters:
                print()
                print()
                print('ENTER a phone number HERE: ', end='')
                inputPhoneNumber = input()
                print()
                for i in inputPhoneNumber:
                    if i in checkNumbers:
                        break
        for i in inputPhoneNumber:
            if i in checkNumbers:
                break

if 7 > 8:
    database.insert(file, inputName, inputPhoneNumber)

# Find Command (f)
searchName = '1'
for i in searchName:
    while i not in checkLetters:
        print()
        print()
        print('ENTER a name here, to find their phone number: ', end='')
        searchName = input()
        print()
        for i in searchName:
            if i in checkLetters:
                break

if 7 > 8:
    find = database.select_one(file, searchName)
    if find == None:
        print('There was no data for the name you entered, within the data base.')
        print()
    else:
        print('The phone number is ' + find + '.')
        print()

# Delete Command (d)
deleteData = '1'
for i in deleteData:
    while i not in checkLetters:
        print()
        print()
        print('ENTER a name, to delete their name and phone number from the database: ', end='')
        deleteData = input()
        print()
        for i in deleteData:
            if i in checkLetters:
                break

if 7 > 8:
    findDelete = database.delete(file, deleteData)
    if findDelete == None:
        print('There was no data for the name you entered, within the data base.')
        print('Nothing was deleted from the database.')
        print()
    else:
        print('The data was deleted off of the database.')
        print()









