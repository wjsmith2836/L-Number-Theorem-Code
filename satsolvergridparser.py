C = 3
N = 20
a = []
b = [[0 for i in range(N)] for j in range(N)]
count = 0
p = input()
p = p.split()      
for i in p:
    if not i == "v":
        a.append(int(i))
for i in a:
    if i > 0:
        b[count//N][count%N] = i%C
        count += 1
for row in b:
    print(row)


