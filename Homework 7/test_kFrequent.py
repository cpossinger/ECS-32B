from hw07 import *

def check(val, expected):
    if val == expected:
        print("Passed.")
    else:
        print("Failed.")
        print("Your output:", val)
        print("Expected output:", expected)



class TestKFrequent:
    def test2(self):
        print("Frequent case 2: nums = [], k = 3 (2 point):")
        nums = []
        k = 3
        val = sorted(kFrequent(nums, k))
        expected = []
        check(val, expected)

    def test4(self):
        print("Frequent case 4: nums = [9,9,10,6,9,5,7,7,5,8,10,10,9,3,2], k = 1 (2 point):")
        nums = [9, 9, 10, 6, 9, 5, 7, 7, 5, 8, 10, 10, 9, 3, 2]
        k = 1
        val = sorted(kFrequent(nums, k))
        expected = [9]
        check(val, expected)

    def test6(self):
        print("Frequent case 6: nums = [9, 9, 10, 6, 9, 5, 7, 7, 5, 8, 10, 10, 9, 3, 2], k = 3 (2 point):")
        nums = [9, 9, 10, 6, 9, 5, 7, 7, 5, 8, 10, 10, 9, 3, 2]
        k = 3
        val = sorted(kFrequent(nums, k))
        expected = [5, 9, 10]
        check(val, expected)

    def test8(self):
        print("Frequent case 8: nums = [9, 9, 10, 6, 9, 5, 7, 7, 5, 8, 10, 10, 9, 3, 2], k = 5(2 point):")
        nums = [9, 9, 10, 6, 9, 5, 7, 7, 5, 8, 10, 10, 9, 3, 2]
        k = 5
        val = sorted(kFrequent(nums, k))
        expected = [2, 5, 7, 9, 10]
        check(val, expected)

test = TestKFrequent()
test.test2()
test.test4()
test.test6()
test.test8()























