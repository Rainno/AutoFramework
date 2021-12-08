# 使用 session 简化 TPshop 的登录操作
import requests
# 1、 现获取 session 对象
session = requests.session() # session = requests + cookie实现
# 2、 使用 session 对象而非 requests 向服务器发送请求， 先获取验证码（都不需要单独处理 cookie）
response = session.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response.status_code)
print(response.content)
print("-"*80)
# 3、 使用 session 对象而非 requests 向服务器发送请求， 执行登录（都不需要单独处理 cookie）
myData = {
    "username":"13012345678",
    "password":"123456",
    "verify_code":"8888"
}
response = session.post("http://localhost/index.php?m=Home&c=User&a=do_login",data=myData)
print(response.status_code)
print(response.json())