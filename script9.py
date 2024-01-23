
#        0   1  2  3
listA = [11,22,33,44]
print(listA[0])
listA[0] = 33
print(listA)

# Methods
names = ["chinmay","sarika","poorva","mayuri"]
names.append("ajay")
print(names)

names.insert(2,"amol")
print(names)

names.pop()
print(names)

names.pop(2)
print(names)

# append() , pop() ,insert()
#          0         1        2       3
fruits = ["apple","mango","banana","orange"]
#fruits.remove("apple")
print(fruits)

q1 = fruits.index("apple")
print(q1)


fruits.extend(["chikoo","grapes"])
print(fruits)

listA = [11,22,33]
listB = [44,55,66]

listB.extend(listA)
print(listA)
print(listB)

animals = ["tiger","lion","rabbit"]
#animals.clear()
print(animals)

animals.sort()
print(animals)

animals.reverse()
print(animals)




listC = [11,22,33]
listD = listC

listD[0] = 44
print(listC)
print(listD)



listH = [11,22,33]
listN = listH

listN[0] = 999

print(listH)
print(listN)


city = ["pune","mumbai","nagpur"]
city2 = city.copy()
city[1] = "surat"
print(city)
print(city2)


























