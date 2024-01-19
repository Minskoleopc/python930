x = 10 
print(x)
x = 1900
print(x)


# list 
# list stores the value by index
#            0        1       2     3       4
names = ["chinmay","mayuri","ram","sham","satish"]
print(type(names))
print(names[0])

# program 2
cities = ["pune","mumbai","banglore","kolkata"]
marks = [12,33,4,4555,66,6,77]
info = ["chinmay","deshpadne",True,9766909110]

# program 3
#          0        1        2          3
cities = ["pune","mumbai","bangalore","kolkata"]
#          -4      -3        -2          -1
a1 = len(cities)
print(a1)

# retrive the value by index
print(cities[0])
print(cities[-2])

# program 4
#            0         1         2         3      4      5    6
country = ["india","pakistan","srilanka","cuba","china","UK","USA"]
#            -7       -6        -5         -4     -3    -2    -1                     
# listName[startIndex:EndIndex(not included):steps]

print(country[1::])
print(country[4::])
print(country[1:6:])
print(country[1:6:1])
print(country[0:len(country):3])
print(country[6:0:-2])
print(country[0:-1])
print(country[-6:-2])

# program 5
#           0        1       2       3
fruits = ["apple","mango","banana","grapes"]
print(fruits[0])
print("mango" in fruits)

# program 6
# updating element in list
animals  = ["tiger","lion","rabbit"]
animals[0] = "snake"
print(animals)


# program 7
for x in range(5):
    print(x)

#         0  1  2   3    4
marks  = [1,22,333,4444,5555]
print(marks[0])

for x in range(len(marks)):
    #print(x)
    print(marks[x])

# 0 
# 1
# 2
# 3
# 4 
#           0       1        2          3
flowers = ["rose","lotus","jasmine","sunflower"]
for x in range(len(flowers)):
    #print(x)
    print(flowers[x])

for x in flowers:
    print(x)

