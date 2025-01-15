

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print(self, res=""):
        if self.left:
            self.left.print(res)
        print(self.data, end=", ")
        if self.right:
            self.right.print(res)

    def insert(self, val):
        if self.data == val:
            return
        if val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinaryTree(val)

        if val > self.data:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinaryTree(val)

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # def delete(self, val):
    #     if self.data == val


bi = BinaryTree(20)

bi.insert(10)
bi.insert(19)
bi.insert(31)
bi.insert(22)
bi.insert(11)
bi.insert(22)
bi.insert(35)
bi.insert(29)
bi.insert(17)
bi.print()
print(bi.search(11))
