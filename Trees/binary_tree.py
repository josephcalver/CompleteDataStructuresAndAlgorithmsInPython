from Queues.queue_linked_list import Queue


class Node:

    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return self.data


def insert(root_node, new_node):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            node = queue.dequeue()
            if node.value.left_child is not None:
                queue.enqueue(node.value.left_child)
            else:
                node.value.left_child = new_node
                return "Node successfully inserted"

            if node.value.right_child is not None:
                queue.enqueue(node.value.right_child)
            else:
                node.value.right_child = new_node
                return "Node successfully inserted"


def get_deepest_node(root_node):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        deepest_node = None
        while not queue.is_empty():
            node = queue.dequeue()
            if node.value.left_child is not None:
                queue.enqueue(node.value.left_child)

            if node.value.right_child is not None:
                queue.enqueue(node.value.right_child)
            deepest_node = node.value
        return deepest_node


def delete_deepest_node(root_node, deepest_node):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            node = queue.dequeue()
            if node.value is deepest_node:
                node.value = None
                return "Deepest node deleted"
            else:
                if node.value.left_child:
                    if node.value.left_child is deepest_node:
                        node.value.left_child = None
                        return "Deepest node deleted"
                    else:
                        queue.enqueue(node.value.left_child)
                if node.value.right_child:
                    if node.value.right_child is deepest_node:
                        node.value.right_child = None
                        return "Deepest node deleted"
                    else:
                        queue.enqueue(node.value.right_child)
        return "Deepest node not found"


def delete(root_node, delete_node):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            node = queue.dequeue()
            if node.value is delete_node:
                deepest_node = get_deepest_node(root_node)
                node.value.data = deepest_node.data
                delete_deepest_node(root_node, deepest_node)
                return "Node successfully deleted"
            else:
                if node.value.left_child is not None:
                    queue.enqueue(node.value.left_child)

                if node.value.right_child is not None:
                    queue.enqueue(node.value.right_child)
        return "Failed to delete"


def preorder_traversal(node):
    if not node:
        return

    print(node.data)

    preorder_traversal(node.left_child)
    preorder_traversal(node.right_child)


def inorder_traversal(node):
    if not node:
        return

    inorder_traversal(node.left_child)

    print(node)

    inorder_traversal(node.right_child)


def postorder_traversal(node):
    if not node:
        return

    postorder_traversal(node.left_child)

    postorder_traversal(node.right_child)

    print(node)


def level_order_traversal(node):
    if not node:
        return

    queue = Queue()
    queue.enqueue(node)
    while not queue.is_empty():
        # print("Queue contains: {}".format(queue))
        node = queue.dequeue()
        print(node.value.data)
        if node.value.left_child is not None:
            queue.enqueue(node.value.left_child)
        if node.value.right_child is not None:
            queue.enqueue(node.value.right_child)


def find(node, value):
    # using level-order traversal
    if not node:
        return

    queue = Queue()
    queue.enqueue(node)
    while not queue.is_empty():
        node = queue.dequeue()
        if node.value.data == value:
            print("Tree contains value: {}".format(value))
            break
        if node.value.left_child is not None:
            queue.enqueue(node.value.left_child)
        if node.value.right_child is not None:
            queue.enqueue(node.value.right_child)
    else:
        print("Tree does not contain value: {}".format(value))


root = Node("Drinks")
hot = Node("Hot")
cold = Node("Cold")
root.left_child = hot
root.right_child = cold

tea = Node("Tea")
coffee = Node("Coffee")
hot.left_child = tea
hot.right_child = coffee

preorder_traversal(root)
print("*" * 10)

inorder_traversal(root)
print("*" * 10)

postorder_traversal(root)
print("*" * 10)

level_order_traversal(root)
print("*" * 10)

find(root, "Tea")

find(root, "Cola")
print("*" * 10)

rootbeer = Node("Root Beer")
print(insert(root, rootbeer))
level_order_traversal(root)
print()

# print(get_deepest_node(root))
# print(delete_deepest_node(root, get_deepest_node(root)))
# print(get_deepest_node(root))
# print()

delete(root, tea)
level_order_traversal(root)
print()

delete(root, hot)
level_order_traversal(root)
print()
