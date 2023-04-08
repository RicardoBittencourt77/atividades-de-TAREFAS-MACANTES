import pyperclip


def isPhoneNumberUS(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


def isPhoneNumberBR(text):
    if len(text) != 14:
        return False
    for i in range(1, 3):
        if not text[i].isdecimal():
            return False
    if text[0] != '(':
        return False
    if text[3] != ')':
        return False
    if text[4] != ' ':
        return False
    for i in range(5, 9):
        if not text[i].isdecimal():
            return False
    if text[9] != '-':
        return False
    for i in range(10, 14):
        if not text[i].isdecimal():
            return False
    return True


def isCellPhoneNumberBR(text):
    if len(text) != 15:
        return False
    for i in range(1, 3):
        if not text[i].isdecimal():
            return False
    if text[0] != '(':
        return False
    if text[3] != ')':
        return False
    if text[4] != ' ':
        return False
    for i in range(5, 10):
        if not text[i].isdecimal():
            return False
    if text[10] != '-':
        return False
    for i in range(11, 15):
        if not text[i].isdecimal():
            return False
    return True


def is0800PhoneNumberBR(text):
    if len(text) != 13:
        return False
    for i in range(0, 4):
        if not text[i].isdecimal():
            return False
    if text[4] != ' ':
        return False
    for i in range(5, 8):
        if not text[i].isdecimal():
            return False
    if text[8] != ' ':
        return False
    for i in range(9, 13):
        if not text[i].isdecimal():
            return False
    return True


"""
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
"""

# message = 'Cal me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# message = 'Cal me at (79) 99555-1011 tomorrow. (79) 99555-9999 is my office.'
message = pyperclip.paste()

print('\nSearching for US phone number:')
for i in range(len(message)):
    chunk1 = message[i:i+12]
    if isPhoneNumberUS(chunk1):
        print('Phone number found: ' + chunk1)

print('\nSearching for Brazil phone number:')
for i in range(len(message)):
    chunk2 = message[i:i+14]
    if isPhoneNumberBR(chunk2):
        print('Phone number found: ' + chunk2)

print('\nSearching for Brazil cell phone number:')
for i in range(len(message)):
    chunk3 = message[i:i+15]
    if isCellPhoneNumberBR(chunk3):
        print('Phone number found: ' + chunk3)

print('\nSearching for Brazil 0800 phone number:')
for i in range(len(message)):
    chunk4 = message[i:i+13]
    if is0800PhoneNumberBR(chunk4):
        print('Phone number found: ' + chunk4)

print('\n\nDone')
