l = [44, 22, 87, 11, 2, 10, 99, 122, 33, 32, 16]

for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)
