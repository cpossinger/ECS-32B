from hw07 import *

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

    root = BinaryTreeNode(int(data[0]))
    i = 1
    nodes = [root]
    while nodes:
        next_nodes = []
        j = 0
        while (j < len(nodes)) and (i < len(data)):
            if data[i] != "n":
                l = BinaryTreeNode(int(data[i]))
                nodes[j].left = l
                next_nodes.append(l)
            i += 1
            if i < len(data):
                if data[i] != "n":
                    r = BinaryTreeNode(int(data[i]))
                    nodes[j].right = r
                    next_nodes.append(r)
                i += 1
                j += 1
        nodes = next_nodes
    return root


def check(val, expected):
    if val == expected:
        print("Passed.")
    else:
        print("Failed.")
        print("Your output:", val)
        print("Expected output:", expected)


class TestConvertBSTtoGST:
    def test2(self):
        print('convertBSTtoGST case 2: ["3"] (2 point):')
        root = BinaryTreeNode(3)
        val = serialize(convertBSTtoGST(root))
        check(val, ["3"])

    def test4(self):
        print('convertBSTtoGST case 4: ["5","n","6"] (2 point):')
        root = deserialize(["5","n","6"])
        val = serialize(convertBSTtoGST(root))
        check(val, ["11","n","6"])

    def test6(self):
        print('convertBSTtoGST case 6: ["4","1","6","0","2","5","7","n","n","n","3","n","n","n","8"](2 point):')
        root = deserialize(["4","1","6","0","2","5","7","n","n","n","3","n","n","n","8"])
        val = serialize(convertBSTtoGST(root))
        expected = ["30","36","21","36","35","26","15","n","n","n","33","n","n","n","8"]
        check(val, expected)

    def test8(self):
        print('convertBSTtoGST case 8: ["1","n","2","n","3","n","4","n","5"] (2 point):')
        root = deserialize(["1","n","2","n","3","n","4","n","5"])
        val = serialize(convertBSTtoGST(root))
        expected = ["15","n","14","n","12","n","9","n","5"]
        check(val, expected)

    def test10(self):
        print('convertBSTtoGST case 10: ["5","2","n","1","3","0"] (2 point):')
        root = deserialize(["5","2","n","1","3","0"])
        val = serialize(convertBSTtoGST(root))
        expected = ["5","10","n","11","8","11"]
        check(val, expected)

    def test12(self):
        print('convertBSTtoGST case 12: ["10","4","15","1","5","11","17"] (2 point):')
        root = deserialize(["10","4","15","1","5","11","17"])
        val = serialize(convertBSTtoGST(root))
        expected = ["53","62","32","63","58","43","17"]
        check(val, expected)

test = TestConvertBSTtoGST()
test.test2()
test.test4()
test.test6()
test.test8()
test.test10()
test.test12()
