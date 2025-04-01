def partition(a, l, h):
	pivot = a[h]
	i = l - 1
	for j in range(l, h):
		if a[j] < pivot:
			i += 1
			a[i], a[j] = a[j], a[i]
	a[i + 1], a[h] = a[h], a[i + 1]
	return i + 1
		
def q(a, l, h):
	if l < h:
		p = partition(a, l, h)
		q(a, l, p - 1)
		q(a, p + 1, h)
l = [55, 44, 18, 9, 31, 99, 1, 33]
q(l, 0, len(l) - 1)
print(l)
