import json
import random
import string

# 生成随机用户名
def generate_username(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# 生成随机密码
def generate_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# 生成用户数据
users = {}
for i in range(100):
    username = generate_username()
    password = generate_password()
    users[username] = {"password": password}

# 将用户数据保存到 JSON 文件
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

print("JSON file generated successfully.")
