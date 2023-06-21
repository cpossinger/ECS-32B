from hw02 import Solution     # or from hw02-framework import Solution
                              # if you haven't changed the file name yet



# set up
sol = Solution()

# test cases for postfixEval
def testPostfixEval():
    print("--- Testing postfixEval ---")

    test1 = ["2", "4", "7", "*", "-"]
    print("Test 1:", sol.postfixEval(test1) == -26)

    test2 = ['7','8','+','3','2','+','/']
    print("Test2:",sol.postfixEval(test2)==3)

    test3 = ['17','10','+','3','*','9','/']
    print("Test3:",sol.postfixEval(test3)==9)

    test4 = ['5','3','+','6','2','/','*','3','5','*','+']
    print("Test4:",sol.postfixEval(test4)==39)

    test5 = ['4','5','6','*','+']
    print("Test5:",sol.postfixEval(test5)==34)

    test6 = ['6','2','/','1','2','+','*']
    print("Test6:",sol.postfixEval(test6)==9)

    test7 = ['46','8','4','*','2','/','+']
    print("Test7:",sol.postfixEval(test7)==62)

    test8 = ['2.3','3.5','4','+','8','+','-']
    print("Test8:",sol.postfixEval(test8)==-13.2)

    test9 = ['1.2','2.4','/','2.3','*']
    print("Test9:",sol.postfixEval(test9)==1.15)

    test10 = ['1.1','3.3','+','2.2','/','4','*']
    print("Test10:",sol.postfixEval(test10)==8)

    test11 = ['1.1']
    print("Test11:",sol.postfixEval(test11)==1.1)
    print(sol.postfixEval(test11))

    test12 = ['10']
    print("Test12:",sol.postfixEval(test12)==10)
    print(sol.postfixEval(test12))
    # add as many test cases as you want

    print("--- Finished postfixEval ---\n")



# test cases for validParentheses
def testValidParentheses():
    print("--- Testing validParentheses ---")

    test1 = "({})[]"
    print("Test 1:", sol.validParentheses(test1) == True)

    test2 = "(ab){[]}"
    print("Test 2:", sol.validParentheses(test2) == True)

    test3 = "}{"
    print("Test 3:", sol.validParentheses(test3) == False)

    test4 = "ababcd()()((((())))"
    print("Test 4:", sol.validParentheses(test3) == False)

    test5 = ""
    print("Test 5:", sol.validParentheses(test5) == True)

    
    test6 = "{({([abc][def])}())}"
    print("Test 6:", sol.validParentheses(test6) == True)
    
    test7 = "[{()]ab"
    print("Test 7:", sol.validParentheses(test7) == False)

    test8 = "ab"
    print("Test 8:", sol.validParentheses(test8) == True)

    test9 = "a()b[cd()]"
    print("Test 9:", sol.validParentheses(test9) == True)

    test10 = "]"
    print("Test 10:", sol.validParentheses(test10) == False)

    test11 = "["
    print("Test 11:", sol.validParentheses(test11) == False)

    test12 = "a"
    print("Test 12:", sol.validParentheses(test12) == True)
    # add as many test cases as you want


    print("--- Finished validParentheses---\n")



# test cases for reverseString 
def testReverseString():
    print("--- Testing reverseString ---")

    test1 = "abcde"
    print("Test 1:", sol.reverseString(test1) == "edcba")

    test2 = ""
    print("Test 2:", sol.reverseString(test2) == "")
    
    test3 = "xyz"
    print("Test 3:", sol.reverseString(test3) == "zyx")

    test4 = "!@#$%"
    print("Test 4:", sol.reverseString(test4) == "%$#@!")

    test5 = "qwertyytrewq"
    print("Test 5:", sol.reverseString(test5) == "qwertyytrewq")
    
    test6 = "a(){b"
    print("Test 6:", sol.reverseString(test6) == "b{)(a")

    test7 = " "
    print("Test 7:", sol.reverseString(test7) == " ")
    
    # add as many test cases as you want

    print("--- Finished reverseString---\n")

# Run the tests
testPostfixEval()
testValidParentheses()
testReverseString()
