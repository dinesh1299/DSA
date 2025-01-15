

l=[44,22,87,11,2,10,99,122,33,32,16]

for i in range(1,len(l)):
	j=i-1
	k=l[i]
#	for j in range(0,i+1):
#		if l[j]>k:
#			l[i],l[j]=l[j],l[i]
	
	while l[j]>k and j>=0:
		l[j+1]=l[j]
		j-=1
	l[j+1]=k
print(l)
	