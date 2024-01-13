
# day 1
# variables 

x = 10
print(x)
x = 100
print(x)

# Arithmetic operation 

s = 8
t = 4

print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)

q = 9
r = 3

print(q+r)
print(q-r)
print(q*r)
print(q/r)
print(q%r)

def Calculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)
Calculator(12,3)
Calculator(4,2)

# day2

def addA():
    print(9+9)
addA()
addA()
addA()
addA()

def addB(x,y):
    print(x+y)
addB(12,3)
addB(12,1)
addB(12,8)

def addC(x,y):
    return x + y
a = addC(12,3)
print(a)
print(a+a)
print(a*0.10)

# day 3

# // Introvert      // Extrovert
# // calm             loud
# // less social      more social
# // less outing      more outing

# // Human
# // Properties - color , gender , height , weight
# // Methods - walk() , talk()

# // Vehicle 
# // Properties - color , model , company , type , regNo
# // Method - start() , stop()

# // Bank acc
# // Properites - accNO , accName , accType , bal
# // Methods - withdrawl() , deposit()

a = 10 
print(a)
print(type(a))
# 1 , 4 ,0

b = 10.4
print(b)
print(type(b))
# 1.3 , -4.3 ,0.0

c = True
print(c)
print(type(c))
# True False

c  = "chinmay"
print(c)
print(type(c))
#'chinmay' , 'A' , 'sad',"##","asd@#432","c "

# comparison 
# entity == entity ====> boolean
# < , > , <= , >= ,!= , ==

print(10 > 3)
print(10 < 3)
print(10 >= 3)
print(10 <= 3)
print(10 >= 10)
print(10 <= 10)
print(10 != 10)
print(10 != 9)

# logical operator 

# and 

# True  and True   ----> True 
# False and True   ----> False
# True  and False  ----> False
# False and False  ----> False

print(3 == 3 and 2 == 2)
print(3 == 3 and 2 != 2)
print(3 != 3 and 2 == 2)
print(3 != 3 and 2 != 2)

# or

# True  or True   ----> True 
# False or True   ----> True
# True  or False  ----> True
# False or False  ----> False

print(3 == 3 or 2 == 2)
print(3 == 3 or 2 != 2)
print(3 != 3 or 2 == 2)
print(3 !=3 or 2 != 2)


# not
#not True - False
#not False - True
print(not 3 == 3)
print(not 3 == 4)















