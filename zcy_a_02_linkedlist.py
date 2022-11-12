class LinkedList:
    def __init__(self, node=None) -> None:
        self.head = node
        
    # Add object at the end of linked list
    def put(self, node):
        if self.head == None:
            self.head = node
        else:
            i_node = self.head
            while(i_node.next != None):
                i_node = i_node.next
            i_node.next = node

    # Add object after the index
    def put_at(self, node, index):
        if index < -1 or index > self.length()-1:
            print("Out of range of the linked list")
            return
        elif index == -1:
            self.put_front(node)
            return
        
        temp_node = None
        i_node = self.head
        i = 0
        while i <= index :
            temp_node = i_node
            i_node = i_node.next
            i += 1

        temp_node.next = node
        node.next = i_node

    # Add object at front of the list
    def put_front(self, node):
        temp = self.head
        self.head = node
        node.next = temp

    # Remove the last object and return the value
    def get(self):
        if self.head == None:
            print("Empty list")
            return
        elif self.head.next == None:
            value = self.head.data
            self.head = None
            return value
        else:
            temp_node = None
            i_node = self.head
            while i_node.next != None:
                temp_node = i_node
                i_node = i_node.next
            value = i_node.data
            temp_node.next = None
            return value

    # Remove the object at index and return value
    def get_at(self, index):
        if index < 0 or index > self.length()-1:
            print("Out of range of the linked list")
            return
        if index == self.length()-1: 
            return self.get()
        if index == 0:
            return self.get_front()

        i = 0
        i_node = self.head
        while i < index - 1:
            i_node = i_node.next
            i += 1
        
        value = i_node.next.data
        i_node.next = i_node.next.next
   
        return value

    # Remove the first object and return the value
    def get_front(self):
        value = self.head.data
        self.head = self.head.next
        return value

    # Print the linked list
    def print_all(self):
        i_node = self.head
        node_list = []
        while(i_node != None):
            node_list.append(i_node.data)
            i_node = i_node.next
        print(node_list)

    # Swap two object location
    def swap(self, index_one, index_two):
        larger_index = 0
        smaller_index = 0

        if index_one > self.length()-1 or index_one < 0:
            print("Out of range of the linked list")
        elif index_two > self.length()-1 or index_two < 0:
            print("Out of range of the linked list")
        elif index_one == index_two:
            return
        else:
            if index_one > index_two:
                larger_index = index_one
                smaller_index = index_two
            else:
                larger_index = index_two
                smaller_index = index_one

        # Get the two node and remove from list
        node_one = self.get_at(smaller_index)
        node_two = self.get_at(larger_index - 1)
 
        # Create two new note
        node_one = Node(node_one)
        node_two = Node(node_two)

        # Put the node at the swap index
        self.put_at(node_two, (0, smaller_index - 1)[smaller_index > -1])
        self.put_at(node_one, larger_index - 1)

    # Reverse the linked list
    def reverse(self):
        prev_node = None
        i_node = self.head
         
        while i_node != None:
            next_node = i_node.next
            i_node.next = prev_node
            prev_node = i_node
            i_node = next_node
        self.head = prev_node


    # Return length of linked list
    def length(self):
        i_node = self.head
        count = 0
        while i_node != None:
            count += 1
            i_node = i_node.next
        return count

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

# ------------------------------------------------------------- #
# Some operation on linked list

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

list = LinkedList()
list.put(node1)
list.put(node2)
list.put(node3)
list.put(node4)

# Put item into list
list.print_all()
list.put_at(node5, 2)
list.put_front(node6)
list.put_at(node7, 2)
list.print_all()

# Remove item from the list
print(list.get())
print(list.get_front())
print(list.get_at(2))
list.print_all()

# Get the count of the list
print(list.length())

# Swap two element
list.swap(0, 2)
list.print_all()

# Reverse the list
list.print_all()
list.reverse()
list.print_all()
