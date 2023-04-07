#! python3
# pw.py - Um programa para repositório de senhas que não é seguro.

import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# o primeiro argumento da linha de comando é o nome da conta
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

'''
    No Windows, um arquivo batch poderá ser criado para executar esse programa
com a janela Run de WIN-R.

    Digite o seguinte no editor de arquivo e salve  como pw.bat na pasta C:\Windows:

    @py.exe C:\Python34\pw.py %*
    @pause
    
    Com esse arquivo batch criado, executar o programa de senhas protegidas no Windows
é somente uma questão de pressionar WIN-R e digitar pw <nome-da-conta>.
'''
