

def p(a,l,h):
	pi=a[l]
	j=h
	for i in range(h,l-1,-1):
		if a[i]>pi:
			a[j],a[i]=a[i],a[j]
			j-=1
			print('-----',a)
	a[j],a[l]=a[l],a[j]
	print(a)
	return j
def q(a,l,h):
	if l<h:
		pi=p(a,l,h)
		q(a,l,pi-1)
		q(a,pi+1,h)

l=[44,1,21,11,33,77,67,89,87,23]
q(l,0,len(l)-1)
print(l)

