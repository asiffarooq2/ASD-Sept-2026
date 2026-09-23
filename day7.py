#Collections---->Lists,Tuples,Sets and Dictionaries
# my_list=[57,89,88,"Abhishek","Asif","True",None,57,88,15.6,17.52] #Ordered
# my_list2=[85,13,57,14,74,89]
# # print(type(my_list))
# # print(my_list) #Mutable-->Change there values
# # my_list[2]="Abhishek"
# print(my_list)
# print(my_list[2:9])
# print(my_list[-3])
# my_list.append("ASD")
# my_list.insert(4,"Suraj")
# my_list.remove(88)
# my_list.pop()
# my_list.clear()
# my_list2.sort()
# my_list.extend(my_list2)
# print(my_list)

#Tuples--Collections,Ordered but not mutable
# my_tuple=(15,13.35,"Asif",False,None,57,88,94)
# print(type(my_tuple))
# print(my_tuple[-1])
# print(my_tuple[:5])
# my_tuple[2]="Mohan"
# my_tuple=(15)
# print(type(my_tuple))
# my_list=[56]
# print(type(my_list))
# t1=(1,2,3)
# t2=(5,9,0)
# t3=t1+t2
# t4=t1*3
# print(t4)
# fruits=("Apple","Banana","Orange","Grapes") #Packing
# print(fruits)
# a,b,c,d=fruits#Unpacking
# print(a)
# print(b)
# print(c)
# print(d)
my_list = [57,89,88,"Abhishek","Asif","True",None,57,88,15.6,17.52] 
# print(len(my_list))
# for asif in range(1,11):
#     print(asif)
# for item in my_list: #Traversing a list
#     print(item)
# name=float(input("Enter the item to search:"))
# if name in my_list:
#     print("Present")
# else:
#     print("Not Present")
# marks = [78, 90, 67, 88]
# print(sum(marks))
a = [10, 20]
b = a
c=[10,20]
print(a is b)
print(b is c)