# Creating a node class
class Node:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Creating a Double linked list  Class
class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):

        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):

        if self.head is None:
            node = Node(data, None, None)
            self.head = node
        else:
            self.head.next = Node(data, None, self.head.next)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        current_node = self.head
        dd_str = ''
        while current_node:
            dd_str += str(current_node.data) + ' --> '
            current_node = current_node.next
        print(dd_str)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        current_node = last_node
        dd_str = ''
        while current_node:
            dd_str += current_node.data + '-->'
            current_node = current_node.prev
        print("Link list in reverse: ", dd_str)

    def get_last_node(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        return current_node

    def get_length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next

        return count

