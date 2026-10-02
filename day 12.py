import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/56")
# if response.status_code == 200:
#     data = response.json()
#     # print(data)
#     print("Title:", data["title"])
#     print("Body:", data["body"])
# else:
#     print("Error:", response.status_code)

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

import json
person = {
    "name": "Rahul",
    "age": 22,
    "city": "Delhi"
}
print(type(person))
new_format=json.dumps(person)  #Converts Dictionary to Json Format
print(type(new_format))
old_format=json.loads(new_format) #Converts JSON to dictionary
print(type(old_format))