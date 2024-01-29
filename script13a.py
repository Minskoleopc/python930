
first_name = "chinmay"
print(type(first_name))


strOne = "13124"
e = strOne.isdigit()
print(e)

strTwo = "chinmay"
e2 = strTwo.isalpha()
print(e2)

strThree = "chinmay123"
strFour = "chinmay"
strFive = "123"
strSix = "ac1@23"
strSix = "ac1 23"

print(strThree.isalnum())
print(strFour.isalnum())
print(strFive.isalnum())

# program2
info= "chinmaydeshpande010@gmail.com" 
#["chinmaydeshpande010","gmail.com"] 
e2 = info.split('@')
print(e2)

info2 = "I am learning javascript"
#["I ","m le","rning j","v","script"]
e3 = info2.split('a')
print(e3)
a  = ["I ","m le","rning j","v","script"]

#program 3
info4 = "I am learning python"
e4 = info4.replace("python","javascript")
print(e4)

# program 4
full_name = "Ninad"
e5 = full_name.istitle()
print(e5)

# program 5
lastName = "deshpande"
print(lastName.islower())

# program 6
lastName3 = "dESHPANDE"
e6 = lastName3.isupper()
print(e6)

print(lastName3.upper())
print(lastName3.lower())

# program 7
city = "@"
e7 = city.isspace()
print(e7)

city2 = "citynagpur"
print(city2.removeprefix("city"))

city3 = "nagpurcity"
print(city3.removesuffix("city"))
#######################################

city3.upper()
city3.lower()
city3.capitalize()
city3.startswith("n")
city3.endswith("y")
city3.strip()
city3.lstrip()
city3.rstrip()
city3.index("n")



str1 = "123"
str2 = "12.34"
str3 = "½"
str4 = "Ⅳ"  # Roman numeral 4

print(str1.isnumeric())  # True
print(str2.isnumeric())  # False
print(str3.isnumeric())  # True
print(str4.isnumeric())  # True


print(str1.isdigit())  # True
print(str2.isdigit())  # False
print(str3.isdigit())  # True
print(str4.isdigit())  # True


# digit - 0,1,2,3,4,5,6,7,8,9
# numeric 0-1 , romans , fractions
