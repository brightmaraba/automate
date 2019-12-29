import random
numberOfStreaks = 0
tossResult = []
count = 0
index = 0

for currentTossResult in range(10000):
    randomFlip = random.randint(1, 2)
    if randomFlip == 1:
        currentTossResult = 'H'
    else:
        currentTossResult = 'T'

    tossResult.append(currentTossResult)

