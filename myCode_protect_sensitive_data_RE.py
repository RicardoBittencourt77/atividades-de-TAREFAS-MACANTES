import re
import pyperclip

text = pyperclip.paste()

# encontra e modifica números de serie
# find and modify serial numbers
modified_text = re.sub(r'\d{8}-', 'XXXXXXXX-', text)

# encontra e modifica CPF (Cadastro de Pessoa Física)
# finds and modifies CPF (Individual Taxpayer Registration)
modified_text = re.sub(r'\d{3}\.', 'XXX.', modified_text)
modified_text = re.sub(r'-\d{2}', '-XX', modified_text)

print(modified_text)
