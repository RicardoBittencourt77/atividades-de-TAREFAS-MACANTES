while True:
    print('Who are you?')
    name = input()
    if name != 'Richard':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
