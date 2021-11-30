# 1. Feladat
print('--- 1. Feladat ---')
nums = [3, 4, 9, 6, 2]
for x in nums:
    if (x % 2 == 0):
        print(str(x) + ": oszthato")
    else:
        print(str(x) + ": nem oszthato")

# 2. Feladat
print('--- 2. Feladat ---')
players = ['Peter', 'Kate', 'John']
counter = 0
for elem in players:
    counter += 1
    print(str(counter) + '. ' + elem)

# 3. Feladat
print('--- 3. Feladat ---')
inputArray = ['', 4, True]
typeList = []

for element in inputArray:
    if type(element) is int:
        typeList.append('integer')
    if type(element) is str:
        typeList.append('string')
    if type(element) is bool:
        typeList.append('boolean')

print("Bemenet:")
print(inputArray)
print("Kimenet:")
print(typeList)
