import random
print('My name is')
for i in range(5):
    print(f'Jimmy Five Times {i}')

total = 0
for num in range(101):
    total = total + num
print(total)

for i in range(12, 16):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)

print('')

for i in range(5):
    print(random.randint(1, 20))