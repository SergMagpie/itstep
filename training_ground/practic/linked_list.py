class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"Node data {self.data}"
# HEAD | Node("b") -> Node(24) -> Node("st") -> None

class LinkedList:
    
    def __init__(self, nodes) -> None:
        self.head = None
        if nodes is not None:
            current_node = Node(nodes.pop(0))
            self.head = current_node
            for elem in nodes:
                current_node.next = Node(elem)
                current_node = current_node.next

    def add(self, data, place=-1):
        new_node = Node(data)
        if place == 0:
            new_node.next = self.head
            self.head = new_node
            return True
        count = 1
        node = self.head
        while node:
            if count == place or not node.next:
                new_node.next = node.next
                node.next = new_node
                return True
            count += 1
            node = node.next
       

    def len_list(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
            
    def find(self, searched_data):
        node = self.head
        while node is not None:
            if node.data == searched_data:
                return node
            node = node.next
        return None

    def remove(self, data):
        '''
        Remove first element with data and return True if success else return False
        '''
        previous_node = None
        node = self.head
        while node is not None:
            if node.data == data:
                if previous_node is None:
                    self.head = node.next
                    del node
                    return True
                previous_node.next = node.next
                del node
                return True
            previous_node = node
            node = node.next
        return False

    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == "__main__":
    linked_list = LinkedList(['b', "24", "st", "1213"])


    print(linked_list)
    print(linked_list.find("b"))
    print(linked_list.len_list())
    # print(linked_list.remove("b"))
    # print(linked_list.remove("1213"))
    linked_list.add("333", 0)
    linked_list.add("222", 1)
    linked_list.add("444", 2)
    linked_list.add("555", 6)
    linked_list.add("666")
    print(linked_list)
    