# 修改学院信息
import requests
# 发请求， 接收响应
myJson = {
    "data": [
        {
            "dep_id": "T01",
            "dep_name": "C++/学院",
            "master_name": "C++-Master",
            "slogan": "Here is Slogan"
        }
    ]
}
response = requests.put("http://127.0.0.1:8000/api/departments/T01/",json=myJson)
print(response.status_code)
print(response.text)