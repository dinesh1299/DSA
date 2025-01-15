def binarysearch(v, a):
    s, l = 0, len(a) -1 
    
    while s <= l:
        m = (s + l) // 2
        if a[m] == v:
            return m
        elif a[m] < v:
            l = m + 1
        else:
            s = m - 1

print(binarysearch(6, [1,4,6,7,9,10,33,44]))