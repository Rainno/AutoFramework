import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, database="books",
                       user="root", password="root", charset="utf8")
cursor = conn.cursor()
# 核心: 编写两条SQL语句,并执行
try:
    sql1 = "insert into t_book values(4,'西游记','1986-09-10',3000,2000,0)"
    cursor.execute(sql1)
    sql2 = "insert into t_hero values(6,'孙悟空',1,'七十二变',0,4)"
    cursor.execute(sql2)
    # 如果上述两条 SQL 语句执行正常,手动提交
    conn.commit()
except Exception as e:
    print(e)
    # 让数据操作回滚
    conn.rollback()
finally:
    cursor.close()
    conn.close()
