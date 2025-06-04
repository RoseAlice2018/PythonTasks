import hashlib

def hash_password(password):
    # 使用sha256算法对密码进行哈希
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def Login():
    name = input("请输入用户名：")
    password = input("请输入密码：")
    with open("password.txt", "r") as f:
        for line in f:
            app_name, encrypted_password = line.strip().split(":")
            if app_name == name and hash_password(password) == encrypted_password:
                print("登录成功！")
                return
    print("登录失败！")
def Save(name, password):
    encrypted_password = hash_password(password)
    with open("password.txt", "a") as f:
        f.write(f"{name}:{encrypted_password}\n")

def Register():
    name = input("请输入用户名：")
    password = input("请输入密码：")
    Save(name, password)

while True:
    method = input("选择模式： 1 注册 2 登录\n")
    if method == "1":
        Register()
    elif method == "2":
        Login()
    else:
        print("无效的选择")


