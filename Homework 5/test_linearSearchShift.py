from hw05 import *

class TestLinearSearchShift:
    def test1(self):
        print("linearSearchShift case 1: plist = [] (1 point):")
        l = []
        val = linearSearchShift(l)
        if val == 0:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str(0) + ".")
        print()

    def test3(self):
        print("linearSearchShift case 3: plist = [5, 10] (2 point):")
        l = [5, 10]
        val = linearSearchShift(l)
        if val == 0:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str(0) + ".")
        print()

    def test5(self):
        print("linearSearchShift case 5: plist = [2, 3, 4, 5, 0, 1] (2 point):")
        l = [2, 3, 4, 5, 0, 1]
        val = linearSearchShift(l)
        if val == 4:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str(4) + ".")
        print()

    def test7(self):
        print("linearSearchShift case 7: plist = [4, 5, 0, 1, 2, 3] (2 point):")
        l = [4, 5, 0, 1, 2, 3]
        val = linearSearchShift(l)
        if val == 2:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str(2) + ".")
        print()

    def test9(self):
        print("linearSearchShift case 9: plist = [-11, -6, -3, 2, 5, 7, 9, 13] (2 point):")
        l = [-11, -6, -3, 2, 5, 7, 9, 13]
        val = linearSearchShift(l)
        if val == 0:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str(0) + ".")
        print()

    def test11(self):
        print("linearSearchShift case 11: plist = [2, 3, 7, 9, 13, -20, -6, -3] (2 point):")
        l = [2, 3, 7, 9, 13, -20, -6, -3]
        val = linearSearchShift(l)
        if val == 5:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str(5) + ".")
        print()

    def test13(self):
        print("linearSearchShift case 13: plist = [-10, -20] (2 point):")
        l = [-10, -20]
        val = linearSearchShift(l)
        if val == 1:
            print("Passed")
        else:
            print("Failed")
            print("Your output = " + str(val) + ".")
            print("Expected output = " + str(1) + ".")
        print()


t = TestLinearSearchShift()
t.test1()
t.test3()
t.test5()
t.test7()
t.test9()
t.test11()
t.test13()
