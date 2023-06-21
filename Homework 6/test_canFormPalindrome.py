from hw06 import *

def check(val, expected):
    if val == expected:
        print("Passed")
    else:
        print("Failed")
        print("Your output =", val)
        print("Expected output =", expected)



class TestCanFormPalindrome:
    
    def test2(self):
        print("canFormPalindrome case 2: s = 'x' (2 point):")
        l = "x"
        val = canFormPalindrome(l)
        check(val, True)
    
    def test4(self):
        print("canFormPalindrome case 4: s = 'xzz' (2 point):")
        l = "xzz"
        val = canFormPalindrome(l)
        check(val, True)
    
    def test6(self):
        print("canFormPalindrome case 6: s = 'abxzzbbx' (2 point):")
        l = "abxzzbbx"
        val = canFormPalindrome(l)
        check(val, False)
    
    def test8(self):
        print("canFormPalindrome case 8: s = 'axzzbbxa' (2 point):")
        l = "axzzbbxa"
        val = canFormPalindrome(l)
        check(val, True)

    
    def test10(self):
        print("canFormPalindrome case 10: s = 'aaabacaaadacabaaaaaaaaaadadaaaadaaaeaaaaaaaaaaa' (2 point):")
        l = "aaabacaaadacabaaaaaaaaaadadaaaadaaaeaaaaaaaaaaa"
        val = canFormPalindrome(l)
        check(val, True)

test = TestCanFormPalindrome()
test.test2()
test.test4()
test.test6()
test.test8()
test.test10()
