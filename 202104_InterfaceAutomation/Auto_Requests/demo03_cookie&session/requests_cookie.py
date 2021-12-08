# 访问 TPshop 实现登录与订单查询
import requests
# 流程
# 1、 获取验证码,第一次访问服务器， 服务器会生成 session， 并且响应回 cookie
response = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response.status_code)
print(response.content)
print(response.headers)
# 获取 cookie 的值
cookie_value = response.cookies.get("PHPSESSID")
print(cookie_value)
print("-"*80)
# 2、 执行登录
# 问题: 登录失败, 原因: 没有提交 cookie
myData = {
    "username":"13012345678",
    "password":"123456",
    "verify_code":"8888"
} #发送请求时， 设置 cookie
response = requests.post("http://localhost/index.php?m=Home&c=User&a=do_login",
                         data=myData,cookies={"PHPSESSID":cookie_value})
print(response.status_code)
print(response.json())
# 3、 查看订单
print("-"*80)
response = requests.get("http://localhost/Home/Order/order_list.html",
                        cookies={"PHPSESSID":cookie_value})
print("订单:",response.status_code)
print("订单:",response.text)