import pyperclip
import re
from time import sleep

urls = re.compile(r'http://.*|https://.*')

text = pyperclip.paste()

findedurls = urls.findall(text)

print('\nFinding for URLs...')

sleep(5)

if len(findedurls) > 0:
    for i in findedurls:
        print(i)
else:
    print('Nothing finded.')
