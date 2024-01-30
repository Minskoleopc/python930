

info = ["sarika","pansare",45,66]

# retrive 
# list stores the value by index
print(info[0])

# update 
info[0] = "poorva"
print(info)

# add 
info.append("pune")
info.insert(3,"hindi")

# delete
info.pop()
info.pop(2)
info.remove("poorva")

# duplicate  values allowed - yes
fruits = ["apple","banana","grapes","orange","apple"]
print(fruits)



info2 = {
    # property:value 
    # key:value
    "firstName":"sarika",
    "lastName":"pansare",
    "age":45,
    "rollNo":66
}

# print(info2[0]) not work
# retrive
print(info2['firstName'])
print(info2['age'])

# update 
info2['firstName'] = "poorva"
print(info2)

# add 
info2['city'] = "pune"
info2['city'] = "nagpur"
print(info2)

#delete
info2.pop("age")
info2.popitem()
print(info2)


vehicle = {
    "color":"blue",
    "type":"sedane",
    "color":"blue"
}
print(vehicle)

# particular property in dictionary
print("Color" in vehicle)
