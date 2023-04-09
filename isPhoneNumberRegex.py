import re
import pyperclip

# message = 'Cal me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# message = 'Cal me at (21) 3555-1011 tomorrow. (21) 99555-9999 is my office.'
message = pyperclip.paste()

print('\nSearching for USA phone number:')
isPhoneNumberUSRegex = re.compile(r'\d{3}.\d{3}.\d{4}')
findedPhoneNumberUS = (isPhoneNumberUSRegex.findall(message))
for i in findedPhoneNumberUS:
    print(i)

# o símbolo ? é usado para dizer que o caracter é opcional
# o .(ponto) é usado para representar qualquer caracter na posição

print('\nSearching for Brazil phone number:')
isPhoneNumberBrazilRegex = re.compile(r'\W?\d{2}\W?.?\d{4,5}\W?\d{4}')
findedPhoneNumberBR = (isPhoneNumberBrazilRegex.findall(message))
for i in findedPhoneNumberBR:
    print(i)

print('\n\nDone')
