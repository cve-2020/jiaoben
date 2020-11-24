import socket
import time
import threading

# 尝试通过获得banner来得到端口服务的服务版本
# def getBanner(ip, port):
#     socket.setdefaulttimeout(2)
#     s = socket.socket()
#     try:
#         s.connect((ip, port))
#         result = s.recv(1024)
#         s.close()
#         print(result)
#     except:
#         pass


def scanner_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    getport = s.connect_ex((ip, port))
    if getport == 0:
        lock.acquire()
        print("%s：%d端口开放" % (ip, port))
        lock.release()
    s.close()
    time.sleep(2)


def scan(url):
    print("——————开始扫描——————")
    for i in range(0, 65534):
        getport = threading.Thread(target=scanner_port, args=(url, int(i)))
        getport.start()
    print("————扫描端口完成————")


if __name__ == '__main__':
    url = input("输入想检测的url或者是ip:")
    lock = threading.Lock()
    scan(url)
