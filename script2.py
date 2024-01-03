# function without parameter and with return type 
def add():
    print(9+9)

add()
add()
add()
add()
add()

# function with parameter and without type
def addB(x,y):
    print(x+y)

addB(12,4)
addB(10,5)
addB(1,1)
addB(11,11)

# function with parameter and return value 
# 100 - given    # 100 + 100 ,  100 / 5 , 100 - 50 , 100 * 0.10
# 100 - shown    # value 

def addC(x,y):
    return x + y
q3 = addC(12,2)
print(q3)
print(q3 + q3)
print(q3 / 4)
print(q3 - 4)
print(q3 * 0.10)
