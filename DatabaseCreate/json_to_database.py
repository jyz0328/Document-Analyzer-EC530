import sqlite3
import json

# 读取user.json文件
with open("users.json", "r") as file:
    users_data = json.load(file)

# 连接到数据库
conn = sqlite3.connect('users.db')
c = conn.cursor()

# 创建用户凭据表
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text PRIMARY KEY, password text)''')

# 将JSON数据插入到数据库中
for username, data in users_data.items():
    password = data["password"]
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))


# 保存（提交）更改
conn.commit()

# 关闭连接
conn.close()
