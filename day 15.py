# import os
# base_path = "D:/Automation"
# for i in range(1, 1001):
#     folder = f"Folder_{i}"
#     os.makedirs(os.path.join(base_path, folder), exist_ok=True)
#     # "D:/Automation/Folder_1"
# print("Folders created!")

# for i in range(1, 6):
#     file_path = f"file_{i}.txt"
#     with open(file_path, "w") as f:
#         f.write(f"This is file number {i}")

# import os
# prefix = "NEW_"
# for filename in os.listdir():
#     if filename.endswith(".txt"):
#         os.rename(filename, prefix + filename)
# import os
# prefix = "NEW_"
# for filename in os.listdir():
#     if filename.endswith(".txt"):
#         os.rename(filename, prefix + filename)
#         print(filename)
#         # os.remove(filename)

# import os
# base_path="E:/ASDE Academy"
# for i in range(1,6):
#     folder=f"Folder_{i}"
#     folder_path=os.path.join(base_path,folder)
#     print(folder_path)
#     # os.makedirs(os.path.join(base_path,folder),exist_ok=True)
#     os.makedirs((folder_path),exist_ok=True)
#     file_name = f"file_{i}.txt"
#     file_path=os.path.join(folder_path,file_name)
#     print(file_path)
#     with open(file_path, "w") as f:
#         f.write(f"This is file number {i}")
#     # "E:/ASD Academy/folder_1/file_1.txt
# print("Folders created Succesfully")


# import os
# BASE_PATH = r"E:/ASDE Academy"
# for root, dirs, files in os.walk(BASE_PATH):
#     print("Root=",root)
#     print("DIRS=",dirs)
#     print("files=",files)
#     for filename in files:
#         if filename.endswith(".txt"):
#             file_path = os.path.join(root, filename)
#             print(file_path)
#             # os.remove(file_path)
# print("All .txt files deleted successfully!")

# import shutil
# import os
# os.makedirs("Ujjawal",exist_ok=True)
# # shutil.rmtree("Hello")
# for i in range(1,3):
#     # shutil.copy(f"test_{i}.txt","Ujjawal")
#     shutil.move(f"test_{i}.txt","Ujjawal")
#     print("Files moved successfully...")
#     # shutil.move(f"Ujjawal/file_{i}.txt","Demo")


from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
sheet["A1"] = "Name"
sheet["B1"] = "Marks"
sheet["C1"] = "City"
data = [("Aman", 85,"Srinagar"), ("Riya", 90,"Kota"), ("Sam", 72,"Ballia")]
for i, (name, marks,city) in enumerate(data, start=2):
    sheet[f"A{i}"] = name
    sheet[f"B{i}"] = marks
    sheet[f"C{i}"] =city
wb.save("students.xlsx")

# my_list=["Apple","Banana","Orange","Mango","Walnut"]
# i=1
# for item in my_list:
#     print(i,item)
#     i+=1

# for i,item in enumerate(my_list,start=1):
#     print(i,item)