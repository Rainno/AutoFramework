# 演示 requests 库的基本使用流程
# 与 Jmeter、 POSTman 实现接口测试的流程一致
# 0、 导包
import requests
# 1、 定位接口资源
url = "http://127.0.0.1:8000/api/departments/"
# 2、 设计提交的测试数据
myParam = {"$dep_id_list": "T2001N,T2005N"}
# 3、 发送并接收响应结果
response = requests.get(url, params=myParam)
# 获取状态码并打印
print(response.status_code)
# 获取响应头并打印
print(response.text)