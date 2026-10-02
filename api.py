import requests
# response=requests.get("https://jsonplaceholder.typicode.com/posts/5")
# print(response.status_code)
# # if response.status_code==200:
# if response.status_code==200:
#     print(response.text)
#     print(type(response.text))
#     data=response.json() #Converts json format into dictionary format 
#     # print(data.keys())
#     # print(data.values())
#     print(data)
#     print(type(data))
#     # print(data["id"])
#     # print(data["title"])
#     # print(data["bodyes"])
#     print(data.get("bodyes"))
# else:
#     print("Error in fetching data")

# new_post = {
# "title": "Hello API",
# "body": "This is sample data.",
# "userId": 1
# }
# print(type(new_post))
# response=requests.post("https://jsonplaceholder.typicode.com/posts",json=new_post)
# if response.status_code == 201:
#     print("New Post Created:")
#     print(response.text)
#     print(response.json())
# else:
#     print("Failed")
# 201 = successfully created.

# updated = {
# "title": "Updated Title",
# "body": "Updated content"
# }
# response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated)
# if response.ok:
#     print("Updated Data:", response.json())

# response=requests.delete("https://jsonplaceholder.typicode.com/posts/5")
# if response.status_code==200:
#     print("Post deleted Successfully")
#     print(response.text)
#     print(type(response.text))
#     data=response.json() #Converts json format into dictionary format 
#     print(data)
#     # print(data.keys())
#     # print(data.values())

# import json
# person = {
# "name": "Rahul",
# "age": 22,
# "city": "Delhi"
# }
# print(type(person))
# data=json.dumps(person)
# print(data)
# print(type(data))
# dict_data=json.loads(data)
# print(type(dict_data))
# with open("person.json", "w") as f:
#     json.dump(person, f, indent=7)
# print("JSON saved")

# with open("person.json","r") as f:
#     data=json.load(f)
# print(data)
# print(data["city"])

# import requests
# city = "Delhi"
# url = f"https://api.weatherapi.com/v1/current.json?key=demo&q={city}"
# response = requests.get(url)
# if response.ok:
#     data = response.json()
#     print("Temperature:", data["current"]["temp_c"], "°C")
# else:
#     print("Error fetching data")

# import requests
# site = input("Enter website URL: ")
# response = requests.get(site)
# print("Status Code:", response.status_code)

# import requests
# user_id = 8
# response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
# if response.ok:
#     data= response.json()
#     print("Name:", data["name"])
#     print("Email:", data["email"])