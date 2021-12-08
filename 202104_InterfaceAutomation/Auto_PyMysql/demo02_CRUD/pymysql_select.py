# 需求：查询books中t_book表的所有数据
import pymysql

conn = pymysql.connect(host="127.0.0.1",
                       port=3306,
                       database="books",
                       user="localhost",
                       password="123456",
                       charset="utf8")

cursor = conn.cursor()
# 查询语句
sql = "select * from t_book"
cursor.execute(sql) # cursor执行sql语句
# 获取响应结果的行数
print("响应结果行数：", cursor.rowcount)
# 获取单条数据，一次调用获取一条
# row1 = cursor.fetchone()
# row2 = cursor.fetchone()
# row3 = cursor.fetchone()
# 一次获取所有数据
rows = cursor.fetchall()
# print("所有数据：", rows)
for row in rows :
    print("----------------")
    print(row)
    print("id:",row[0])
    print("书名:",row[1])
    print("时间:",row[2])
    print("阅读数:",row[3])
    print("评论数:",row[4])
    print("是否删除:",row[5])
print("+++++++++++++++++++++++")
cursor.close()
conn.close()