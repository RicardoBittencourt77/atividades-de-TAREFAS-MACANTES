#! python3
# bulletPointAdder.py - Acrescenta marcadores da Wikipedia no início
# de cada linha de texto do clipboard.

import pyperclip
text = pyperclip.paste()

# Separa as linhas e acrescenta os asteriscos.
lines = text.split('\n')
for i in range(len(lines)):     # pecorre todos os índices da lista "lines" em um loop
    # acrescenta um asterisco em cada string da lista "lines"
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
