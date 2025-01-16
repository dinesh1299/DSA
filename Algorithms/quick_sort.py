

def pn(a, l, h):
	pi = a[l]
	j = h
	for i in range(h, l-1, -1):
		if a[i] > pi:
			a[j], a[i] = a[i], a[j]
			j -= 1
	a[j], a[l] = a[l], a[j]
	return j
def q(a, l, h):
	if l < h:
		pi = pn(a, l, h)
		q(a, l, pi - 1)
		q(a, pi + 1, h)

l = [44, 1, 21, 11, 33, 77, 67, 89, 87, 23]
q(l, 0, len(l)-1)
print(l)


def pn(a, l, h):
		pi = a[h]
		i = l - 1
		for j in range(l, h):
			if a[j] < pi:
				i += 1
				a[i], a[j] = a[j], a[i]
		a[i + 1], a[h] = a[h], a[i + 1]
		return i + 1
		
def q(a, l, h):
	if l < h:
		p = pn(a, l, h)
		q(a, l, p - 1)
		q(a, p + 1, h)
l = [55, 44, 18, 9, 31, 99, 1, 33]
q(l, 0, len(l) - 1)
print(l)
