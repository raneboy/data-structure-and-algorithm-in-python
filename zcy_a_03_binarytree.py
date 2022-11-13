
class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left = None
        self.right = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

# Layer 1
node1.left = node2
node1.right = node3

# Layer 2
node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

# ------------------------------------------------------------- #
# Recursive method of traversing binary tree

# Pre-order is head-left-right
def recursive_pre_order_traverse(head):
    if head == None: return

    print(head.data, end=" ")
    recursive_pre_order_traverse(head.left)
    recursive_pre_order_traverse(head.right)

# recursive_pre_order_traverse(node1)

def recursive_in_order_traverse(head):
    if head == None: return

    recursive_in_order_traverse(head.left)
    print(head.data, end=" ")
    recursive_in_order_traverse(head.right)

# recursive_in_order_traverse(node1)

def recursive_pos_order_traverse(head):
    if head == None: return

    recursive_pos_order_traverse(head.left)
    recursive_pos_order_traverse(head.right)
    print(head.data, end=" ")

#recursive_pos_order_traverse(node1)

# ------------------------------------------------------------- #
# un-recursive method of traversing binary tree

# Pre-order is head-left-right
# Add right side into stack first then left
def non_recursive_pre_order_traverse(head):
    if head != None:
        stack = []
        stack.append(head)
        output = []
        while len(stack) != 0:
            head = stack.pop()
            output.append(head.data)

            if(head.right != None):
                stack.append(head.right)

            if(head.left != None):
                stack.append(head.left)

        print(output)

# non_recursive_pre_order_traverse(node1)

# post order left-right-head
def non_recursive_pos_order_traverse(head):
    if head == None: return

    stack = []
    output = []
    stack.append(head)
    while len(stack) != 0:
        head = stack.pop()
        output.append(head.data)

        if head.left != None:
            stack.append(head.left)
        
        if head.right != None:
            stack.append(head.right)

 
    while len(output) != 0:
            print(output.pop(), end=" ")

# non_recursive_pos_order_traverse(node1)

# post order left-right-head version two
def non_recursive_pos_order_traverse_two(head):
    if head != None:
        stack = []
        output = []
        stack.append(head)
        current = None
        while len(stack) != 0:
            current = stack[len(stack)-1]
            if current.left != None and head != current.left and head != current.right:
                stack.append(current.left)
            elif current.right != None and head != current.right:
                stack.append(current.right)
            else:
                output.append(stack.pop().data)
                head = current
        
        print(output)


# non_recursive_pos_order_traverse_two(node1)

# In order left-head-right
def non_recursive_in_order_traverse(head):
    if head != None:
        stack = []
        output = []
        while len(stack) != 0 or head != None:

            # Reach the left most until none, then move to right by a step
            if head != None:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                output.append(head.data)
                head = head.right
        
        print(output)

# non_recursive_in_order_traverse(node1)


# ------------------------------------------------------------- #
# Breadth first traverse

def breadth_first_traverse(head):
    if head != None:
        queue = []
        output = []
        queue.append(head)
        while len(queue) != 0:
            head = queue.pop()
            output.append(head.data)
            if head.left != None:
                queue.insert(0, head.left)

            if head.right != None:
                queue.insert(0, head.right)

        print(output)

# breadth_first_traverse(node1)


# ------------------------------------------------------------- #
# Depth first traverse 

# Determine whether a target number inside a binary tree

target = 6

def depth_first_traverse(head, target):
    if head != None:
        stack = []

        while len(stack) != 0 or head != None:
            
            if head != None:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()

                if head.data == target:
                    return True

                head = head.right

        return False

# print(depth_first_traverse(node1, target))
# print(depth_first_traverse(node1, 10))