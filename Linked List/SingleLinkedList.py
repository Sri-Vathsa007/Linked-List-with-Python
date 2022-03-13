# Creating a Node class
class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = Node(data, None)

    def insert_values(self, data):
        self.head = None

        for d in data:
            self.insert_at_end(d)

    def print_node_values(self):
        if self.head is None:
            print("Linked list is empty")
            return

        current_node = self.head
        ll_atr = ""
        while current_node:
            ll_atr += f"{current_node.data}-->"
            current_node = current_node.next
        print(ll_atr)

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def remove_at(self, index):
        if index <= 0 or index > self.get_length():
            print("Linked list out of index range exception")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        current_node = self.head

        while current_node:
            if count == index - 1:
                current_node.next = current_node.next.next
                break

            current_node = current_node.next
            count += 1

    def insert_at(self, index, data):
        if index <= 0 or index > self.get_length():
            print("Linked list index out of range")

        if index == 0:
            return self.insert_at_beginning(data)

        count = 0
        current_node = self.head

        while current_node:
            if count == index - 1:
                node = Node(data, current_node.next)
                current_node.next = node
                break

            current_node = current_node.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        current_node = self.head

        while current_node:

            if data_after not in current_node.data:
                print(f"There is no {data_after} in the linked list")

            if current_node.data == data_after:
                current_node.next = Node(data_to_insert, current_node.next)
                break

            current_node = current_node.next

    def remove_by_value(self, data):
        current_node = self.head

        if data not in current_node.data:
            print(f"{data} not in linked list")

        if current_node.data == data:
            current_node = current_node.next
            return

        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                break

            current_node = current_node.next

# sll = SingleLinkedList()
# sll.insert_values(["a", "b", "c"])
# sll.print_node_values()
# sll.get_length()
# sll.remove_at(2)
# sll.print_node_values()
# print(sll.get_length())
# sll.insert_at(2, "c")
# sll.print_node_values()
# sll.insert_after_value("c", "d")
# sll.print_node_values()
# sll.remove_by_value("c")
# sll.print_node_values()
# sll.remove_by_value("d")
# sll.print_node_values()
