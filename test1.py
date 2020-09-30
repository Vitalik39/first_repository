def printMass(math, N):
    for i in range(N):
        for j in range(N):
            print('%4d' % mass[i][j], end='')

        print()


def readMass(filePath):
    file = open(filePath)

    mass = []
    N = 0

    for row in file:
        z = []
        rowStr = row.strip().split('  ')

        for i in range(len(rowStr)):
            z.append(int(rowStr[i]))

        mass.append(z)
        N += 1

    file.close()

    return mass, N


mass, N = readMass('test_file.txt')
printMass(mass, N)

for i in range(N):
    print('%4s' % "--", end='')
print()

summ = 0
c = 0
for i in range(N):
    s = 0
    for j in range(N):
        s += mass[j][i]
    print('%4d' % s, end='')
    if s > summ:
        summ = s
        c = i
print()
print(c + 1)