
def merge(left, right):
    i, j = 0, 0
    res = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    while i < len(left):
        res.append(left[i])
        i += 1
    
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

arr = [42, 21, 4, 2, 65, 87, 34, 12, 90, 3, 27]

print(merge_sort(arr))

# left = [1, 4, 6, 9]

# right = [2, 5, 7, 8]

# print(merge(left, right))