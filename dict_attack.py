# import hashlib
# def dictionary_attack(target_hash,wordlist):
#     with open(wordlist,'r') as file:
#         for line in file:
#             print(line)
#             password=line.strip()
#             print(password)
#             hashed=hashlib.sha256(password.encode()).hexdigest()
#             if hashed==target_hash:
#                 return password
#     return None
# password=input("Enter your password:")
# target_hash=hashlib.sha256(password.encode()).hexdigest()
# # print(target_hash)
# result=dictionary_attack(target_hash,'wordlist.txt')
# print("Password found=",result)

import hashlib
# wordlist = ["admin", "test", "hello123", "password"]
# target_hash = hashlib.sha256("hello123".encode()).hexdigest()
# for word in wordlist:
#     if hashlib.sha256(word.encode()).hexdigest() == target_hash:
#         print("Match found:", word)
#         break

target_password=input("Enter the password:")
target_hash=hashlib.sha256(target_password.encode()).hexdigest()
wordlist = ["admin", "test", "hello123", "password"]
def crack_sha256(prangya,aman):
    for asif in aman:
        hashed_word=hashlib.sha256(asif.encode()).hexdigest()
        if hashed_word==prangya:
            return asif   
    return None

sunil=crack_sha256(target_hash,wordlist) #Function Call
print("Password found=",sunil)