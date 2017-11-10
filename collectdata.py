import time
import pymysql.cursors

if __name__=="__main__":
    while True:
        try:
            connect = pymysql.Connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='Xabcd1234.LL',
                db='mysql',
                charset='utf8'
            )
            cur = connect.cursor()
            cur2 = connect.cursor()

            cur.execute("select id,name,open_price,last_price,today from orlprice")
            while True:
                data = cur.fetchone()
                if data == None: break
                cur2.execute(
                    "select id,name,open_price,last_price,today from orlpricedtl where id = %d and today = %s")
                if None == cur2.fetchone():
                    cur2.execute("insert into orlpricedtl values(%d,%s,%s,%s,%s)" % data)

            connect.commit()
            cur2.close()
            cur.close()
            connect.close()
            time.sleep(36000)

        except Exception as e:
            print (e)
            connect.commit()
            cur2.close()
            cur.close()
            connect.close()
            time.sleep(600)


        # 创建数据表
        # cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

        # 插入一条数据
        # cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


        # 修改查询条件的数据
        # cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

        # 删除查询条件的数据
        # cur.execute("delete from student where age='9'")


