
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        new_node = Node(val)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def reverse(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev if temp.prev else temp

    def find_first(self):
            print(self.head.val)

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val if slow else None

    def display(self):
        temp = self.head
        while temp:
            print("None <-> ", temp.val, end=" <-> ")
            temp = temp.next
        print("None")


# Example usage
dl = DoublyLinkedList()
dl.insert_at_beginning(10)
dl.insert_at_beginning(20)
dl.insert_at_beginning(30)
dl.display()

print("Middle element:", dl.find_middle())
dl.reverse()
dl.display()
dl.find_first()