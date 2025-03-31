

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def delete_at_pos(self, position):
        if position == 0:
            return self.head.next
        
        i = 0
        cur = self.head
        while cur:
            if position-1 == i:
                break
            i+=1
            cur = cur.next
            
        cur.next = cur.next.next
        return self.head

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next and cur.next.value != value:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next

    def display(self):
        cur = self.head
        while cur:
            print(cur.value, end=" → ")
            cur = cur.next
        print("None")


sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()
sll.delete_at_pos(2)
sll.display()

