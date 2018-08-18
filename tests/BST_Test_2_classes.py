import BST_Two_Classes


def test_empty_tree():
    tree = BST_Two_Classes.Tree()
    assert tree.root == None


def test_add_node_to_the_empty_tree():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(22)
    assert tree.root.data == 22


def test_insert_right_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(50)
    assert tree.root.rightchild.data == 50



def test_insert_left_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(40)
    tree.insert_node(23)
    assert tree.root.leftchild.data == 23


def test_insert_two_left_children():
    tree = BST_Two_Classes.Tree() #create empty tree
    tree.insert_node(40)
    tree.insert_node(23)
    tree.insert_node(10)
    assert tree.root.leftchild.data == 23
    assert tree.root.leftchild.leftchild.data == 10


def test_insert_left_child_and_right_child_to_leftchild():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(40)
    tree.insert_node(23)
    tree.insert_node(10)
    tree.insert_node(30)
    assert tree.root.leftchild.data == 23
    assert tree.root.leftchild.leftchild.data == 10
    assert tree.root.leftchild.rightchild.data == 30


def test_insert_right_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(40) #create root
    tree.insert_node(50)
    tree.insert_node(70)
    assert tree.root.rightchild.data == 50
    assert tree.root.rightchild.rightchild.data == 70


def test_insert_right_child_and_left_child_to_rightchild():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(40)
    tree.insert_node(50)
    tree.insert_node(70)
    tree.insert_node(45)
    assert tree.root.rightchild.data == 50
    assert tree.root.rightchild.rightchild.data == 70
    assert tree.root.rightchild.leftchild.data == 45

def test_node_not_found():
    tree = BST_Two_Classes.Tree()
    assert not tree.search_node_value(22)


def test_search_leftchild_node():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(22)
    tree.insert_node(18)
    assert tree.search_node_value(18)

def test_search_rightchild_node():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(22)
    tree.insert_node(25)
    assert tree.search_node_value(25)
    assert not tree.search_node_value(26)


def test_search_diffrent_nodes_in_tree():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(20)
    tree.insert_node(40)
    tree.insert_node(15)
    tree.insert_node(7)
    tree.insert_node(17)
    tree.insert_node(25)
    tree.insert_node(21)
    tree.insert_node(27)
    tree.insert_node(50)
    tree.insert_node(55)
    tree.insert_node(45)
    assert tree.search_node_value(20)
    assert tree.search_node_value(15)
    assert tree.search_node_value(27)
    assert tree.search_node_value(45)
    assert tree.search_node_value(55)

""" #Failed with excepltion
def test_duplicate_insert():# HOW I CAN KNOW THAT TREE HAVE BOTH VALUE OT JUST FIRST ONE?????
    tree = BST_Two_Classes.Tree()
    node1 = tree.insert_node(30)
    node2 = tree.insert_node(30)
    assert tree.search_node_value(30)

"""


def test_min_node():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(20)
    tree.insert_node(40)
    tree.insert_node(15)
    tree.insert_node(7)
    min_node = tree.min_node()
    assert tree.root.leftchild.leftchild.leftchild == min_node



def test_min_node_in_tree_with_right_child_when_rightchild_have_lefttchild():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(20)
    tree.insert_node(40)
    tree.insert_node(30)
    min_node = tree.min_node()
    assert tree.root == min_node


def test_max_node():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(20)
    tree.insert_node(40)
    tree.insert_node(50)
    tree.insert_node(57)
    max_node = tree.max_node()
    assert tree.root.rightchild.rightchild.rightchild == max_node




def test_delete_root_wo_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(22)
    tree.delete_node(22)
    assert tree.root is None
    assert not tree.search_node_value(22)


def test_delete_root_with_left_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(22)
    tree.insert_node(20)
    root = tree.delete_node(22)
    assert not tree.search_node_value(22)
    assert root.data == 20


def test_delete_root_with_left_child_when_leftchild_have_leftchild():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(22)
    tree.insert_node(20)
    tree.insert_node(10)
    tree.delete_node(22)
    assert not tree.search_node_value(22)
    assert tree.search_node_value(20)
    assert tree.root.data == 20
    assert tree.root.leftchild.data == 10
    assert tree.root.leftchild.leftchild is None



def test_delete_root_with_right_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.delete_node(25)
    assert not tree.search_node_value(25)
    assert tree.search_node_value(30)
    assert tree.root.data == 30


def test_delete_root_with_right_child_when_righchild_have_rightchild():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(22)
    tree.insert_node(30)
    tree.insert_node(40)
    tree.delete_node(22)
    assert not tree.search_node_value(22)
    assert tree.search_node_value(30)
    assert tree.root.data == 30
    assert tree.root.rightchild.data == 40
    assert tree.root.rightchild.rightchild is None


def test_delete_root_with_both_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.delete_node(25)
    assert not tree.search_node_value(25)
    assert tree.search_node_value(30)
    assert tree.root.data == 30
    assert tree.root.leftchild.data == 15
    assert tree.root.rightchild is None


def test_delete_root_with_both_children_right_child_have_right_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(40)
    tree.insert_node(15)
    tree.delete_node(25)
    assert not tree.search_node_value(25)
    assert tree.search_node_value(30)
    assert tree.root.data == 30
    assert tree.search_node_value(15)
    assert tree.root.leftchild.data == 15
    assert tree.root.rightchild.data == 40
    assert tree.root.rightchild.rightchild is None


def test_delete_root_with_both_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.delete_node(25)
    assert not tree.search_node_value(25)
    assert tree.search_node_value(15)
    assert tree.search_node_value(30)
    assert tree.root.data == 30
    assert tree.root.leftchild.data == 15
    assert tree.root.rightchild is None


def test_delete_min_left_node_wo_children_from_subleft_tree():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(10)
    tree.delete_node(10)
    assert tree.root.leftchild.leftchild is None
    assert not tree.search_node_value(10)

def test_delete_right_child_wo_children_node_from_left_subtree():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(10)
    tree.insert_node(20)
    tree.insert_node(23)
    tree.delete_node(23)
    assert tree.root.leftchild.rightchild.rightchild is None
    assert not tree.search_node_value(23)


def test_delete_leftchild_wo_children_node_from_subright_tree():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(27)
    tree.delete_node(27)
    assert tree.root.rightchild.leftchild is None
    assert not tree.search_node_value(27)

def test_delete_rightchild_node_from_subright_tree_wo_childrent():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(37)
    tree.insert_node(40)
    tree.delete_node(40)
    assert tree.root.rightchild.rightchild.rightchild is None
    assert not tree.search_node_value(40)


def test_delete_node_with_parent_and_left_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(20)
    tree.insert_node(10)
    tree.delete_node(20)
    assert not tree.search_node_value(20)
    assert tree.root.leftchild.data == 10




def test_delete_node_with_parent_and_left_child_if_leftchild_have_rightchild():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(20)
    tree.insert_node(10)
    tree.insert_node(15)
    tree.delete_node(20)
    assert not tree.search_node_value(20)
    assert tree.root.leftchild.data == 10
    assert tree.root.leftchild.rightchild.data == 15

def test_delete_node_with_parent_and_right_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(40)
    tree.delete_node(30)
    assert not tree.search_node_value(30)
    assert tree.root.rightchild.data == 40

def test_delete_node_with_parent_and_right_child_if_child_have_left_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(40)
    tree.insert_node(35)
    tree.delete_node(30)
    assert not tree.search_node_value(30)
    assert tree.root.rightchild.data == 40
    assert tree.root.rightchild.leftchild.data == 35

def test_delete_node_from_left_subtree_with_parent_and_right_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(20)
    tree.insert_node(23)
    tree.delete_node(20)
    assert tree.root.leftchild.rightchild.data == 23


def test_delete_root_and_replace_with_min_right_node_from_right_subtree():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(27)
    #assert tree.min_node(tree.root.rightchild) == 27
    tree.delete_node(25)
    assert tree.root.data == 27
    assert not tree.search_node_value(25)
    assert tree.root.leftchild.data == 15
    assert tree.root.rightchild.data == 30



def test_delete_root_with_left_child_when_leftchild_have_rightchild():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(20)
    tree.insert_node(22)
    tree.delete_node(30)
    assert not tree.search_node_value(30)
    assert tree.root.data == 22
    assert tree.root.leftchild.rightchild is None
    assert tree.root.leftchild.data == 20


def test_delete_root_with_right_child_when_rightchild_have_lefttchild():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(22)
    tree.insert_node(30)
    tree.insert_node(25)
    tree.delete_node(22)
    assert not tree.search_node_value(22)
    assert tree.root.data == 25
    assert tree.root.rightchild.data == 30
    assert tree.root.rightchild.leftchild is None

def test_delete_root_with_right_child_when_rightchild_have_tree_of_lefttchild():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(40)
    tree.insert_node(60)
    tree.insert_node(80)
    tree.insert_node(55)
    tree.insert_node(57)
    tree.insert_node(50)
    tree.insert_node(45)
    tree.delete_node(40)
    assert tree.root.data == 45
    assert tree.root.rightchild.data == 60
    assert tree.root.rightchild.leftchild.leftchild.leftchild is None


def test_delete_right_node_wo_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.delete_node(30)
    assert tree.root.data == 25
    assert tree.root.rightchild is None


def test_delete_left_node_wo_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.delete_node(15)
    assert tree.root.data == 25
    assert tree.root.leftchild is None

def test_delete_right_node_with_right_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(35)
    tree.delete_node(30)
    assert tree.root.data == 25
    assert tree.root.rightchild.data == 35
    assert tree.root.rightchild.rightchild is None


def test_delete_right_node_with_left_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(27)
    tree.delete_node(30)
    assert tree.root.data == 25
    assert tree.root.rightchild.data == 27
    assert tree.root.rightchild.leftchild is None

def test_delete_right_node_with_both_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(35)
    tree.insert_node(27)
    tree.delete_node(30)
    assert tree.root.data == 25
    assert tree.root.rightchild.data == 27
    assert tree.root.rightchild.rightchild.data == 35
    assert tree.root.rightchild.leftchild is None


def test_delete_left_node_with_left_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(10)
    tree.delete_node(15)
    assert tree.root.data == 25
    assert tree.root.rightchild.data == 30
    assert tree.root.leftchild.data == 10
    assert tree.root.leftchild.leftchild is None


def test_delete_left_node_with_right_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(20)
    tree.delete_node(15)
    assert tree.root.data == 25
    assert tree.root.rightchild.data == 30
    assert tree.root.leftchild.data == 20
    assert tree.root.leftchild.rightchild is None

def test_delete_left_node_with_both_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(10)
    tree.insert_node(20)
    tree.delete_node(15)
    assert tree.root.data == 25
    assert tree.root.leftchild.data == 20
    assert tree.root.leftchild.leftchild.data == 10
    assert tree.root.leftchild.rightchild is None

def test_delete_node_with_both_children_and_replace_with_min_right_node():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(15)
    tree.insert_node(35)
    tree.insert_node(27)
    tree.insert_node(40)
    tree.delete_node(30)
    assert tree.root.data == 25
    assert tree.root.rightchild.data == 27
    assert tree.root.rightchild.leftchild is None
    assert tree.root.rightchild.rightchild.data == 35
    assert tree.root.rightchild.rightchild.rightchild.data == 40


def test_delete_node_with_both_children_and_rightchild_tree():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(100)
    tree.insert_node(50)
    tree.insert_node(150)
    tree.insert_node(130)
    tree.insert_node(120)
    tree.insert_node(160)
    tree.delete_node(150)
    assert tree.root.rightchild.data == 130


def test_found_parent_for_empty_tree():
    tree = BST_Two_Classes.Tree()
    parent = tree.search_parent_node(None)
    assert parent is None

def test_found_parent_to_root():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    parent = tree.search_parent_node(25)
    assert parent is None


def test_found_parent_to_leftnode_wo_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(20)
    parent = tree.search_parent_node(20)
    assert parent.data == 25


def test_found_parent_to_rightnode_wo_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    parent = tree.search_parent_node(30)
    assert parent.data == 25


def test_found_parent_for_left_left_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(20)
    tree.insert_node(10)
    parent = tree.search_parent_node(10)
    assert parent.data == 20


def test_found_parent_for_right_right_child():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(40)
    parent = tree.search_parent_node(40)
    assert parent.data == 30


def test_found_parent_to_node_with_both_children():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(20)
    parent = tree.search_parent_node(30)
    assert parent.data == 25


def test_found_parent_value_when_node_is_NONE():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    parent = tree.search_parent_node(40)#??????
    assert parent is None


def test_found_parent_to_node_with_both_children_left_side():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(25)
    tree.insert_node(30)
    tree.insert_node(20)
    tree.insert_node(10)
    tree.insert_node(23)
    parent = tree.search_parent_node(10)
    parent1 = tree.search_parent_node(23)
    assert parent.data == 20
    assert parent1.data == 20



def test_inorder_tree_root_only_to_list():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    origin_list = [30]
    list = tree.inorder_traversal(tree.root)
    assert origin_list == list


def test_inorder_tree_root_with_leftchild_to_list():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(10)
    origin_list = [10, 30]
    list = tree.inorder_traversal(tree.root)
    assert origin_list == list


def test_inorder_tree_root_with_leftchild_rightchild_to_list():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(10)
    tree.insert_node(20)
    origin_list = [10,20, 30]
    list = tree.inorder_traversal(tree.root)
    assert  tree.root.leftchild.rightchild.data == 20
    assert origin_list == list



def test_inorder_tree_root_rightchild_to_list():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(40)
    original_tree = [30, 40]
    list = tree.inorder_traversal(tree.root)
    assert original_tree == list


def test_inorder_tree_root_rightchild_rightchild_to_list():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(40)
    tree.insert_node(70)
    original_tree = [30, 40, 70]
    list = tree.inorder_traversal(tree.root)
    assert original_tree == list


def test_inorder_tree_root_rightchild_leftchild_to_list():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(40)
    tree.insert_node(35)
    original_tree = [30, 35, 40]
    list = tree.inorder_traversal(tree.root)
    assert original_tree == list


def test_tree_inorder_root_rightchild_leftchild_full_tree_to_list():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(20)
    tree.insert_node(10)
    tree.insert_node(27)
    tree.insert_node(40)
    tree.insert_node(35)
    tree.insert_node(60)
    tree.insert_node(50)
    original_tree = [10, 20, 27, 30, 35, 40, 50, 60]
    list = tree.inorder_traversal(tree.root)
    assert original_tree == list


def test_tree_preorder_root_rightchild_leftchild_full_tree_to_list():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(20)
    tree.insert_node(10)
    tree.insert_node(27)
    tree.insert_node(40)
    tree.insert_node(35)
    tree.insert_node(60)
    tree.insert_node(50)
    original_tree = [30, 10, 20, 27, 35, 40, 50, 60]
    list = tree.preorder_traversal(tree.root)
    assert original_tree == list


def test_tree_postorder_root_rightchild_leftchild_full_tree_to_list():
    tree = BST_Two_Classes.Tree()
    tree.insert_node(30)
    tree.insert_node(20)
    tree.insert_node(10)
    tree.insert_node(27)
    tree.insert_node(40)
    tree.insert_node(35)
    tree.insert_node(60)
    tree.insert_node(50)
    original_tree = [10, 20, 27, 35, 40, 50, 60, 30]
    list = tree.postorder_traversal(tree.root)
    assert original_tree == list
