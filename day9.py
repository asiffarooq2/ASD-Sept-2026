#Read Operation In Files
# my_file=open("raman.txt","r")
# print(my_file.read())
# print(my_file.read(13))
# print(my_file.readline())
# print(my_file.readlines())
# my_data = my_file.readlines()
# print(my_data[2])
# my_file.close()

#Write Mode
# text_file=open("Nomesh.txt","x")
# text_file.write("Python is a good programming language")
# text_file.close()

#Append Mode
# text_file=open("Nomesh.txt","a")
# text_file.write("\nJavascript is mostly used for web development")
# text_file.close()

# with open("Nomesh.txt","r") as f:
#     print(f.read())

# with open("Sawan.txt","w") as f:
#     f.write("Sawan was one of my Student.\t")
#     f.write("Sunil was one of my favourite students\n")

# with open("Sawan.txt","x") as f:
#     f.write("Sawan was one of my Student.\t")
#     f.write("Sunil was one of my favourite students\n")

# with open("image.jpg", "rb") as f:
#     data = f.read()
# with open("image2.jpg", "wb") as f:
#     f.write(data)
#     print("File created successfully")

import os
# name_of_file=input("Enter the name of your file:")
# text=input("Enter your text here:")
# if os.path.exists(name_of_file):
#     print("File already exists")
# else:
#     with open(name_of_file,"w") as f:
#         f.write(text)
#     print("File created successfully")

# name_of_file=input("Enter the name of your file:")
# os.remove(name_of_file)
# print("File deleted Succesfully")

with open("Nomesh.txt", "r") as f1:
    data1 = f1.read()
with open("Sawan.txt", "r") as f2:
    data2 = f2.read()
# print(data1)
# print(data2)
if data1 == data2:
    print("Both files are same")
else:
    print("Different files")