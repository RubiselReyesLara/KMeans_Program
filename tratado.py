FILE = open('datos\datos.txt', 'r')
FILE2 = open('datos\datos-tratados.txt', 'w')
i = 0

VECTOR = [eval(x.replace('\n','')) for x in FILE.readlines()[0:100]]
VECTOR = [x[:5] for x in VECTOR]

for i in VECTOR:
    if i[1] == 1 and i[2] == 1 and i[3] == 1 and i[4] == 1:
        i.append(0)
    elif i[1] <= 2 and i[2] <= 3 and i[3] <= 2 and i[4] <= 3:
        i.append(1)
    elif i[2] <= 4 and i[3] <= 2 and i[4] <= 2 or i[4] >= 2 or i[1] <= 4 and i[2] <= 2 and i[3] <= 2 and i[4] <= 2:
        i.append(2)
    elif i[1] <= 4 and i[2] <= 3 and i[3] <= 3 and i[4] <= 4 or i[1] <= 4 and i[2] <= 3 and i[3] <= 3 and i[4] <= 4:
        i.append(3)

    FILE2.write(f'{i}\n')
FILE2.close()

print(VECTOR)