class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


#  Task 2
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


# Task 1
def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current


def sum_of_tree(node: Node, total=0):
    total += node.val
    if node.left:
        total = sum_of_tree(node.left, total=total)
    if node.right:
        total = sum_of_tree(node.right, total=total)
    return total


root = Node(2)
insert(root, 1)
insert(root, 3)
insert(root, 0)
insert(root, 4)

print("Minimum", min_value_node(root).val)
print("Maximum", max_value_node(root).val)
print("Sum", sum_of_tree(root))
