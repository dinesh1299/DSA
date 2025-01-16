class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __str__(self):
        cur = self.front
        out = ""
        while cur:
            out += str(cur.data) + ", "
            cur = cur.next
        return out[:-2]

    def push(self, val):
        node = Node(val)
        if not self.front:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def insert_at_begin(self, val):
        if not self.front:
            self.push(val)
            return

        cur = self.front
        self.front = Node(val)
        self.front.next = cur
        self.size += 1

    def insert_at_end(self, val):
        if not self.rear:
            self.push(val)
            return
        cur = self.front
        while cur.next:
            cur = cur.next

        node = Node(val)
        cur.next = node
        node.next = None
        self.size += 1

    def insert_at(self, index, val):
        if index < 0 or index > self.size-1:
            return
        if index == 0:
            self.insert_at_begin(val)
            return
        if index == self.size-1:
            self.insert_at_end(val)
            return
        cur = self.front
        itr = 1
        while cur:
            if index == itr:
                break
            cur = cur.next
            itr += 1
        node = Node(val)
        node.next = cur.next
        cur.next = node
        self.size += 1

    def pop(self):
        if self.front:
            self.front = self.front.next
            self.size -= 1

    def remove(self, val):
        cur = self.front
        if cur is None:
            return
        if cur.data == val:
            self.pop()
        else:
            found = False
            while cur.next:
                if cur.next.data == val:
                    found = True
                    break
                cur = cur.next
            if not found:
                return
            if not cur.next.next:
                cur.next = None
            else:
                cur.next = cur.next.next
            self.size -= 1


qu = Queue()
print('Inserting begin..')
qu.insert_at_begin(7)
print(qu)

print('Pushing..')
qu.push(1)
qu.push(2)
qu.push(3)
qu.push(4)
qu.push(5)
print(qu)
print('Inserting at..')
qu.insert_at(5, 12)
print(qu)
print('Inserting begin..')
qu.insert_at_begin(6)
print(qu)
print('Inserting End..')
qu.insert_at_end(19)
print(qu)
print('Removing..')
qu.pop()
print(qu)
