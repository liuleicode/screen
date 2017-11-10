import os
import time
while True:
    try:
        today = time.strftime('%Y%m%d',time.localtime(time.time()))
        filepath = "D:\\software\\backup\\"+today+".sql"
        if not os.path.exists(filepath) :
            os.chdir("os.chdir(")
            os.system("mysqldmump  -uroot -pXabcd1234.LL mysql orlpricedtl> "+filepath)
        time.sleep(3600)
    except Exception as e:
        print(e)
        time.sleep(300)
