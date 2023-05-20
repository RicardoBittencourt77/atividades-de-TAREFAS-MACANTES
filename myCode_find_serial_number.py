import re
import pyperclip

# text recebe uma string que contém matrículas das quais se quer esconder digitos
# text receives a string containing license plates from which you want to hide digits
text = pyperclip.paste()

# 1 - substitui a parte da string selecionada pela máscara com vários 'X' e devolve o texto com as strings modificadas
# 1 - replaces the part of the string selected by the mask with several 'X's and returns the text with the modified strings
new_text = re.sub(r'\d{8}-\d{2}', 'XXXXXXXX-XX', text)
print(new_text)

# 2- a regex procura por uma string formada por '10 números', '1 -' e '2 números'
# 2- the regex searches for a string consisting of '10 numbers', '1 -' and '2 numbers'
find_regex = re.compile(r'\d{10}-\d{2}')

# substitui a parte da string selecionada e devolve a string modificada
# replaces the selected string part and returns the modified string
print()
text_to_string = find_regex.findall(text)
for i in text_to_string:
    new_text2 = i.replace(i[2:6], 'XXXX')
    print(new_text2)

# 3 - outra forma de fazer a substituição
# 3 - another way to replace
print()
find_regex2 = re.compile(r'(\d{2})(\d{8})-(\d{2})')
new_text3 = find_regex2.sub(r'\2', 'XXXXXXXX-')
group0 = find_regex2.findall(text)
for i in group0:
    group1 = i[0]
    group2 = i[2]
    print(str(group1) + new_text3 + str(group2))

# 4 - modifica apenas a primeira string encontrada
# 4 - modifies only the first string found
print()
group0 = find_regex2.search(text)
group1 = group0.group(1)
group2 = group0.group(3)
print(str(group1) + new_text3 + str(group2))
