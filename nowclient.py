#python3 ./nowclient.py
#use hml page instead of using client
import requests
import os

def login(url):
    """用户登录"""
    username = input("Please input username for login: ")
    password = input("Please input password for login: ")
    response = requests.post(url, json={"username": username, "password": password})
    return response

def register(url):
    """用户注册"""
    username = input("Please input new username for register: ")
    password = input("Please input new password for register: ")
    response = requests.post(url, json={"username": username, "password": password})
    return response

def logout(url):
    """用户登出"""
    response = requests.get(url)
    return response

def upload_file(url, file_path, cookies):
    """上传文件并打印服务器响应
    files = {'document': open(file_path, 'rb')}
    response = requests.post(url, files=files, cookies=cookies)
    return response
    """
    """上传文件并打印服务器响应"""
    if not os.path.exists(file_path):
        return {"status_code": 400, "error": "File not found. Please ensure the file path is correct."}
    try:
        with open(file_path, 'rb') as f:
            files = {'document': f}
            response = requests.post(url, files=files, cookies=cookies)
            return response
    except Exception as e:
        return {"status_code": 400, "error": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"
    while True:
        action = input("What do you want to do? (1 for login, 2 for register, 3 for exit): ")
        if action == '1':
            login_url = f"{base_url}/login"
            login_response = login(login_url)
            if login_response.status_code == 200:
                print("Logged in successfully")
                cookies = login_response.cookies
                while True:  # 在登录成功后添加循环
                    user_choice = input("Choose an option: (1 for upload, 2 for logout): ")
                    if user_choice == '1':
                        file_path = input("Input the filename for upload: ")
                        upload_response = upload_file(f"{base_url}/upload", file_path, cookies)
                        if isinstance(upload_response, dict):
                            print(upload_response["error"])
                        else:
                            if upload_response.status_code == 200:
                                print("Document analyzed successfully with the following result:")
                                print(upload_response.json())
                            else:
                                print("Error during document upload:", upload_response.status_code)
                    elif user_choice == '2':
                        print("Logging out successfully...")
                        break
                    else:
                        print("invalid action. Please Input 1 for upload, 2 for logout")
                '''
                file_path = input("Input the filename for upload: ")
                upload_response = upload_file(f"{base_url}/upload", file_path, cookies)
                if isinstance(upload_response, dict):
                    print(upload_response["error"])
                else:
                    if upload_response.status_code == 200:
                        print("Document analyzed successfully with the following result:")
                        print(upload_response.json())
                    else:
                        print("Error during document upload:", upload_response.status_code)
                '''
            else:
                print("Login failed. Wrong username or password. ")
        elif action == '2':
            reg_url = f"{base_url}/register"
            reg_response = register(reg_url)
            if reg_response.status_code == 200:
                print("Registered successfully")
            else:
                print("Registration failed . Already existed user")
        elif action != '3':
            print ("invalid action. Please Input 1 for login, 2 for register, 3 for exit ")
        elif action == '3':
            print("Exiting...")
            break  # This breaks the loop and ends the program

