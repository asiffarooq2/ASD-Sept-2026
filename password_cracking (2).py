# import hashlib
# def dictionary_attack(target_hash,wordlist):
#     with open(wordlist,'r') as file:
#         for line in file:
#             password=line.strip()
#             hashed=hashlib.sha256(password.encode()).hexdigest()
#             # print("File Hash",hashed)
#             if hashed==target_hash:
#                 return password
#     return None
# user_password=input("Enter your password:")
# target_hash=hashlib.sha256(user_password.encode()).hexdigest()
# print("Input Hash:",target_hash)
# result=dictionary_attack(target_hash,"wordlist.txt")
# print("Password Found:",result)

import hashlib
wordlist = ["admin", "test", "hello123", "password"]
password=input("Enter the Password:")
target_hash=hashlib.sha256(password.encode()).hexdigest()
# target_hash = hashlib.sha256("hello123".encode()).hexdigest()
for word in wordlist:
    if hashlib.sha256(word.encode()).hexdigest() == target_hash:
        print("Match found:", word)
        break