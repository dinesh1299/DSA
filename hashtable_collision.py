class Hash:
    def __init__(self, max):
        self.max = max
        self.lst = [[] for i in range(max)]

    def get_hash(self, data):
        x = 0
        for i in data:
            x += ord(i)
        return x % self.max

    def __setitem__(self, key, val):
        index = self.get_hash(key)
        found = False
        for i, j in enumerate(self.lst[index]):
            if j[0] == key:
                self.lst[index][i] = (key, val)
                found = True
                break
        if not found:
            self.lst[index].append((key, val))

    def __getitem__(self, key):
        index = self.get_hash(key)
        res = 'Not found'
        lst = self.lst[index]
        for i in lst:
            if i[0] == key:
                res = i[1]
                break
        return res

    def __delitem__(self, key):
        index = self.get_hash(key)
        lst = self.lst[index]
        for i, j in enumerate(lst):
            if j[0] == key:
                del self.lst[index][i]
                break


hash = Hash(100)
hash['march 6'] = 200
hash['march 6'] = 2000
print(hash.lst)
print(hash['march 6'])

del hash['march 6']

print(hash.lst)
print(hash['march 6'])
