import requests
#response = requests.get("http://127.0.0.1:8000/api/departments/",params={"$dep_id_list":"T2001N,T2005N"})

response = requests.get("http://www.baidu.com")
# 响应内容获取
# 1、 响应行信息 状态码 + URL
print("状态码:", response.status_code)
print("URL:",response.url)
# 2、 响应头信息
print("-"*80)
print("获取所有响应头:",response.headers)
print("获取指定响应头:",response.headers.get("Content-Type"))
print("获取编码集:",response.encoding)
print("获取cookie:",response.cookies)
# 3、 响应体信息
print("-"*80)
print("文本回显响应体:",response.text)
print("二进制显示数据:",response.content)
print("JSON方式回显数据:",response.json().get("count")) # 可以以 JSON 格式解析数据,如果响应体是非 JSON 数据， 解析报错