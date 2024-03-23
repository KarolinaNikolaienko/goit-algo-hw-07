# Завдання 3

# Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку 
# або в AVL-дереві.
# Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

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

def postorder_traversal(root):
    if root:
        sum = root.val
        if root.left:
            sum += postorder_traversal(root.left)
        if root.right:
            sum += postorder_traversal(root.right)
        return  sum

def main():
    # Створення дерева
    #               10
    #             /     \
    #           2        15
    #         /   \        \
    #       1      5        19
    root = Node(10)
    root = insert(root, 15)
    root = insert(root, 2)
    root = insert(root, 1)
    root = insert(root, 5)
    root = insert(root, 19)
    root = insert(root, 8)

    print("Зворотний обхід:")
    print(postorder_traversal(root))


if __name__ == "__main__":
    main()