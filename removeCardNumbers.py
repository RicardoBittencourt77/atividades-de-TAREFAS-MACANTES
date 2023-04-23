# Removing critical information like social security numbers or credit card numbers.

import pyperclip
import re

text = pyperclip.paste()

findCardNumbers = re.compile(
    r'((\d{3,4})(\s|-)(\d{4})(\s|-)(\d{4})(\s|-)(\d{4}))')
modifiedText = findCardNumbers.sub(r'XXXX XXXX XXXX XXXX', text)
print(modifiedText)
