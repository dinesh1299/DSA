

l=[66, 22, 73, 12, 99, 1, 9, 5, 52, 34, 19]

for i in range(len(l)):
	min = i
	for j in range(i, len(l)):
		if l[j] < l[min]:
			min = j
	l[i], l[min] = l[min], l[i]
print(l)
