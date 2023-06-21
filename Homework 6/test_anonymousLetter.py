from hw06 import *

def check(val, expected):
    if val == expected:
        print("Passed")
    else:
        print("Failed")
        print("Your output =", val)
        print("Expected output =", expected)

class TestAnonymousLetter:
    def test2(self):
        print("anonymousLetter case 2: book = 'alsfjei', letter = '' (2 point):")
        b = "alsfjei"
        l = ""
        val = anonymousLetter(b, l)
        check(val, True)

    
    def test4(self):
        print("anonymousLetter case 4: book = 'xzz', letter = 'xzz' (2 point):")
        b = "xzz"
        l = "xzz"
        val = anonymousLetter(b, l)
        check(val, True)

    
    def test5(self):
        print("anonymousLetter case 5: book = 'xzz', letter = 'zxzx' (2 point):")
        b = "xzz"
        l = "zxzx"
        val = anonymousLetter(b, l)
        check(val, False)

    
    def test6(self):
        print("anonymousLetter case 6: book = 'febxxzz', letter = 'zxzx' (2 point):")
        b = "febxxzz"
        l = "zxzx"
        val = anonymousLetter(b, l)
        check(val, True)

    
    def test9(self):
        print("anonymousLetter case 9: book = 'abxaxabbz', letter = 'abxzzbbxz' (2 point):")
        b = "abxaxabbz"
        l = "abxzzbbxa"
        val = anonymousLetter(b, l)
        check(val, False)

test = TestAnonymousLetter()
test.test2()
test.test4()
test.test5()
test.test6()
test.test9()
