# my_list=[33,58,97,69] #Ordered
# # print(my_list)
# my_set={87,100,99,58,39,1,12,13,58,12,14,13,14,99} #Unordered
# my_set.add(900)
# my_set.update([999,888,777])
# my_set.remove(588)
# my_set.discard(588)
# my_set.pop(99)
# my_set.clear()
# print(my_set)


# set1 = {1, 2, 3,90,60}
# set2 = {3, 4, 5,60}
# print(set1.union(set2))  
# print(set1.intersection(set2))  
# print(set1.difference(set2))  

# my_dict={
#     "name":"Aman",
#     "age":25,
#     "city":"Delhi"
# }
# print(my_dict["age"])
# print(my_dict["city"])
# print(type(my_dict))
# my_dict["name"]="Asif"
# print(my_dict["name"])
# my_dict["course"]="Python"
# my_dict["academy"]="ASD"
# # print(my_dict)
# # print(my_dict.get("names"))
# # print(my_dict["names"])
# # my_dict.pop("name")
# print(my_dict)
# my_dict.popitem()
# print(my_dict)

# student = {
# "name": "Aman",
# "marks": [80, 90, 85],
# "info": {
# "city": "Delhi",
# "class": "12th"
# },
# "course":{
#     "coding":"Python",
#     "networking":"CCNA"
# }
# }
# print(student["course"]["networking"])

# student = {
#     "name": "Ravi",
#     "math": 100,
#     "science": 85,
#     "english": 88
# }
# student["total"]=student["math"]+student["science"]+student["english"]
# print(student)
# print(student.values())
# print(student.keys())
# print(student.items())
# for item in student:
#     print(student[item])
# for item in student.keys():
#     print(item)
# for item in student.values():
#     print(item)

# for key,value in student.items():
#     print(f"{key}:{value}")

qty=int(input("Enter the quantity:"))
my_item={
    "name":"HP",
    "price":15000,
    "GST":500
}
my_item["quantity"]=qty
my_item["total"]=(my_item["price"]+my_item["GST"])*my_item["quantity"]
print(my_item["total"])