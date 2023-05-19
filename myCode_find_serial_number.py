import re
import pyperclip

# text recebe uma string que contém matrículas das quais se quer esconder digitos
# text receives a string containing license plates from which you want to hide digits
text = pyperclip.paste()

# a regex procura por uma string formada por '10 números', '1 -' e '2 números'
# the regex searches for a string consisting of '10 numbers', '1 -' and '2 numbers'
find_regex = re.compile(r'\d{10}-\d{2}')

# substirui a parte da string selecionada pela máscara com vários 'X'
# replace the part of the string selected by the mask with several 'X's
new_text = re.sub(r'\d{8}-\d{2}', 'XXXXXXXX-XX', text)
print(new_text)

text_to_string = find_regex.findall(text)
for i in text_to_string:
    new_text2 = i.replace(i[2:6], 'XXXX')
    print(new_text2)
