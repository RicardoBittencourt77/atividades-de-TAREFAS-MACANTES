import pyperclip
import re
from time import sleep

# exemplos de formatos procurados: 2023/01/01, 1-1-2023, 01-01-2023, 01/01/2023
dateFormat = re.compile(r'''((\d{4}[/-]
                    \d{1,2}[/-]
                    \d{1,2})
                    |(\d{1,2}[/-]
                    \d{1,2}[/-]
                    \d{4})
                    |(\d{2}\/
                    \d{2}\/
                    \d{4})
                    |(\d{1,2}[/-]
                    \d{1,2}[/-]
                    \d{2}))''', re.X)   # X corresponde a VERBOSE

"""
    # procura pelo formato do tipo '1 de janeiro de 2023'
    # link para teste: https://www.historiadobrasil.net/resumos/datas_importantes.htm
dateFormat = re.compile(r'''[0-9\s]+
                    [a-z\s]+
                    [a-z\s]+
                    \d{4}''', re.VERBOSE)
"""

text = pyperclip.paste()

matches = []

print('\nLooking for Dates...')
sleep(3)

for groups in dateFormat.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\nCopied to clipboard:')
    print('\n'.join(matches))
else:
    print('No date found.')
