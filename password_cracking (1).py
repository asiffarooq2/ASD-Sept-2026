# import hashlib
# password = "hello123"
# hash_value = hashlib.sha256(password.encode()).hexdigest()
# print(hash_value)
# user_password=input("Enter your password")
# user_hash_value = hashlib.sha256(user_password.encode()).hexdigest()
# if hash_value==user_hash_value:
#     print("Password Matched")
# else:
#     print("Password not matched")

# import hashlib
# import itertools
# import string
# def brute_force(target_hash,max_length=4):
#     characters=string.ascii_lowercase+string.digits #a-z,0-9
#     for length in range(1,max_length+1):
#         for guess in itertools.product(characters,repeat=length):
#             # print(guess)
#             guess_word=''.join(guess)
#             print(guess_word)
#             hashed=hashlib.md5(guess_word.encode()).hexdigest()
#             # print(hashed)
#             if hashed==target_hash:
#                 return guess_word
#     return None

# text=input("Enter the Password:")
# target_hash=hashlib.md5(text.encode()).hexdigest()
# result=brute_force(target_hash)
# print("Password found:",result)

# import hashlib
# import string
# import itertools
# import threading

# found = False
# result = None
# lock = threading.Lock()

# def brute_force_worker(start_chars, target_hash, max_length):
#     global found, result
#     characters = string.ascii_lowercase + string.digits
#     for ch in start_chars:
#         for length in range(1, max_length + 1):
#             if found:
#                 return
#             for guess in itertools.product(characters, repeat=length - 1):
#                 if found:
#                     return
#                 guess_word = ch + ''.join(guess)
#                 hashed = hashlib.md5(guess_word.encode()).hexdigest()
#                 if hashed == target_hash:
#                     with lock:
#                         found = True
#                         result = guess_word
#                     return
                
# def multithreaded_bruteforce(target_hash, max_length=4, threads_count=4):
#     threads = []
#     characters = string.ascii_lowercase + string.digits

#     chunk_size = len(characters) // threads_count
#     chunks = [
#         characters[i:i + chunk_size]
#         for i in range(0, len(characters), chunk_size)  #List comprehension
#     ]
#     for chunk in chunks:
#         t = threading.Thread(
#             target=brute_force_worker,
#             args=(chunk, target_hash, max_length)
#         )
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     return result
# # ---------------- MAIN ---------------- #
# text = input("Enter the Password: ")
# target_hash = hashlib.md5(text.encode()).hexdigest()
# print("Target Hash:", target_hash)
# password = multithreaded_bruteforce(target_hash, max_length=7, threads_count=6)
# if password:
#     print("Password found:", password)
# else:
#     print("Password not found")



import re
def check_strength(password):
    if len(password) < 8:
        return "Very Weak"
    if not re.search(r"[0-9]", password):
        return "Weak (add numbers)"
    if not re.search(r"[A-Z]", password):
        return "Medium (add uppercase)"
    if not re.search(r"[!@#$%^&*]", password):
        return "Strong (add special characters)"
    return "Very Strong"

name=input("Enter your password:")
print(check_strength(name))