greet = "hello"
greet2 = 'hi'
greet3 = """
hello I am
 learning js
"""
greet4 =  '''
    hello i am learning python
'''
print(greet)
print(type(greet))

#program 2
# String stores the value by index

name = "chinmay"
#  0     1     2    3    4     5   6
#  c     h     i    n    m     a    y
# -7    -6    -5   -4   -3    -2    -1

print(name[0])
print(name[-7])

#           0        1       2       3
fruits = ["apple","mango","banana","papaya"]
for x in range(4):
    #print(x)
    print(fruits[x])


for y in fruits:
    print(y)



# program 3
# looping through list
city = "nagpur"
# 0      1      2     3    4   5
# n      a      g     p     u    r

print(city[0])
for m in range(6):
    #print(m)
    print(city[m])

for x in city:
    print(x)


# program 4
#          0         1        2        3
listA  = ["apple","banana","grapes","papaya"]
print(listA[0])
listA[0] = "chikoo"
print(listA)

first_name = "chinmay"
print(first_name)
#first_name[0] = "e"

# program 5
#    0       1      2      3    4    5   6     7    8    9
#    c       h      a      n    d    r   a     p    u    r
#   -10      -9    -8      -7   -6  -5  -4    -3   -2    -1

city7 = "chandrapur"
#strinName[startIndex:EndIndex(not included):steps]
print(city7[3::])
print(city7[3:8:])
print(city7[3:8:1])
print(city7[0:10:2])
print(city7[0:10:3])
print(city7[-2::])
print(city7[-8:-1:])
print(city7[1:-1:])
print(city7[1:-1:2])
print(city7[-1:-10:-1])
print(city7[-1:-10:-2])







