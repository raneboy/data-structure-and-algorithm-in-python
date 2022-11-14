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
# ------------------------------------------------------------- #
# Determine max width of tree

# Method with usage of hashmap
def max_width_in_tree(head):
    if  head != None:
        queue = []
        
        # Used a heshmap tp record node and its level
        hashmap = {}
        level_node_num = 0
        current_tree_level = 1

        max_level = -1e-10
        max_value = -1e-100

        hashmap[head] = current_tree_level
        queue.append(head)

        while len(queue) != 0:
            head = queue.pop()
            current_node_level = hashmap[head]
            # The node at the same level
            if current_node_level == current_tree_level:
                level_node_num += 1
                
            # Node in the same level as we observe the tree
            else:
                if level_node_num > max_value:
                    max_level = current_tree_level

                max_value = max(max_value, level_node_num)
                
                current_tree_level += 1
                level_node_num = 1

            if head.left != None:
                hashmap[head.left] = current_node_level + 1
                queue.insert(0, head.left)

            if head.right != None:
                hashmap[head.right] = current_node_level + 1
                queue.insert(0, head.right)

        # The last node in the tree in the bottom most which has the highest node number
        # and this node do not used in the comparison of total node number of a level
        # Thus, finalize whole process (last node) :
        if level_node_num > max_value:
                max_level = current_tree_level

        max_value = max(max_value, level_node_num)
        
        print("Max Width: level", max_level, "width", max_value)
    
# max_width_in_tree(node1)

# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# Determine wether the tree is complete, full. balance or binary search tree

# Determine whether a binary tree is BST
# If a binary is BTS, the list will be in an accesding order  like [1, 3, 7, 34, 35, 67] (In Order Traverse)
# A binary tree is considered BTS if the value of left < head < right from top to bottom

# The binary tree in order traverse is [2, 5, 6, 8, 10, 12, 13]
head = Node(8)
head.left = Node(5)
head.right = Node(12)

head.left.left = Node(2)
head.left.right = Node(6)

head.right.left = Node(10)
head.right.right = Node(13)

prev_value = 0.001

class CheackBTS:
    def __init__(self) -> None:
        self.prev_value = -1e-20

    def check_if_BTS(self, head):
        if head == None: 
            return True
        
        is_left_bst = self.check_if_BTS(head.left)
        
        if not is_left_bst:
            return False

        if head.data <= self.prev_value:
            return False
        else:
            self.prev_value = head.data

        return self.check_if_BTS(head.right)
   

# solution = CheackBTS()
# print(solution.check_if_BTS(node1))
# solution2 = CheackBTS()
# print(solution2.check_if_BTS(head))


# The other algorithm to check whether a tree id BST

def is_binary_serch_tree(head):
    return process(head)[0]

# Return [is_BTS_boolean, max value, min value]
def process(head):
    if head == None:
        return None

    left_side = process(head.left)
    right_side = process(head.right)

    max_value = head.data
    min_value = head.data

    if left_side != None:
        max_value = max(max_value, left_side[1])
        min_value  = min(min_value, left_side[2])

    if right_side != None:
        max_value = max(max_value, right_side[1])
        min_value = min(min_value, right_side[2])  

    is_bst = True

    if left_side != None and (not left_side[0] or left_side[1] >= head.data):
        is_bst = False

    if right_side != None and (not right_side[0] or head.data >= right_side[1]):   
        is_bst = False

    return [is_bst, max_value, min_value]

# print(is_binary_serch_tree(node1))
# print(is_binary_serch_tree(head))


# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# Determine whether a binary tree is complete

# The binary tree below is designed to be not complete
head2 = Node(1)
head2.left = Node(2)
head2.right = Node(3)

head2.left.left = Node(4)
head2.left.right = Node(5)

head2.right.right = Node(7)


def is_binary_tree_complete(head):
    if head != None:
        queue = []
        queue.append(head)

        # When reach the node which do not have right child, change to true
        leaf = False

        left = None
        right = None

        while len(queue) != 0:
            head = queue.pop()
            left = head.left
            right = head.right

            if (leaf and (leaf != None and right != None)) or (left == None and right != None):
                return False

            if left != None:
                queue.insert(0, left)

            if right != None:
                queue.insert(0, right)

            if left != None and right == None:
                leaf = True

        return True

# print(is_binary_tree_complete(head))
# print(is_binary_tree_complete(head2))

# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# Determine whether a binary tree is balance

# The binary tree below is not balance
head3 = Node(1)
head3.left = Node(2)
head3.right = Node(3)

head3.left.left = Node(4)
head3.left.right = Node(5)

head3.right.left = Node(6)
head3.right.right = Node(7)

head3.left.left.left = Node(8)

head3.left.left.left.left = Node(16)

def is_binary_tree_balance(head):
    return process_balance(head)[0]


# The return [is_balanced_bool, node_depth]
def process_balance(head):
    if head == None:
        return [True, 0]

    left_side = process_balance(head.left)
    right_side = process_balance(head.right)

    # Plus 1 because this indicate the next node height (from bottom to top)
    height = max(left_side[1], right_side[1]) + 1

    is_balance = left_side[0] and right_side[0] and abs(left_side[1] - right_side[1]) < 2

    return [is_balance, height]

# print(is_binary_tree_balance(head))
# print(is_binary_tree_balance(head3))

# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# Determine whether a binary tree is full

# The binary tree below is full
head4 = Node(1)
head4.left = Node(2)
head4.right = Node(3)

head4.left.left = Node(4)
head4.left.right = Node(5)

head4.left.right.left = Node(6)
head4.left.right.right = Node(7)

def is_binary_tree_full(head):
    return process_full(head)


def process_full(head):
    if head == None:
        return False

    left_side = process_full(head.left)
    right_side = process_full(head.right)

    is_full = True
    
    if (left_side and not right_side) or (right_side and not left_side):
        is_full = False

    return is_full
        
# print(is_binary_tree_full(head))
# print(is_binary_tree_full(head2))
# print(is_binary_tree_full(head4))

# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# Lowest common ancestor

head5 = Node(1)
node12 = Node(2)
node13 = Node(3)
node14 = Node(4)
node15 = Node(5)
node16 = Node(6)
node17 = Node(7)
node18 = Node(8)
node19 = Node(9)
node20 = Node(10)

head5.left = node12
head5.right = node13

head5.left.left = node14

head5.left.left.left = node15
head5.left.left.left.left = node16

head5.left.left.right = node17
head5.left.left.right.right = node18

def lowest_common_ancestor(head, node_one, node_two):
    hashmap = {}
    hashmap[head] = head

    # Get a hashmap with key is current node, value is its parent
    process_lca(head, hashmap)

    # Use a set to record all of the parent of node_one
    node_hashset = set()
    i_node = node_one
    
    # The loop end when reach the highest head
    while i_node != hashmap[i_node]:
        node_hashset.add(i_node)
        i_node = hashmap[i_node]
    node_hashset.add(head)

    node_set2 = []
    i_node2 = node_two
    while i_node2 != hashmap[i_node2]:
        node_set2.append(i_node2)
        i_node2 = hashmap[i_node2]
    node_set2.append(head)

    for node in node_set2:
        if node in node_hashset:
            return node.data

def process_lca(head, hashmap):
    if head == None:
        return

    hashmap[head.left] = head
    hashmap[head.right] = head
    process_lca(head.left, hashmap)
    process_lca(head.right, hashmap)



# Determine lca version two (shorter lines of code)
def lowest_common_ancestor_two(head, node_one, node_two):
    if head == None or head == node_one or head == node_two:
        return head

    left = lowest_common_ancestor_two(head.left, node_one, node_two)
    right = lowest_common_ancestor_two(head.right, node_one, node_two)

    if left != None and right != None:
        return head

    return (right, left)[left != None]


# print(lowest_common_ancestor(head5, node16, node18))
# print(lowest_common_ancestor_two(head5, node16, node18).data)


# ------------------------------------------------------------- #
# ------------------------------------------------------------- #

# Given Tree Structure   #
#           7               
#         /              
#       3
#      /  \             # The in order traverse is:
#     /     6           # 4-> 2-> 5-> 1-> 6-> 3-> 7
#    1                  
#     \     5           # And it take O(N) to know that
#      \  /             # 6 is printed after 1
#       2
#         \             # We decide to make each node not only point to two child but also a parent based on in order traverse
#           4           # In this case, the parent of 1 is 6, the parent of 5 is 1 etc.
#
#                       # By doing so, we can quickly know what is the value will be printed at certain node
#                       # Plus, we can determine what come next with only O(k), not O(N)
#                       # k indicate diatance between two value, such as, distance between "2" and "1" is 2


class NodeWithParent:
    def __init__(self, value) -> None:
        self.data = value
        self.parent = None
        self.left = None
        self.right = None

head6 = NodeWithParent(1)
node22 = NodeWithParent(2)
node23 = NodeWithParent(3)
node24 = NodeWithParent(4)
node25 = NodeWithParent(5)
node26 = NodeWithParent(6)
node27 = NodeWithParent(7)

# The most top
head6.left = node22
head6.right = node23
head6.parent = node26

# Left side
node22.parent = node25
node22.left = node24
node22.right = node25

node24.parent = node22
node25.parent = head6

# Right side
node23.parent = node27
node23.left = node26
node23.right = node27

node26.parent = node23
node27.parent = None


def get_successor_after_node(node):
    if node == None:
        return None

    if node.right != None:
        return get_left_most(node.right)
    else:
        parent_node = node.parent
        while parent_node != None and parent_node.left != None:
            node = parent_node
            parent_node = node.parent
        return node


def get_left_most(node):
    if node == None:
        return None

    while node.left != None:
        node = node.left

    return node


# The parent of 4 is 2
# print(get_successor_after_node(node24).data)
# The parent of 2 is 5
# print(get_successor_after_node(node22).data)
# The parent of 5 is 1
# print(get_successor_after_node(node25).data)
# The parent of 1 is 6
# print(get_successor_after_node(head6).data)
# The parent of 6 is 3
# print(get_successor_after_node(node26).data)
# The parent of 3 is 7
# print(get_successor_after_node(node23).data)


# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# Serialize and deserialize a binary tree


def serialize_by_pre_order(head):
    if head == None:
        return "#_"

    res = str(head.data) + "_"
    res += serialize_by_pre_order(head.left)
    res += serialize_by_pre_order(head.right)
    return res

def reconstrut_tree_by_serial(serial_string):
    queue = []
    values = serial_string.split("_")
    for value in values:
        queue.append(value)
    print(queue)
    return process_serial_to_tree(queue)

def process_serial_to_tree(queue):
    node_val = queue.pop(0)
    
    if node_val == "#":
        return None

    head = Node(int(node_val))
    head.left = process_serial_to_tree(queue)
    head.right = process_serial_to_tree(queue)
    return head


# tree_seial = serialize_by_pre_order(node1)
# print(tree_seial)
# head7 = reconstrut_tree_by_serial(tree_seial)
# print(head7.data)
# print(head7.left.data, "  ", head7.right.data)
# print(head7.left.left.data, "  ", head7.left.right.data, "  ", head7.right.left.data, "  ", head7.right.right.data)


# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# Interview question - paper folding

# When paper is folded one time left-right, it create a concave
# When paper is folder again, it create another a concave and a convex
# It is observed that it will create a concave at the left of the first concave, and a convex at the right


# True mean concave
def print_paper_folding_process(start_fold, end_fold, down):
    if start_fold > end_fold:
        return

    print_paper_folding_process(start_fold + 1, end_fold, True)
    print(("|-|", "|_|")[down], end=" ")
    print_paper_folding_process(start_fold + 1, end_fold, False)

print(print_paper_folding_process(1, 3, True))