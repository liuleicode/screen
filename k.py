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
                url = "http://hq.sinajs.cn/list=hf_"
                urllist = [url + "OIL", url + 'CL', url + 'DINIW', url + 'USDCNY', url + 'GC', url + 'XAU']
                count = 1
                for url in urllist:
                    #    请求
                    request = urllib.request.Request(url)

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
                    param = (
                        result[13], result[0], "", "", result[1], result[8], result[4], result[5], result[7],
                        result[9],
                        result[2], result[3], result[6], count)
                    cursor.execute(sql % param)
                    connect.commit()
                    count +=1
                    print('成功修改', cursor.rowcount, '条数据')

                time.sleep(30)
        except Exception as e:
            print(e)
            cursor.close()
            connect.close()
            time.sleep(10)
