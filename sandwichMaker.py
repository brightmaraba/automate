import pyinputplus as pyin
breadType = {'wheat': 30, 'white': 40, 'sourdough': 50}
proteinType = {'Chicken': 30, 'Turkey': 40, 'Ham': 50, 'Tofu': 60}
cheeseType = {'Cheddar': 5, 'Swiss': 10, 'Mozzarella': 20}
veggieType = {'Lettuce': 2, 'Mayo': 3, 'Mustard': 4, 'Tomato': 5}
orderList = []

print("WELCOME TO LA CASA BELLE")
print("Select Bread Type")
breadResponse = pyin.inputMenu(['Wheat', 'White', 'Sourdough'], default='Wheat')
orderList.append(breadResponse)
print("Select Protein Type")
proteinResponse =  pyin.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], default='Chicken')
orderList.append(proteinResponse)
print("Do you want Cheese")
cheeseChoice = pyin.inputYesNo()
print(cheeseChoice)
if cheeseChoice == 'yes':
    print("Select Cheese Type")
    cheeseType = pyin.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'])
    orderList.append(cheeseType)
else:
    print("You have selected no Cheese")

print("Do you want Mayo?")
mayoChoice = pyin.inputYesNo()
if mayoChoice == 'yes':
    orderList.append('Mayo')
print("Do you want mustard?")
mustardChoice = pyin.inputYesNo()
if mustardChoice == 'yes':
    orderList.append('Mustard')
print("Do you want lettuce?")
lettuceChoice = pyin.inputYesNo()
if lettuceChoice == 'yes':
    orderList.append('Lettuce')
print("Do you want Tomato?")
tomatoChoice = pyin.inputYesNo()
if tomatoChoice == 'yes':
    orderList.append('Tomato')





