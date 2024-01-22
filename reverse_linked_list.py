from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    head = None

    def insert_to_list(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            node = ListNode(value)
            node.next = self.head
            self.head = node

    def print_list(self):
        if not self.head:
            return None
        else:
            node = self.head
            while node:
                print(node.val, end=" ")
                node = node.next
        print("\n")

    def delete_node(self, value):
        previous = None
        current = self.head
        while current is not None:
            if (current.val == value):
                previous.next = current.next
            previous = current
            current = current.next

    def reverse_list(self):
        if not self.head:
            return None
        else:
            while self.head.next:
                self.head = self.head.next


def insert_values(linked_list: LinkedList, values: List[int]):
    for i in values:
        linked_list.insert_to_list(i)


linked_list = LinkedList()
insert_values(linked_list, [i + 1 for i in range(10)])
linked_list.print_list()
linked_list.delete_node(8)
linked_list.print_list()
linked_list.delete_node(3)
linked_list.print_list()
# linked_list.reverse_list()
# print(linked_list.print_list())
