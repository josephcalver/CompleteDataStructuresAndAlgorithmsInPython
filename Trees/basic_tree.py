class TreeNode:

    def __init__(self, data, children=None):
        if children is None:
            children = []
        self.data = data
        self.children = children

    def __str__(self, level=0):
        string = " " * level + str(self.data) + "\n"
        for child in self.children:
            string += child.__str__(level + 1)
        return string

    def add_child(self, child_node):
        self.children.append(child_node)


root = TreeNode('Drinks', [])
hot_drinks = TreeNode('Hot Drinks', [])
cold_drinks = TreeNode('Cold Drinks', [])
root.add_child(hot_drinks)
root.add_child(cold_drinks)

tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
hot_drinks.add_child(tea)
hot_drinks.add_child(coffee)

coke = TreeNode('Coca Cola', [])
tonic = TreeNode('Tonic Water', [])
lemonade = TreeNode('Lemonade', [])
cold_drinks.add_child(coke)
cold_drinks.add_child(tonic)
cold_drinks.add_child(lemonade)

print(root)
