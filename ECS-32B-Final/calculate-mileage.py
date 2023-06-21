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


def getWeight(edges, u, v):
    for edge in edges:
        if edge[0] == u and edge[1] == v:
            return edge[2]
        if edge[0] == v and edge[1] == u:
            return edge[2]
    print("Error: City", u, "and City", v, "are not adjacent.")
    return float("inf")


def mileage(map, stops):
    total = 0
    for i in range(1, len(stops)):
        total += getWeight(map, stops[i-1], stops[i])
    return total



mileage_of_all_maps = 0

# test_map1
map1 = setupMap("map1.txt")
packages1 = setupPackages("packages1.txt")
truck = Truck("truck", 5, "UPS")
_, stops = deliveryService(map1, truck, packages1)
current_mileage = mileage(map1, stops)
mileage_of_all_maps += current_mileage
print("Truck's mileage using the setup in test_map1 =", current_mileage)

# test_map1_smallTruck
map1 = setupMap("map1.txt")
packages1 = setupPackages("packages1.txt")
truck = Truck("truck", 3, "UPS")
_, stops = deliveryService(map1, truck, packages1)
current_mileage = mileage(map1, stops)
mileage_of_all_maps += current_mileage
print("Truck's mileage using the setup in test_map1_smallTruck =", current_mileage)

# test_map2
map2 = setupMap("map2.txt")
packages2 = setupPackages("packages2.txt")
truck = Truck("truck", 5, "UPS1")
_, stops = deliveryService(map2, truck, packages2)
current_mileage = mileage(map2, stops)
mileage_of_all_maps += current_mileage
print("Truck's mileage using the setup in test_map2 =", current_mileage)

# test_map3_packages3
map3 = setupMap("map3.txt")
packages3 = setupPackages("packages3.txt")
truck = Truck("truck", 5, "UPS1")
_, stops = deliveryService(map3, truck, packages3)
current_mileage = mileage(map3, stops)
mileage_of_all_maps += current_mileage
print("Truck's mileage using the setup in test_map3_packages3 =", current_mileage)

# test_map3_packages4
map3 = setupMap("map3.txt")
packages4 = setupPackages("packages4.txt")
truck = Truck("truck", 5, "UPS1")
_, stops = deliveryService(map3, truck, packages4)
current_mileage = mileage(map3, stops)
mileage_of_all_maps += current_mileage
print("Truck's mileage using the setup in test_map3_packages4 =", current_mileage)

# test_map4_packages4
map4 = setupMap("map4.txt")
packages4 = setupPackages("packages4.txt")
truck = Truck("truck", 5, "UPS1")
_, stops = deliveryService(map4, truck, packages4)
current_mileage = mileage(map4, stops)
mileage_of_all_maps += current_mileage
print("Truck's mileage using the setup in test_map4_packages4 =", current_mileage)

print()
print("The total mileage of all the maps =", mileage_of_all_maps)























