

# list
#         0       1       2         3
names = ["ram","rakesh","satish","sachin"]
print(names)
print(type(names))


# program 2 
print(names[0])
print(names[2])
print(names[3])

#program 3 -- total number elements in list
q1 = len(names)
print(q1)

#program 4
#           0         1        2       3
fruits = ["grapes","mango","papaya","orange"]
fruits[0] = "apple"
print(fruits)

#program 5
vegetables = ["carrot","brinjal","tomato","cauliflower"]
print("Tomato" in vegetables)

# program 6
#          0 1   2   3     4    5 
numbers = [1,22,333,4444,55555,666666]
#         -6 -5 -4  -3    -2    -1

print(numbers[0])
print(numbers[-1])
print(numbers[-3])

#listName[startIndex:endIndex(not included):step]
s = numbers[1::]
print(s)
print(numbers[1:4])
print(numbers[1:5:1])
print(numbers[0:len(numbers):2])

# len(numbers) - 1 is always a last index

# program 7
#              0         1          2        3
countries = ["india","pakistan","srilanka","japan"]
print(len(countries)-1) 


# program 8
#            0       1        2      3
animals = ["tiger","lion","rabbit","cat"]
print(animals)
print(len(animals))
print(animals[3])

for x in range(4):
    print(x)
    print(animals[x])

# x = 0
# x = 1
# x = 2
# x = 4

for item in animals:
    print(item)



# program 9
#        0   1 2  3  4 
marks = [11,22,33,44,55]

for c in range(len(marks)):
    #print(c)
    print(marks[c])


n = [11222,33333,44444,55555]
for item in range(len(n)):
    print(n[item])


for item in n:
    print(item)





