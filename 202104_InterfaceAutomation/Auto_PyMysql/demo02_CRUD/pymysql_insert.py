import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, database="books",
                       user="root", password="root", charset="utf8",
                       autocommit=True)
cursor = conn.cursor()
# 核心:发送 SQL 语句
sql = "insert into t_book values(4, '红楼梦', '1990-10-10',500,300,0)"
cursor.execute(sql)
print("受影响的行数:", cursor.rowcount)
# 手动提交
# conn.commit()
cursor.close()
conn.close()
# 默认情况下， 新增操作不会提交到数据库， 怎么提交?
# 方案1:手动提交 conn.commit()
# 方案2:设置自动提交 创建 conn 时， 设置参数 autocommit = True (默认是 False)
