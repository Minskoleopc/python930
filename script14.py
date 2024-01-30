#         0             1     2   3
info = ["chinmay","deshpande",23,44]

# # retrive 
# print(info[0])
# # update 
# info[0] = "tanmay"
# # add 
# info.append("punr")
# # delete
# info.remove("deshpande")

# dictionary

# program 2
info2 = {
    #  property:value
    #  key     :value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":44
}
print(info2)
print(type(info2))
print(info2["firstName"])
# dictionary does not stores the value by index
#print(info2[0])

# retrive
print(info2['lastName'])
# udapte
info2['lastName'] = "dani"
print(info2)
# add
info2['city'] = "pune"
info2['city'] = "nagpur"
print(info2)
# delete
info2.pop("lastName")
print(info2)
info2.popitem()
print(info2)

# revision

vehicle = {
    "color":"red",
    "type":"sedane"
}

# print(vehicle['color'])
# vehicle['color']  = "blue"
# vehicle['regNo'] = 123
# vehicle.pop('type')


# program 3
fruits = ["apple","mango","banana","apple"]
print(fruits)

info3 = {
    "firstName":"chinmay",
    "age":23,
    "skills":["python","js","sql"],
    "age":45
}
print(info3)
print("apple" in fruits)
print("age" in "SKills")
























