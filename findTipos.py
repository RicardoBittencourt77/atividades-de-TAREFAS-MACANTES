""" Encontra erros comuns de digitação como vários espaços entre palavras,
repetição acidental de palavras ou vários pontos de exclamação no final das
sentenças.

    Finds common typos like multiple spaces between words,
accidental repetition of words or multiple exclamation marks at the end of sentences
sentences."""

import re

text = 'We are a lot of funny funny !!!!!!!! funny funny funny funny, I said it        33333 times!!!!!!!!'
words = []
new_words = []

wordsRE = re.compile(r'(\w+|[,.]+|\s\s+|[!?]+$)')
found_words = wordsRE.findall(text)

for groups in found_words:
    # bool(re.search(r'\d\d+', groups[0:]) == True)
    if any(char.isdigit() for char in groups[0:]):
        words.append(groups[0])
    elif any(char.isspace() for char in groups[0:]):
        groups[0] == None
    elif any(char == '!' or char == '?' for char in groups[0:]):
        words.append(groups[0])
    else:
        words.append(groups[0:])

for i in range(len(words)-1):
    if words[i] != words[i+1]:
        new_words.append(words[i])
if words[-1] != words[-2]:
    new_words.append(words[-1])

new_text = ' '.join(new_words)
new_text2 = ''

for i in range(len(new_text)-2):
    if new_text[i+1] == ',' or new_text[i+1] == '.':
        continue
    else:
        new_text2 += new_text[i]

new_text2 += new_text[-1]

print(new_text2)
