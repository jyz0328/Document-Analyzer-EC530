#python3 ./nowclient.py
import requests

def login(url):
    """用户登录"""
    username = input("plz input username: ")
    password = input("plz input password: ")
    response = requests.post(url, json={"username": username, "password": password})
    return response

def logout(url):
    """用户登出"""
    response = requests.get(url)
    return response

def upload_file(url, file_path, cookies):
    """上传文件并打印服务器响应"""
    files = {'document': open(file_path, 'rb')}
    response = requests.post(url, files=files, cookies=cookies)
    return response

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"
    login_url = f"{base_url}/login"
    
    login_response = login(login_url)
    
    if login_response.status_code == 200:
        print("log in successfully")
        cookies = login_response.cookies
        
        file_path = input("input the filename for upload: ")
        upload_response = upload_file(f"{base_url}/upload", file_path, cookies)
        
        if upload_response.status_code == 200:
            print("analyze document successfully with following result:")
            print(upload_response.json())
        else:
            print("analyze document failed with following response:", upload_response.status_code)
        
        logout_response = logout(f"{base_url}/logout")
        
        if logout_response.status_code == 200:
            print("log out successfully")
    else:
        print("log in faniled with this response:", login_response.status_code)
