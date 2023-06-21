from hw07 import *

def check(val, expected):
    if val == expected:
        print("Passed.")
    else:
        print("Failed.")
        print("Your output:", val)
        print("Expected output:", expected)


class TestAllPaths:
    
    def test1(self):
        print('allPaths case 1: [("a","b"), ("a","c"), ("b","d"), ("c","d")] (5 point):')
        edges = [("a","b"), ("a","c"), ("b","d"), ("c","d")]
        source = "a"
        destination = "d"
        val = sorted(allPaths(edges, source, destination))
        expected = sorted([["a","b","d"], ["a","c","d"]])
        check(val, expected)

    
    def test3(self):
        print('allPaths case 3: [("a","b"), ("a","c"), ("a","d"), ("b","d"), ("b","e"), ("b","c"), ("d","c"), ("e","d")] (5 point):')
        edges = [("a","b"), ("a","c"), ("a","d"), ("b","d"), ("b","e"), ("b","c"), ("d","c"), ("e","d")]
        source = "a"
        destination = "c"
        val = sorted(allPaths(edges, source, destination))
        expected = sorted([["a","c"], ["a","b","c"], ["a","b","d","c"], ["a","b","e","d","c"], ["a","d","c"]])
        check(val, expected)

    
    def test5(self):
        print('allPaths case 5 (5 point):')
        edges = [("a","b"), ("a","c"), ("a","d"), ("b","d"), ("b","e"), ("b","c"), ("c","d"), ("e","d")]
        source = "a"
        destination = "d"
        val = sorted(allPaths(edges, source, destination))
        expected = sorted([["a","d"], ["a","b","d"], ["a","b","e","d"], ["a","b","c","d"], ["a","c","d"]])
        check(val, expected)

test = TestAllPaths()
test.test1()
test.test3()
test.test5()























