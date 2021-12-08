
# 获取连接
from demo04_utils.pymysql_dbutils import MyDBUtil

conn = MyDBUtil.getConn()
cursor = MyDBUtil.getCursor(conn)
print(conn)
print(cursor)
# 核心：sql语句
sql = "select * from t_book"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)

# 资源释放
MyDBUtil.closeResource(cursor,conn)