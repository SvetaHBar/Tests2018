class Node(object):
    def __init__(self, data):
        self.data = data
        self.rightchild = None
        self.leftchild = None


class Tree(object):
    def __init__(self, node=None):
        self.root = node #instance attribute of class Tree  / property of class Tree / or variable => in our case it's a root
                         #self it's reference to current instance of the class => tree in our case
                         # we're added the argument to constructor node = None, for case if we want to create a sub tree
                         # like in delete case and move thr rightchild be a root


    def insert_node(self, value):
        if self.root is None:
            self.root = Node(value)
            return self.root
        elif self.root.data == value:
            raise Exception("duplicate")
        node = self.root
        while self.root:
            if value < node.data:  # go left
                if node.leftchild is None:
                    node.leftchild = Node(value)
                    # return node
                    return self.root
                else:
                    # insert_node(node.leftchild, value) #recursion
                    # return node
                    node = node.leftchild
            elif value > node.data:  # go right
                if node.rightchild is None:
                    node.rightchild = Node(value)
                    # return node
                    return self.root
                else:
                    # insert_node(node.rightchild, value)
                    # return node
                    node = node.rightchild

    #def search_node_value(self, node, data):
    def search_node_value(self, data):
        if self.root is None:
            return None
        node = self.root
        while node:
            if node.data == data:
                return node
            elif node.data > data:  # go left
                if node.leftchild:
                    # return search_node_value(node.leftchild, data)# recursion
                    node = node.leftchild
                else:
                    return False  # not found
            elif node.data < data:  # go right
                if node.rightchild:
                    # return search_node_value(node.rightchild, data) #recursion
                    node = node.rightchild
                else:
                    return False  # not found
        return node

    def min_node(self):
        node = self.root
        while node.leftchild:  # if left child exist
            node = node.leftchild  # move to the leftchild
        return node

    def max_node(self):
        node = self.root
        while node.rightchild:
            node = node.rightchild
        return node

    def search_parent_node(self, value):
        parentNode = None
        node = self.root
        while node:
            if value == node.data:
                # return parentNode
                break
            elif value < node.data:  # go left
                parentNode = node
                node = node.leftchild
            elif value > node.data:  # go right
                parentNode = node
                node = node.rightchild
        if parentNode and node is None:
            parentNode = None
        return parentNode

    def is_a_leaf(self, node):
        return node.leftchild is None and node.rightchild is None

    def inorder_traversal(self, root):
        list = []
        if root: #if using self.root - we were alwayes stay with root and not moving left or right to the children. root mitkadem im recurcive
            list = self.inorder_traversal(root.leftchild)
            list.append(root.data)
            list += self.inorder_traversal(root.rightchild)
        return list

    def preorder_traversal(self, root):
        list = []
        if root:
            list.append(root.data)
            list += self.inorder_traversal(root.leftchild)
            list += self.inorder_traversal(root.rightchild)
        return list

    def postorder_traversal(self, root):
        list = []
        if root:
            list = self.inorder_traversal(root.leftchild)
            list += self.inorder_traversal(root.rightchild)
            list.append(root.data)
        return list

    def delete_node(self, value):
        node_for_delete = self.search_node_value(value)
        parent = self.search_parent_node(node_for_delete.data)

        if self.root and parent is None:

            if self.is_a_leaf(self.root):
                if self.root.data == value:
                    self.root = None
                    return self.root
                else:
                    print("value not in the tree")
                    return False

            elif self.root.leftchild and self.root.rightchild is None:
                if self.root.data == value:
                    if self.root.leftchild.rightchild is None:
                        self.root = self.root.leftchild
                    # root.leftchild = None# we no need make left child = None, it's not work in case, left child have left child
                    # enough that left child is a the root and leftchild.leftchild is a new leftchild
                    else:
                        left_sub_tree = Tree(self.root.leftchild)  # we want our tree to start from leftchild
                        max_left_child_node = left_sub_tree.max_node()
                        parent_max_node = self.search_parent_node(max_left_child_node.data)
                        left_child = self.root.leftchild
                        self.root = max_left_child_node
                        self.root.leftchild = left_child
                        parent_max_node.rightchild = None # we want to delete the max node , klomar disconnect him from the parent
                    return self.root

            elif self.root.leftchild is None and self.root.rightchild:
                if self.root.data == value:
                    if self.root.rightchild.leftchild is None:  # we checking only left child because his value smaller than child value (rightchild always bigger)
                        self.root = self.root.rightchild
                    else:
                        right_sub_tree = Tree(self.root.rightchild)#we start the our tree from rightchild
                        min_right_child_node = right_sub_tree.min_node()
                        parent_min_node = self.search_parent_node(min_right_child_node.data)
                        right_child = self.root.rightchild
                        self.root = min_right_child_node  # new root
                        self.root.rightchild = right_child
                        parent_min_node.leftchild = None
                    return self.root

            elif self.root.leftchild and self.root.rightchild:
                right_sub_tree = Tree(self.root.rightchild)# we want our tree to start from rightchild
                #right_sub_tree.root = self.root.rightchild
                min_right_child_node = right_sub_tree.min_node()
                left_child = self.root.leftchild
                right_child = self.root.rightchild
                if self.root.data == value:
                    if self.root.rightchild == min_right_child_node:
                        self.root = min_right_child_node
                        self.root.leftchild = left_child
                    elif self.root.rightchild != min_right_child_node:
                        self.root = min_right_child_node
                        self.root.leftchild = left_child
                        self.root.rightchild = right_child
                    return self.root

 # if node not a root

        if self.root and parent is not None:
            # deleted node has no children
            # this scenario handled before
            if self.is_a_leaf(node_for_delete):
                if node_for_delete.data < parent.data:
                    parent.leftchild = None
                elif node_for_delete.data > parent.data:
                    parent.rightchild = None
                return self.root


            elif node_for_delete.leftchild and node_for_delete.rightchild is None:
                if node_for_delete.data < parent.data:
                    parent.leftchild = node_for_delete.leftchild
                elif node_for_delete.data > parent.data:
                    parent.rightchild = node_for_delete.leftchild
                return self.root



            elif node_for_delete.leftchild is None and node_for_delete.rightchild:
                if node_for_delete.data < parent.data:
                    parent.leftchild = node_for_delete.rightchild
                elif node_for_delete.data > parent.data:
                    parent.rightchild = node_for_delete.rightchild
                return self.root


            elif node_for_delete.leftchild and node_for_delete.rightchild:
                if node_for_delete.data > self.root.data:
                    right_child = node_for_delete.rightchild
                    left_child = node_for_delete.leftchild
                    parent.rightchild = left_child
                    parent.rightchild.rightchild = right_child


                elif node_for_delete.data < parent.data:
                    sub_left_tree = Tree(self.root.leftchild)
                    max_left_child_node = sub_left_tree.max_node()
                    parent_max_node = self.search_parent_node(max_left_child_node.data)
                    left_child = node_for_delete.leftchild
                    right_child = node_for_delete.rightchild
                    parent.leftchild = max_left_child_node
                    parent.leftchild.leftchild = left_child
                    parent_max_node.rightchild = None

                return self.root
