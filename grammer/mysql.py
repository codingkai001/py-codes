import pymysql

try:
    # 建立连接对象
    conn = pymysql.connect(host="localhost", user="root", passwd="fk290419", db="fksql", port=3306, charset="utf8")
except Exception as e:
    print(e)
else:
    cur = conn.cursor()  # 得到游标对象
    # cur.execute("create table student(id int(2) not NULL PRIMARY KEY auto_increment,\
    #             name VARCHAR(40), stu_num CHAR(9), sex VARCHAR (10), phone text)DEFAULT charset=utf8")
    # conn.commit()
    cur.executemany("INSERT INTO student(name, stu_num, sex, phone) VALUES (%s, %s, %s, %s)",
                    (("酷酷", "221600184", "女", "13993327164"),
                     ("谷歌", "220001605", "男", "13993363254")))
    conn.commit()
    cur.execute("SELECT * FROM student")
    lines = cur.fetchall()
    for line in lines:
        print(line)
