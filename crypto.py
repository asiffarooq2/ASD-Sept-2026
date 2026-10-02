#Symmetric Encryption
from cryptography.fernet import Fernet
key=Fernet.generate_key()
cipher=Fernet(key) #Byte
# print(key)
# print(cipher)
# # message = b"hello world"
# message="Hello World"
# # encrypted=cipher.encrypt(message)
# encrypted=cipher.encrypt(message.encode())
# print("Encrypted:", encrypted)
# # decrypted=cipher.decrypt(encrypted)
# decrypted=cipher.decrypt(encrypted)
# print("Decrypted:",decrypted.decode())

# with open("secret.key", "wb") as f:
#     f.write(key)

# with open("secret.key", "rb") as f:
#     key = f.read()
#     cipher = Fernet(key)
# print(key)
# print(cipher)

#Asymmetric Encryption
# import rsa
# public_key, private_key = rsa.newkeys(512)
# msg = "I am Learning Python"
# encrypted = rsa.encrypt(msg.encode(), public_key)
# decrypted = rsa.decrypt(encrypted, private_key).decode()
# # decrypted = rsa.decrypt(encrypted, private_key)
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)

#Hashing Concept
import hashlib
password = "Sudip@123"
hashed=hashlib.sha256(password.encode()).hexdigest()#0-9,A-10---F-15
print("Hash:", hashed)
# user_password=input("Enter you password:")
# user_hashed=hashlib.sha256(user_password.encode()).hexdigest()
# # if password==user_password:
# if hashed==user_hashed:
#     print("Login Succesful")
# else:
#     print("Invalid Login")

import os, hashlib
password = "Sudip@123"
salt = os.urandom(16)
salted = salt + password.encode()
hashed = hashlib.sha256(salted).hexdigest()
print("Salt:", salt)
print("Salted Hash:", hashed)
my_password=salt+password.encode()
my_hashed = hashlib.sha256(my_password).hexdigest()
print("Salted Hash:",hashed)
print("My Salted Hash:",my_hashed)