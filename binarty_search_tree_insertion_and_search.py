class Node:

    def __init__(self,value):

        self.value = value
        self.right = None
        self.left = None


class Binary:
    def __init__(self):
        self.root = None

    def insert(self, value):

        if self.root is None:
            self.root = Node(value)
        else:
            self.recursive_insert(self.root, value)

    def recursive_insert( self,node, value):

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                node = node.left
                self.recursive_insert( node, value)
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                node = node.right
                self.recursive_insert( node, value)

    def search_node(self, value):
        if self.root == value:
            print("the value is root node")
        else:
            self.search_node_recursive(self.root, value)

    def search_node_recursive(self, node, value):
        if value==node.value:
            print("found")

        if value > node.value:
            print("right of " )
            print(node.value, end="\n")
            node = node.right
            self.search_node_recursive( node, value)
        elif value < node.value:
            print("left of")
            print(node.value ,end="\n")

            node = node.left
            self.search_node_recursive( node, value)


Binary_search_tree = Binary()
Binary_search_tree.insert(1)
Binary_search_tree.insert(2)
Binary_search_tree.insert(3)
Binary_search_tree.insert(5)
Binary_search_tree.insert(25)
Binary_search_tree.insert(21)
Binary_search_tree.search_node(5)
Binary_search_tree.search_node(21)
