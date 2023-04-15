#! python3
# phoneAndEmail.py - Encontra números de telefone e endereço de e-mail no clipboard.

import pyperclip
import re

# Cria regex para telefone padrão BR.
phoneRegex = re.compile(r'''(
    (\d{2}|\(\d{2}\))?              # código de área
    (\s|-|\.)?                      # separador
    (\d{4,5})                       # primeiros 4 ou 5 dígitos
    (\s|-|\.)                       # separador
    (\d{4})                         # últimos 4 dígitos
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extensão
    )''', re.VERBOSE)

# Cria regex para email.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # nome do usuário
    @                           # símbolo @
    [a-zA-Z0-9.-]+              # nome do domínio
    (\.[a-zA-z]{2,4})           # ponto seguido de outros caracteres
    )''', re.VERBOSE)

# Encontra as correspondências no texto do clipboard.
text = str(pyperclip.paste())

# Link da página sugerida para o texte do código.
# https://nostarch.com/contactus

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copia os resultados para o clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email addresses found.')
