

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head

        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        count = 0
        while count < index:
            cur = cur.next
            count += 1
        return cur

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        cur_node = self.get_node(index - 1)
        next_node = cur_node.next
        cur_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next


linked_list = LinkedList(10)
linked_list.append(15)
linked_list.append(16)
linked_list.append(17)
linked_list.print_all()
print()
linked_list.get_node(1)
linked_list.add_node(0, 1000)
linked_list.print_all()
print()
linked_list.delete_node(1)
linked_list.print_all()
