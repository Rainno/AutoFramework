# 1、 导包
import pymysql

# 2、 创建连接
conn = pymysql.connect(host="127.0.0.1", port=3306, database="books",
                       user="root", password="root", charset="utf8", autocommit=True)
# 3、 创建游标
cursor = conn.cursor()
# 4、 核心
sql = "delete from t_book where id = 4"
cursor.execute(sql)
# 5、 释放资源
cursor.close()
conn.close()
