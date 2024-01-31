
listA = ["chinmay","deshpande",24,55]

info  = {
    # property   # value 
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":24,
    "rollNo":55,
    "age":54
}

# retrive
# print(info['age'])

# update
# info['rollno'] = 66

# property exist
#print("rollNo" in info)

#print(info["age"])
# vehicle = {
#     "color":"blue",
#     "type":"sedane"
# }
# print(type(vehicle))
# # does not stores value by index
# #print(vehicle[0])

# names = ["chinmay","sarika","poorva","amit","amol"]
# print(len(names))
# print(len(vehicle))

# program 1

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":55
}

for key in student:
    print(key)

for prop in student:
    print(prop,student[prop])




animal = {
    "color":"red",
    "legs":4,
    "name":"tiger"
}

print(animal['color'])

for key in animal:
    print(key,animal[key])


# keys()
for key in animal.keys():
    print(key)

# values()
for val in animal.values():
    print(val)

# items()
for k,v in animal.items():
    print(k,v)


subjects = {
    "subOne":"marathi",
    "subTwo":"hindi",
    "subThree":"english",
    "subFour":"sanskrit"
}

# keys(),values(),items()

# clear()
# subjects.clear()
# print(subjects)


#pop()
subjects.pop("subOne")
print(subjects)

# popitem()
subjects.popitem()
print(subjects)


subjects2 = {
    "subOne":"geography",
    "subTwo":"history",
    "subThree":"science",
    "subFour":"Maths"
}

# subject3 = subjects2
# print(subjects2)
# print(subject3)

# subjects2["subOne"] = "civics"
# print(subject3)
# print(subjects2)

subject3 = subjects2.copy()
subjects2["subOne"] = "civics"
print(subject3)
print(subjects2)


students3 = {
    "firstName":"rasika",
    "lastName":"kulkarni"
}

print("hello")
#print(students3['firstNamee'])
print(students3.get('firstNamee'))
print('bye')




#a = students3.get('firstNam2')
#b = students3['firstNam2']

#print(a)
#print(b)





































