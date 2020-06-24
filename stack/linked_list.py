class Node():
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._nodes = None

    def __str__(self):
        output = ''
        current_node = self.head
        while current_node is not None:
            output += f'{current_node.value} ->'
            current_node = current_node.next_node
        return output

    def add_to_head(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def remove_tail(self):
        current = self.head
        if self.head is None:
            return None
        while current is not None:
            if current.next_node == self.tail:
                self.tail = current
                return current
        return current.value

    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node
        return False

    def get_length(self):

        temp = self.head
        count = 0

        while (temp):
            count += 1
            temp = temp.next_node
        return count

    def get_max(self):
        if self.head is None:
            return self.head

        current_node = 0
        next_n = self.head.next_node

        while self.head is not None:
            if current_node <= next_n.value:
                current_node = next_n.value
            self.head = self.head.next_node

        return current_node