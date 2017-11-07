import urllib.request
import time
import pymysql.cursors

if __name__ == "__main__":
    while True:
        try:
            # 连接数据库
            connect = pymysql.Connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='Xabcd1234.LL',
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
                print(data)
                # 打印结果
                # print(data)
                result1 = data.split('"')[1].split(',')
                print(result1)

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
                result2 = data2.split('"')[1].split(',')
                print(result2)

                sql = "UPDATE orlprice SET name = '%s',new_price = '%s',rmb_price ='%s',diff_price = '%s',diff_percent = '%s',open_price = '%s',high_price='%s',low_price = '%s',last_price = '%s',hold_count = '%s',buy_price = '%s',sell_price ='%s',price_time = '%s' WHERE id = %d "
                data1 = (
                    result2[13], result2[0], "", "", result2[1], result2[8], result2[4], result2[5], result2[7],
                    result2[9],
                    result2[2], result2[3], result2[6], 1)
                data2 = (
                    result1[13], result1[0], "", "", result1[1], result1[8], result1[4], result1[5], result1[7],
                    result1[9],
                    result1[2], result1[3], result1[6], 2)

                cursor.execute(sql % data1)
                cursor.execute(sql % data2)

                connect.commit()
                print('成功修改', cursor.rowcount, '条数据')

                connect.commit()
                time.sleep(30)
        except Exception as e:
            print(e)
            time.sleep(10)
