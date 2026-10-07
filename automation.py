# import os
# base_path = "D:/Cryptography"
# for i in range(1, 6):
#     folder = f"Crypto_{i}"
#     os.makedirs(os.path.join(base_path,folder),exist_ok=True)
# print("Folders created!")


# import os
# base_path="E:/ASD Academy"
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
# BASE_PATH = r"E:/ASD Academy"
# PREFIX = "Python_"

# for root, dirs, files in os.walk(BASE_PATH):
#     for filename in files:
#         if filename.endswith(".txt") and not filename.startswith(PREFIX):
#             print("Inside if condition")
#             old_path = os.path.join(root, filename)
#             new_path = os.path.join(root, PREFIX + filename)
#             os.rename(old_path, new_path)
#             print(filename)
#             # os.remove(filename)
# print("All files renamed successfully!")

# import os
# BASE_PATH = r"E:/ASD Academy"
# for root, dirs, files in os.walk(BASE_PATH):
#     for filename in files:
#         if filename.endswith(".txt"):
#             file_path = os.path.join(root, filename)
#             os.remove(file_path)
# print("All .txt files deleted successfully!")


# import shutil
# import os
# os.makedirs("Ujjawal",exist_ok=True)
# # shutil.rmtree("Hello")
# for i in range(1,3):
#     shutil.copy(f"file_{i}.txt","Ujjawal")
#     shutil.move(f"Ujjawal/file_{i}.txt","Demo")

# from openpyxl import Workbook
# wb = Workbook()
# sheet = wb.active
# sheet["A1"] = "Name"
# sheet["B1"] = "Marks"
# sheet["C1"]="Class"
# data = [("Aman", 85,"10th"), ("Riya", 90,"11th"), ("Sam", 72,"12th")]
# for i, (name, marks,grade) in enumerate(data, start=2):
#     sheet[f"A{i}"] = name
#     sheet[f"B{i}"] = marks
#     sheet[f"C{i}"]= grade
# wb.save("students.xlsx")

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# search = driver.find_element("name", "q")
# search.send_keys("Web scraping tools in python")
# search.send_keys(Keys.RETURN)
# time.sleep(10)
# driver.quit()


import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"
response = requests.get(url, timeout=15)
response.raise_for_status()
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find(
        "p", class_="instock availability"
    ).get_text(strip=True)

    print("Book Title:", title)
    print("Price:", price)
    print("Availability:", availability)
    print("-" * 40)
