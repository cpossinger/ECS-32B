from hw05 import *

class TestLinearSearchValueIndexEqual:
    def test1(self):
        print("linearSearchValueIndexEqual case 1: plist = [] (1 point):")
        l = []
        val = linearSearchValueIndexEqual(l)
        if val == []:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str([]) + ".")
        print()

    def test3(self):
        print("linearSearchValueIndexEqual case 3: plist = [10] (2 point):")
        l = [10]
        val = linearSearchValueIndexEqual(l)
        if val == []:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str([]) + ".")
        print()

    def test5(self):
        print("linearSearchValueIndexEqual case 5: plist = [1, 2, 3, 4, 5] (2 point):")
        l = [1, 2, 3, 4, 5]
        val = linearSearchValueIndexEqual(l)
        if val == []:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str([]) + ".")
        print()

    def test7(self):
        print("linearSearchValueIndexEqual case 7: plist = [-10, -5, 0, 3, 7] (2 point):")
        l = [-10, -5, 0, 3, 7]
        val = linearSearchValueIndexEqual(l)
        if val == [3]:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str([3]) + ".")
        print()

    def test9(self):
        print("linearSearchValueIndexEqual case 9: plist = [-5, 1, 2, 3] (2 point):")
        l = [-5, 1, 2, 3]
        val = linearSearchValueIndexEqual(l)
        if sorted(val) == [1, 2, 3]:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str([1, 2, 3]) + ".")
        print()

    def test11(self):
        print("linearSearchValueIndexEqual case 11: plist = [0, 1, 2, 5, 6, 7] (2 point):")
        l = [0, 1, 2, 5, 6, 7]
        val = linearSearchValueIndexEqual(l)
        if sorted(val) == [0, 1, 2]:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str([0, 1, 2]) + ".")
        print()

    def test13(self):
        print("linearSearchValueIndexEqual case 13: plist = [-20, -10, 0, 1, 2, 5, 6, 7] (2 point):")
        l = [-20, -10, 0, 1, 2, 5, 6, 7]
        val = linearSearchValueIndexEqual(l)
        if sorted(val) == [5, 6, 7]:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str([5, 6, 7]) + ".")
        print()


t = TestLinearSearchValueIndexEqual()
t.test1()
t.test3()
t.test5()
t.test7()
t.test9()
t.test11()
t.test13()
