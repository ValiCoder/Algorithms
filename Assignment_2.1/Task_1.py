# Task 1: Implement a singly linked list and write functions to:
# o	Add a node at the end of the list.
# o	Delete a specific node from the list.
# o	Search for a given element in the list.
from operator import index


class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, root) -> None:
        self.root = root

    def append(self, val: int) -> None:
        tmp = self.root
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val=val)

    def output(self) -> None:
        tmp = self.root
        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.next
        print("") # Ensures a new line after printing

    def search(self, val: int) -> str:
        tmp = self.root
        index = 0
        while tmp:
            if tmp.val == val:
                return f"Element {val} found at position {index+1}"
            tmp = tmp.next
            index += 1
        return "Element not found"

    def pop(self):
        if not  self.root:
            print("The list is empty")
            return

        if not  self.root.next:
            self.root = None
            return

        tmp = self.root
        while tmp.next and tmp.next.next:
            tmp=tmp.next
        tmp.next=None

    def reverse(self):
        prev = None
        curr = self.root
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.root = prev

    def delete(self, val: int):
        if not self.root:
            print("The list is empty")
            return

        if self.root.val == val :
            self.root = self.root.next
            return

        tmp = self.root
        while tmp.next:
            if tmp.next.val ==val:
                tmp.next = tmp.next.next
                return
            tmp = tmp.next

# Moved outside the class (correct indentation)
root = Node(10)
ll = LinkedList(root=root)

ll.append(15)
ll.append(30)
ll.output()
print(ll.search(15))
ll.reverse()
ll.output()
ll.delete(15)
ll.output()
print(ll.search(15))
ll.output()

n = int(input("Enter number of elements to add: "))

def inputs(n):
    for i in range(n):
        ll.append(int(input(f"Enter element {i+1}: ")))

inputs(n)
ll.output()
