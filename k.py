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
                url = "http://hq.sinajs.cn/list="
                urllist = [[url + "hf_OIL",1], [url + 'hf_CL',2], [url + 'hf_GC',3], [url + 'hf_XAU',4], [url + 'DINIW',5], [url + 'USDCNY',6]]
                for url in urllist:
                    try:
                        #    请求
                        num = url[1]
                        request = urllib.request.Request(url[0])

                        # 爬取结果
                        response = urllib.request.urlopen(request)

                        data = response.read()

                        # 设置解码方式
                        data = data.decode('gb2312')
                        print(data)
                        # 打印结果
                        result = data.split('"')[1].split(',')
                        print(result)
                        sql = "UPDATE orlprice SET name = '%s',new_price = '%s',rmb_price ='%s',diff_price = '%s',diff_percent = '%s',open_price = '%s',high_price='%s',low_price = '%s',last_price = '%s',hold_count = '%s',buy_price = '%s',sell_price ='%s',price_time = '%s' WHERE id = %d "
                        if(num<=4):
                            param = (
                                result[13], result[0], "----", "----", result[1], result[8], result[4], result[5], result[7],
                                result[9],
                                result[2], result[3], result[6], num)
                        else:
                            param = (
                                result[9], result[8], "----", "----", "----", result[3], result[6], '----', result[5],
                                result[4],
                                result[1], result[2], result[0], num)

                        cursor.execute(sql % param)
                        connect.commit()
                        print('成功修改', cursor.rowcount, '条数据')
                    except Exception as e:
                        print(e)

                time.sleep(30)
        except Exception as e:
            print(e)
            cursor.close()
            connect.close()
            time.sleep(10)
