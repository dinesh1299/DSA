
class HashTable:
    def __init__(self, max):
        self.max = max
        self.lst = [None for i in range(max)]

    def get_hash(self, data):
        x = 0
        for i in data:
            x += ord(i)
        return x % self.max

    def __setitem__(self, key, val):
        index = self.get_hash(key)
        self.lst[index] = val

    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.lst[index]

    def __delitem__(self, key):
        index = self.get_hash(key)
        self.lst[index] = None


hash = HashTable(100)
hash['march 6'] = 200
hash['march 6'] = 2000
print(hash.lst)
print(hash['march 6'])

del hash['march 6']

print(hash.lst)
print(hash['march 6'])
