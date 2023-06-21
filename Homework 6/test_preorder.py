from hw06 import BinaryTreeNode,preorder

def check(val, expected):
    if val == expected:
        print("Passed")
    else:
        print("Failed")
        print("Your output =", val)
        print("Expected output =", expected)


class TestPreorder:
    
    def test1(self):
        print("preorder case 1 (1 point):")
        root = None
        val = preorder(root)
        check(val, [])

    
    def test3(self):
        print("preorder case 3 (1 point):")
        root = BinaryTreeNode(5)
        root.left = BinaryTreeNode(3)
        val = preorder(root)
        check(val, [5,3])

    
    def test4(self):
        print("preorder case 4 (2 point):")
        root = BinaryTreeNode(6)
        root.right = BinaryTreeNode(2)
        val = preorder(root)
        check(val, [6, 2])

    
    def test6(self):
        print("preorder case 6 (2 point):")
        root = BinaryTreeNode(6)
        root.right = BinaryTreeNode(2)
        root.right.left = BinaryTreeNode(3)
        val = preorder(root)
        check(val, [6,2,3])

    def test9(self):
        print("preorder case 9 (2 point):")
        root = BinaryTreeNode(2)
        root.left = BinaryTreeNode(1)
        root.right = BinaryTreeNode(9)
        root.left.right = BinaryTreeNode(5)
        val = preorder(root)
        check(val, [2, 1, 5, 9])


test = TestPreorder()
test.test1()
test.test3()
test.test4()
test.test6()
test.test9()
