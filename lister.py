cats = ['henry', 'drucila', 'jerry', 'tom']
print(cats[1:4])

for cat in range(len(cats)):
    print(f"Cat number {cat + 1} is named {cats[cat]}")

anotherCats = []
while True:
    print(f"Enter the name of the cat {str(len(anotherCats) + 1)} or enter nothing to stop.")
    name = input()
    if name == '':
        break
    anotherCats = anotherCats + [name]

print("The cat names are:")
for name, cat in enumerate(anotherCats):
    print(f" {name} : {cat}")