from hw07 import *


def check(val, expected):
    if val == expected:
        print("Passed.")
    else:
        print("Failed.")
        print("Your output:", val)
        print("Expected output:", expected)


"""
Encodes a tree to a list of strings
"""
def serialize(root):
    result = []
    nodes = [root]
    
    while nodes:
        next_nodes = []
        for n in nodes:
            if n:
                result.append(str(n.val))
                next_nodes.append(n.left)
                next_nodes.append(n.right)
            else:
                result.append("n")
        nodes = next_nodes
    i = len(result) - 1
    while i >= 0 and result[i] == "n":
        i -= 1
    return result[:i+1]


"""
Decodes your encoded data to tree.
"""
def deserialize(data):
    if (not data) or (data[0] == "n"):
        return None

    root = TreeNode(data[0])
    i = 1
    nodes = [root]
    while nodes:
        next_nodes = []
        j = 0
        while (j < len(nodes)) and (i < len(data)):
            if data[i] != "n":
                l = TreeNode(int(data[i]))
                nodes[j].left = l
                next_nodes.append(l)
            i += 1
            if i < len(data):
                if data[i] != "n":
                    r = TreeNode(int(data[i]))
                    nodes[j].right = r
                    next_nodes.append(r)
                i += 1
                j += 1
        nodes = next_nodes
    return root



class TestReconstructBT:
    def test2(self):
        print("econstructBT case 2: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7](1 point):")
        val = reconstructBT([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        encoded_val = serialize(val)
        check(encoded_val, ["3", "9", "20", "n", "n", "15", "7"])

    def test4(self):
        print("econstructBT case 4: preorder = [5,10], inorder = [10,5] (1 point):")
        val = reconstructBT([5,10], [10,5])
        encoded_val = serialize(val)
        check(encoded_val, ["5","10"])

    def test6(self):
        print("econstructBT case 6: preorder = [7,2,3], inorder = [2,7,3] (1 point):")
        val = reconstructBT([7,2,3], [2,7,3])
        encoded_val = serialize(val)
        check(encoded_val, ["7","2","3"])

    def test8(self):
        print("econstructBT case 8: preorder = [7,2,3], inorder = [2,3,7] (1 point):")
        val = reconstructBT([7,2,3], [2,3,7])
        encoded_val = serialize(val)
        check(encoded_val, ["7","2","n","n","3"])

    def test10(self):
        print("econstructBT case 10: preorder = [7,2,3], inorder = [7,2,3] (1 point):")
        val = reconstructBT([7,2,3], [7,2,3])
        encoded_val = serialize(val)
        check(encoded_val, ["7","n","2","n","3"])

    def test12(self):
        print("econstructBT case 12: preorder = [10,9,5,1], inorder = [5,9,10,1] (1 point):")
        val = reconstructBT([10,9,5,1], [5,9,10,1])
        encoded_val = serialize(val)
        check(encoded_val, ["10","9","1","5"])

    def test20(self):
        print("econstructBT case 20: preorder = [3,5,2,1,10], inorder = [2,5,1,3,10] (1 point):")
        val = reconstructBT([3,5,2,1,10], [2,5,1,3,10])
        encoded_val = serialize(val)
        check(encoded_val, ["3","5","10","2","1"])

    def test24(self):
        print("econstructBT case 24: preorder = [3,5,10,2,1], inorder = [3,10,5,1,2] (1 point):")
        val = reconstructBT([3,5,10,2,1], [3,10,5,1,2])
        encoded_val = serialize(val)
        check(encoded_val, ["3","n","5","10","2","n","n","1"])

test = TestReconstructBT()
test.test2()
test.test4()
test.test6()
test.test8()
test.test12()
test.test10()
test.test20()
test.test24()
