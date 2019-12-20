catNames = []
while True:
    count = len(catNames) + 1
    print(f"Enter the name of cat {count} or \
        press enter to exit")
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #Concatenate
print('The cat names are:')
for name in catNames:
    print(' '+ name)