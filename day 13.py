# pip install cryptography
#pip list

# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# cipher = Fernet(key)
# print(key)
# # message = b"hello world"
# message = "hello world"
# # encrypted = cipher.encrypt(message)
# encrypted = cipher.encrypt(message.encode())
# print("Encrypted:", encrypted)
# decrypted=cipher.decrypt(encrypted)
# print("Decrypted:", decrypted.decode())
# with open("secret.key", "wb") as f:
#     f.write(key)
#     f.write(b"Asif")


#pip install rsa
# import rsa
# public_key, private_key = rsa.newkeys(512)
# msg = "hello"
# encrypted = rsa.encrypt(msg.encode(), public_key)
# decrypted = rsa.decrypt(encrypted, private_key).decode()
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)


#Hashing---One way process---only encryption no decryption
# import hashlib
# password="Aasif@123"
# hashed=hashlib.sha256(password.encode()).hexdigest()
# print(hashed)
# user_password=input("Enter your password:")
# user_hashed=hashlib.sha256(user_password.encode()).hexdigest()
# if user_hashed==hashed:
#     print("Password matched")
# else:
#     print("Incorrect password")
# eb8eddc24658c7bea481d1ca82c17584b69416852fffb6eb56a93016b3973cdb

import os
import hashlib
password = "mypassword"
salt = os.urandom(16)
salted1 = salt + password.encode()
hashed1 = hashlib.sha256(salted1).hexdigest()
print("Salt:", salt)
print("Salted Hash:", hashed1)

password =input("Enter your password")
# salt = os.urandom(16)
salted2 = salt + password.encode()
hashed2 = hashlib.sha256(salted2).hexdigest()
print("Salt:", salt)
print("Salted Hash:", hashed2)
if hashed1==hashed2:
    print("Password Matched")
else:
    print("Incorrect password")