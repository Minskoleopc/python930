x = 10
print(x)

#     0   1  2  3  4
h  = [22,33,44,55,66]
print(h)
print(type(h))
print(h[0])
print(h[3])

# program 2
#           0         1         2      3
names = ["chinmay","sarika","poorva","sham"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])


# program 3
# using range 
for x in range(len(names)):
    print(names[x])

#         0       1         2       3
city = ["pune","mumbai","nagpur","kolkata"]
print(city)
q1 = len(city)
print(q1)
print(q1 - 1) # always lastIndex

for x in range(q1):
    print(city[x])

# program 5
# without range 
#           0        1        2      3    
fruits = ["apple","mango","banana","grapes"]
for item in fruits:
    print(item)

# program 6
veg = ["brinjal","tomato","potato","cabbage"]
print("Brinjal" in veg)
if("Brinjal" in veg):
    print("vegetable available")
else:
    print("vegetable not available")















