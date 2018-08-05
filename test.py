import math

l = []


def miao(num):
    flag = True
    i = 2
    square = int(math.sqrt(num)) + 1
    while i <= square:
        if num % i == 0:
            l.append(i)
            flag = False
            miao(num / i)
            i += 1
            break
        i += 1
    if flag:
        l.append(num)

miao(5)
print l

l.sort()
for i in range(len(l)):
    if l[i] % 2 == 0:
        X = 1

        for j in range(len(l)):
            if j == i:
                continue
            X *= l[j]

        print(str(l[i]) + " " + str(X))
        break

