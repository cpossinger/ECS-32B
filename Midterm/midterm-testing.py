from midterm import merge,mergeHelper,UnorderedList,Node

def myTransform(lst):
    result = []
    cur = lst.head
    while cur:
        result.append(cur.getData())
        cur = cur.getNext()
    return result

class TestMerge:
    def test1(self):
        print("merge test case 1 (1 point)")
        l1 = UnorderedList()
        l2 = UnorderedList()
        val = myTransform(merge(l1, l2))
        if val == []:
            print("Passed")
        else:
            print("Failed")
            print("Output =", val)
            print("Expected =", [])
        print()

    def test3(self):
        print("merge test case 3 (1 point)")
        l1 = UnorderedList()
        l1.add(1)

        l2 = UnorderedList()

        val = myTransform(merge(l2, l1))
        if val == [1]:
            print("Passed")
        else:
            print("Failed")
            print("Output =", val)
            print("Expected =", [1])
        print()

    def test5(self):
        print("merge test case 5 (1 point)")
        l1 = UnorderedList()
        l1.add(2)
        l1.add(1)

        l2 = UnorderedList()

        val = myTransform(merge(l2, l1))
        if val == [1,2]:
            print("Passed")
        else:
            print("Failed")
            print("Output =", val)
            print("Expected =", [1, 2])
        print()

    def test7(self):
        print("merge test case 7 (1 point)")
        l1 = UnorderedList()
        l1.add(4)
        l1.add(3)

        l2 = UnorderedList()
        l2.add(2)
        l2.add(1)
        val = myTransform(merge(l2, l1))
        if val == [1, 2, 3, 4]:
            print("Passed")
        else:
            print("Failed")
            print("Output =", val)
            print("Expected =", [1, 2, 3, 4])
        print()

    def test9(self):
        print("merge test case 9 (1 point)")
        l1 = UnorderedList()
        l1.add(5)
        l1.add(5)
        l1.add(2)

        l2 = UnorderedList()
        l2.add(4)
        l2.add(3)
        l2.add(2)
        val = myTransform(merge(l2, l1))
        if val == [2, 2, 3, 4, 5, 5]:
            print("Passed")
        else:
            print("Failed")
            print("Output =", val)
            print("Expected =", [2, 2, 3, 4, 5, 5])
        print()

    def test11(self):
        print("merge test case 11 (1 point)")
        l1 = UnorderedList()
        l1.add(10)
        l1.add(2)
        l1.add(1)

        l2 = UnorderedList()
        l2.add(25)
        l2.add(25)
        l2.add(20)
        l2.add(10)
        l2.add(2)
        l2.add(1)
        val = myTransform(merge(l2, l1))
        if val == [1, 1, 2, 2, 10, 10, 20, 25, 25]:
            print("Passed")
        else:
            print("Failed")
            print("Output =", val)
            print("Expected =", [1, 1, 2, 2, 10, 10, 20, 25, 25])
        print()

    def test13(self):
        print("merge test case 13 (1 point)")
        l1 = UnorderedList()
        l1.add(15)
        l1.add(10)
        l1.add(5)

        l2 = UnorderedList()
        l2.add(20)
        l2.add(3)
        l2.add(2)
        l2.add(-3)
        val = myTransform(merge(l2, l1))
        if val == [-3, 2, 3, 5, 10, 15, 20]:
            print("Passed")
        else:
            print("Failed")
            print("Output =", val)
            print("Expected =", [-3, 2, 3, 5, 10, 15, 20])
        print()

    def test15(self):
        print("merge test case 15 (1 point)")
        l1 = UnorderedList()
        l1.add(5)
        l1.add(5)
        l1.add(5)

        l2 = UnorderedList()
        l2.add(20)
        l2.add(20)
        l2.add(20)
        l2.add(20)
        l2.add(20)
        l2.add(20)
        val = myTransform(merge(l1, l2))
        if val == [5, 5, 5, 20, 20, 20, 20, 20, 20]:
            print("Passed")
        else:
            print("Failed")
            print("Output =", val)
            print("Expected =", [5, 5, 5, 20, 20, 20, 20, 20, 20])
        print()

    def test17(self):
        print("merge test case 17 (1 point)")
        l1 = UnorderedList()
        l1.add(9)
        l1.add(7)
        l1.add(5)
        l1.add(3)
        l1.add(1)

        l2 = UnorderedList()
        l2.add(12)
        l2.add(10)
        l2.add(8)
        l2.add(6)
        l2.add(4)
        l2.add(2)
        val = myTransform(merge(l1, l2))
        if val == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]:
            print("Passed")
        else:
            print("Failed")
            print("Output =", val)
            print("Expected =", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
        print()

    def test19(self):
        print("merge test case 19 (1 point)")
        l1 = UnorderedList()
        l1.add(13)
        l1.add(11)
        l1.add(9)
        l1.add(7)
        l1.add(5)
        l1.add(3)
        l1.add(1)

        l2 = UnorderedList()
        l2.add(10)
        l2.add(8)
        l2.add(6)
        l2.add(4)
        l2.add(2)
        val = myTransform(merge(l1, l2))
        if val == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]:
            print("Passed")
        else:
            print("Failed")
            print("Output =", val)
            print("Expected =", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13])
        print()

test = TestMerge()
test.test1()
test.test3()
test.test5()
test.test7()
test.test9()
test.test11()
test.test13()
test.test15()
test.test17()
test.test19()
