# Завдання 1

# Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку 
# або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

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

def max_elem(root):
    if root:
        max = root.val
        if root.right:
            max = max_elem(root.right)
    return max

def main():
    # Створення дерева
    #               10
    #             /     \
    #           2        15
    #         /    \       \
    #       1       5       19
    
    root = Node(10)
    root = insert(root, 15)
    root = insert(root, 2)
    root = insert(root, 1)
    root = insert(root, 5)
    root = insert(root, 19)

    print(f"Максимальний елемент дерева: {max_elem(root)}")

if __name__ == "__main__":
    main()