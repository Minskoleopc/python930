# # list 
# #          0       1        2     3
# names = ["amol","sarika","amit","raj"]
# print(names[0])

# names[0] = "poorva"
# print(names)

# #          0       1       2      3
# names = ["amol","sarika","amit","raj"]
# #         -4      -3       -2      -1
# #listName[startIndex,endIndex(not included),Steps]
# print(names[1::])
# print(names[1:3:])
# print(names[1:len(names)])

# #          0   1   2    3    4    5
# numbers = [11,222,333,4444,55555,666666]
# #          -6  -5 -4   -3   -2     -1
# print(numbers)
# print(numbers[0:len(numbers):2])
# print(numbers[::-1])
# print(numbers[4:2:-1])

# #           0        1       2        3       4
# fruits = ["apple","mango","banana","grapes","papaya"]
# for x in range(len(fruits)):
#     print(x)
#     print(fruits[x])


# for item in fruits:
#     print(item)


# print("apple" in fruits)

#           0          1      2       3
names = ["chinmay","sarika","sachin","amol"]

names.append("poorva")
print(names)

names.insert(2,"akash")
print(names)

names.pop()
print(names)

names.pop(2)
print(names)

names.remove("sarika")
print(names)


animals = ["tiger","lion","snake","rabbit","tiger"]
e = animals.count("tiger")
print(e)

# animals.clear()
# print(animals)

f = animals.index("lion")
print(f)

animals.extend(["bear","frog"])
print(animals)

animals.sort()
print(animals)

animals.reverse()
print(animals)


# cities = ["pune","bangalore","kolkata"]
# cities2 = cities
# cities2[0] = "wardha"
# print(cities)
# print(cities2)

cities = ["pune","bangalore","kolkata"]
cities2 = cities.copy() # another memory will be created
cities2[0] = "wardha"
print(cities)
print(cities2)