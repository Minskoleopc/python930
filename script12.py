
first_name = "chinmay"
print(first_name)
last_name = 'deshpande'
print(last_name)
print(type(last_name))

q = """
    This is python string
    I am learning python3

"""
print(q)

r = '''
    I am also learning js , js means javascript
'''
print(r)


# program 2

# string stores the value by index??
city = "pune"
#  0   1    2    3
#  p   u    n     e
print(city[0])
print(city[1])


# program 3

city3 = "chandrapur"

# 0      1       2      3     4      5      6     7      8     9
# c      h       a      n     d      r      a     p      u     r
# -10   -9       -8    -7    -6     -5     -4    -3     -2     -1

#stringName[startIndex:endIndex(not included):Steps]
print(city3[1::])
print(city3[1:7:])
print(city3[1:7:1])
print(city3[0:len(city3):2])
print(city3[0:len(city3):3])
print(city3[-7::])
print(city3[-7:-2:])
print(city3[-7:8:])
print(city3[1:-1:])
print(city3[-1:-10:-2])


# program 4
#           0        1         2
fruits = ["apple","banana","grapes"]
print(fruits)

for x in range(len(fruits)):
    print(fruits[x])

for item in fruits:
    print(item)

lang = "java"

for x in range(len(lang)):
    #print(x)
    print(lang[x])

for char in lang:
    print(char)






