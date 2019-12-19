while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe! What is your password? (Hint: A fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted!')