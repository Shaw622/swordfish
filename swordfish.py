while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello ' + str(name) + '. What is your password?(fish name)')
    password = input()
    if password == 'swordfish':
        break
print('認証しました')
