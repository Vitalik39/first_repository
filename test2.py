my_file = open('test_file.txt', encoding='utf-8')

dataFile = my_file.readline()

count = 0
flag = 0
for i in range(len(dataFile)):
    if dataFile[i] != ' ' and flag == 0:
        count += 1
        flag = 1
    else:
        if dataFile[i] == ' ':
            flag = 0

print(dataFile)
print(len(dataFile), 'симв.', count, 'сл.')

dataFile = my_file.readline()

count2 = 0
flag2 = 0

for i in range(len(dataFile)):
    if dataFile[i] != ' ' and flag2 == 0:
        count2 += 1
        flag2 = 1
    else:
        if dataFile[i] == ' ':
            flag2 = 0

print(dataFile)
print(len(dataFile), 'симв.', count2, 'сл.')

dataFile = my_file.readline()

count3 = 0
flag3 = 0

for i in range(len(dataFile)):
    if dataFile[i] != ' ' and flag3 == 0:
        count3 += 1
        flag3 = 1
    else:
        if dataFile[i] == ' ':
            flag3 = 0

print(dataFile)
print(len(dataFile), 'симв.', count3, 'сл.')

dataFile = my_file.readline()

count4 = 0
flag4 = 0

for i in range(len(dataFile)):
    if dataFile[i] != ' ' and flag4 == 0:
        count4 += 1
        flag4 = 1
    else:
        if dataFile[i] == ' ':
            flag4 = 0

print(dataFile)
print(len(dataFile), 'симв.', count4, 'сл.')