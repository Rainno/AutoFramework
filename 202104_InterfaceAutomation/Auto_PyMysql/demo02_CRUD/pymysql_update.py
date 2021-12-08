# 1、 导包
import pymysql

# 2、 创建连接
conn = pymysql.connect(host="127.0.0.1", port=3306, database="books",
                       user="root", password="root", charset="utf8", autocommit=True)
# 3、 创建游标对象
cursor = conn.cursor()
# 4、 发送 SQL
sql = "update t_book set `read` = 400 where id = 4"
cursor.execute(sql)
# 5、 释放资源
cursor.close()
conn.close()
