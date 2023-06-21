import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from csv import *
from part2Task2 import *

def setupMap(map_file):
    map = []
    with open(map_file) as csvfile:
        r = reader(csvfile, delimiter=',')
        for row in r:
            map.append((row[0], row[1], int(row[2])))
    return map


def setupPackages(pk_file):
    packages = []
    with open(pk_file) as csvfile:
        r = reader(csvfile, delimiter=',')
        for row in r:
            pk = Package(row[0])
            pk.office = row[1]
            pk.address = row[2]
            packages.append(pk)
    return packages


def isEdge(map, u, v):
    for edge in map:
        if edge[0] == u and edge[1] == v:
            return True
        if edge[0] == v and edge[1] == u:
            return True
    return False


m = setupMap("/autograder/source/tests/map4.txt")



class TestMap4Packages4(unittest.TestCase):
    @weight(1)
    def test1(self):
        """map4_packages4 test 1 (1 point)"""
        packages = setupPackages("/autograder/source/tests/packages4.txt")
        truck = Truck("truck", 5, "UPS1")

        deliveryService(m, truck, packages)
        val = len(truck.packages)      # if the truck is empty
        expected = 0
        self.assertEqual(val, expected)

    @weight(1)
    def test2(self):
        """map4_packages4 test 2 (1 point)"""
        packages = setupPackages("/autograder/source/tests/packages4.txt")
        truck = Truck("truck", 5, "UPS1")
        deliveryService(m, truck, packages)
        val = True     # if every package is delivered
        for pk in packages:
            if pk.delivered == False:
                val = False
                break
        expected = True
        self.assertEqual(val, expected)

    @weight(1)
    def test3(self):
        """map4_packages4 test 3 (1 point)"""
        packages = setupPackages("/autograder/source/tests/packages4.txt")
        truck = Truck("truck", 5, "UPS1")
        deliveryService(m, truck, packages)
        val = True     # if every package is collected
        for pk in packages:
            if pk.collected == False:
                val = False
                break
        expected = True
        self.assertEqual(val, expected)

    @weight(1)
    def test4(self):
        """map4_packages4 test 4 (1 point)"""
        packages = setupPackages("/autograder/source/tests/packages4.txt")
        truck = Truck("truck", 5, "UPS1")
        (deliveredTo, _) = deliveryService(m, truck, packages)
        val = True     # if every package is delivered to its correct address
        for pk in packages:
            if pk.address != deliveredTo[pk.id]:
                val = False
                break
        expected = True
        self.assertEqual(val, expected)

    @weight(1)
    def test5(self):
        """map4_packages4 test 5 (1 point)"""
        packages = setupPackages("/autograder/source/tests/packages4.txt")
        truck = Truck("truck", 5, "UPS1")
        (_, stops) = deliveryService(m, truck, packages)
        val = True     # if there is an edge between stops[i] and stops[i+1]
        for i in range(1, len(stops)):
            if not isEdge(m, stops[i-1], stops[i]):
                val = False
                break
        expected = True
        self.assertEqual(val, expected)


    @weight(0)
    def test5(self):
        """map4_packages4 multiple runs to average the running time (not graded)"""
        packages = setupPackages("/autograder/source/tests/packages4.txt")
        truck = Truck("truck", 5, "UPS1")
        (deliveredTo, _) = deliveryService(m, truck, packages)
        packages = setupPackages("/autograder/source/tests/packages4.txt")
        truck = Truck("truck", 20, "UPS2")
        (deliveredTo, _) = deliveryService(m, truck, packages)
        packages = setupPackages("/autograder/source/tests/packages4.txt")
        truck = Truck("truck", 3, "UPS1")
        (deliveredTo, _) = deliveryService(m, truck, packages)
        packages = setupPackages("/autograder/source/tests/packages4.txt")
        truck = Truck("truck", 100, "UPS2")
        (deliveredTo, _) = deliveryService(m, truck, packages)
        packages = setupPackages("/autograder/source/tests/packages4.txt")
        truck = Truck("truck", 50, "UPS2")
        (deliveredTo, _) = deliveryService(m, truck, packages)
        val = True
        expected = True
        self.assertEqual(val, expected)
