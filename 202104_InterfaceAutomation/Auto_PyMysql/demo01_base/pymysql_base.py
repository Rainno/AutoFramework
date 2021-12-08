# 演示pymysql, 使用的框架代码

# 1、整合pymysql
import pymysql

# 2、创建连接（connection）
conn = pymysql.connect(host="127.0.0.1",
                       port=3306,
                       database="books",
                       user="localhost",
                       password="123456")
# 3、连接之上获取游标对象(cursor) -- 小毛驴
cursor = conn.cursor()
print(cursor)
print(conn)
# 4、核心：发送SQL


# 5、释放资源
cursor.close()
conn.close()
