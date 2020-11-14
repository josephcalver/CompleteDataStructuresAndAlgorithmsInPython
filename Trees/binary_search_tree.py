class Node:

    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert_node(data, self.root)

    def __insert_node(self, data, node):
        if data <= node.data:
            if node.left_child:
                self.__insert_node(data, node.left_child)
            else:
                new_node = Node(data)
                node.left_child = new_node
        else:
            if node.right_child:
                self.__insert_node(data, node.right_child)
            else:
                new_node = Node(data)
                node.right_child = new_node

    def traverse(self):
        if self.root:
            self.__inorder_traversal(self.root)

    def __inorder_traversal(self, node):
        if node.left_child:
            self.__inorder_traversal(node.left_child)

        print("{} --> ".format(node), end=" ")

        if node.right_child:
            self.__inorder_traversal(node.right_child)

    def search(self, value):
        if self.root:
            return self.__search(value, self.root)

    def __search(self, value, node):
        if not node:
            return "Not found"

        if node.data == value:
            return "Found"
        else:
            if value < node.data:
                return self.__search(value, node.left_child)
            else:
                return self.__search(value, node.right_child)

    def delete(self, value):
        if self.root:
            self.__delete(value, self.root)

    def __delete(self, value, node):
        if node is None:
            return node

        if value < node.data:
            node.left_child = self.__delete(value, node.left_child)
        elif value > node.data:
            node.right_child = self.__delete(value, node.right_child)
        else:
            # value == node.data -- delete the current node
            # if node children
            if not node.left_child and not node.right_child:
                return None

            if not node.left_child:
                temp = node.right_child
                node = None
                return temp
            elif not node.right_child:
                temp = node.left_child
                node = None
                return temp

            # node with two children -- get successor / lowest value in right side of subtree
            temp = self.get_min(node.right_child)
            node.data = temp.data
            node.right_child = self.__delete(temp.data, node.right_child)
        return node

    def get_min(self, node):
        current = node
        while node.left_child:
            current = current.left_child
        return current


bst = BinarySearchTree()
bst.insert(5)
bst.insert(10)
bst.insert(3)
bst.insert(1)
bst.insert(9)
bst.insert(9)
bst.traverse()
print()
print(bst.search(3))
bst.delete(9)
bst.traverse()
bst.delete(10)
print()
bst.traverse()
print()
bst.delete(5)
bst.traverse()
print()
print(bst.search(10))
