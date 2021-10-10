import hashlib

result = hashlib.md5("abcdef609043".encode())
print(result.hexdigest())