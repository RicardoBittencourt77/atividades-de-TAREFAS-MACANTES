""" Encontra erros comuns de digitação como vários espaços entre palavras,
repetição acidental de palavras ou vários pontos de exclamação no final das
sentenças.

    Finds common typos like multiple spaces between words,
accidental repetition of words or multiple exclamation marks at the end of sentences
sentences."""

import re

text = 'We are a lot of fanny fanny fanny fanny fanny fanny   33333!!!!!!'
words = []
new_words = []

wordsRE = re.compile(r'([a-zA-Z]+|$[!?]+|\s\s+|\w\w+|\W\W+)')
found_words = wordsRE.findall(text)

for groups in found_words:
    # or bool(re.search(r'\d\d+', groups[0:]) == True)
    if any(char.isdigit() for char in groups[0:]):
        words.append(groups[0])
    else:
        words.append(groups[0:])

for i in range(len(words)-1):
    if words[i] != words[i+1]:
        new_words.append(words[i])

print(' '.join(new_words))
