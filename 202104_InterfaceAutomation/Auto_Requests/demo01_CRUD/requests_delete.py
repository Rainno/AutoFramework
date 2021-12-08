# 需求:删除学院信息
import requests
# 发请求， 接收响应
response = requests.delete("http://127.0.0.1:8000/api/departments/T01/")
print(response.status_code)
print(response.text)