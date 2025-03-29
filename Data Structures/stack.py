class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur = self.head
        out = ""
        while cur:
            out += f'{cur.data}, '
            cur = cur.next
        return out[:-2]

    def push(self, val):
        node = Node(val)
        if not self.head:
            node.next = None
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        self.head = self.head.next

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
    
    # def insert(self, val):
    #     if not self.head:
    #         self.head = Node(val)
    #         self.max = val
    #     else:
    #         node = Node(val)
    #         node.next = self.head
    #         self.head = node
    #         if val > self.max:
    #             self.max = val

    # def delete(self):
    #     self.head = self.head.next

    # def print_max(self):
    #     return self.max

# def getMax(operations):
#     res = []
#     stack = Stack()
#     for ope in operations:
#         o = [int(i) for i in ope.split()]
#         if o[0] == 1:
#             stack.insert(o[1])
#         elif o[0] == 2:
#             stack.delete()
#         elif o[0] == 3:
#             res.append(stack.print_max())
#     print(res)
#     return res


# n = int(input().strip())
# ops = []

# for _ in range(n):
#     ops_item = input()
#     ops.append(ops_item)

# res = getMax(ops)
# print(res)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print('insertion')
print(stack)
stack.pop()
print(stack)
# stack.pop()
# print('deletion')
# print(stack)
stack.reverse()
print(stack)
