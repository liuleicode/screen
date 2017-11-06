import urllib.request
import time
import pymysql.cursors

if __name__ == "__main__":
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='oracle',
        db='mysql',
        charset='utf8'
    )

    # 获取游标
    cursor = connect.cursor()
    while (True):
        # 网址
        url = "http://hq.sinajs.cn/list=hf_OIL"

        # 请求
        request = urllib.request.Request(url)

        # 爬取结果
        response = urllib.request.urlopen(request)

        data = response.read()

        # 设置解码方式
        data = data.decode('gb2312')

        # 打印结果
        # print(data)
        print(data.split('"')[1].split(','))


        # 网址
        url2 = "http://hq.sinajs.cn/list=hf_CL"

        # 请求
        request2 = urllib.request.Request(url2)

        # 爬取结果
        response2 = urllib.request.urlopen(request2)

        data2 = response2.read()

        # 设置解码方式
        data2 = data2.decode('gb2312')

        # 打印结果
        # print(data2)
        print(data2.split('"')[1].split(','))

        sql = "UPDATE testpy SET name = '%s' WHERE id = %d "
        data = ('adsfads', 1)
        cursor.execute(sql % data)

        if cursor.rowcount == 0:
            sql = "insert into  testpy (name)values( '%s'  ) "
            data = ('adsfads')
            cursor.execute(sql % data)
        connect.commit()
        print('成功修改', cursor.rowcount, '条数据')

        connect.commit()
        time.sleep(30)
