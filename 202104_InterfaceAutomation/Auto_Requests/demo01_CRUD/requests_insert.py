# 演示以 POST 方式访问接口
# 需求: 添加学院信息
import requests
# 发送请求
myJson = {
    "data": [
        {
            "dep_id":"T01",
            "dep_name":"Test学院",
            "master_name":"Test-Master",
            "slogan":"Here is Slogan"
        }
    ]
}
response = requests.post("http://127.0.0.1:8000/api/departments/",json=myJson)
print(response.status_code) # 201
print(response.text) # 新增的数据