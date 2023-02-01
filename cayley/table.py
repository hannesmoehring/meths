import csv, math

group = []
maxVal = 42

for n in range(maxVal):
    if math.gcd(maxVal, n) != 1:
        continue
    group.append(n)

dic = dict()
for y in group:
    for x in group:
        if y not in dic:
            dic[y] = {x: (x * y) % maxVal}
        else:
            dic[y][x] = (x * y) % maxVal

with open("exampleOutPutTable.csv", "w") as file:
    w = csv.DictWriter(file, group)
    for g in group:
        w.writerow(dic[g])