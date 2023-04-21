import pyperclip
import re

urls = re.compile(r'http://.*|https://.*')

text = pyperclip.paste()

findedurls = urls.findall(text)

for i in findedurls:
    print(i)
