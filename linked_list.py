
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def __str__(self):
        res = ""
        curr_node = self.head
        while curr_node:
            res += str(curr_node.data) + " -> "
            curr_node = curr_node.next
        res += "None"
        return res

    def insert_by_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        curr_node = self.head
        for i in range(index - 1):
            if curr_node.next:
                curr_node = curr_node.next
            else:
                break
        new_node.next = curr_node.next
        curr_node.next = new_node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print(linked_list)  # Виведе: 1 -> 2 -> 3 -> 4 -> None

    linked_list.insert_by_index(2, 5)
    print(linked_list)  # Виведе: 1 -> 2 -> 5 -> 3 -> 4 -> None

    linked_list.insert_by_index(0, 6)
    print(linked_list)  # Виведе: 6 -> 1 -> 2 -> 5 -> 3 -> 4 -> None

    linked_list.insert_by_index(30, 7)
    print(linked_list)  # Виведе: 6 -> 1 -> 2 -> 5 -> 3 -> 4 -> 7 -> None
