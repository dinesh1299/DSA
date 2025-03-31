class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        temp = self.head
        while temp and temp.value != value:
            temp = temp.next
        if temp:
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ⇄ ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        while temp:
            print(temp.value, end=" ⇄ ")
            temp = temp.prev
        print("None")


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display_forward()
dll.display_backward()
dll.delete(20)
dll.display_forward()
