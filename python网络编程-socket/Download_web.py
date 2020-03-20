'''
使用socket下载新浪网页
'''
import socket

class Download_web(object):
    '''
    基于socket的网页下载应用
    '''
    def __init__(self):
        pass
    
    def download_web_to(self,website,filepath_name):
    # 下载网页到指定位置
        # 创建一个socket
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            # 建立连接
            s.connect((website,80))
            # 发送数据
            s.send(str.encode('GET / HTTP/1.1\r\nHost: '+website+'\r\nConnection: close\r\n\r\n'))

            # 接受数据
            buffer = []
            while True:
                # 每次最多接受1K字节
                d = s.recv(1024)
                if d :
                    buffer.append(d)
                else:
                    break
            data = b''.join(buffer)

            # 写入文件
            header, html = data.split(b'\r\n\r\n',1)
            print(header.decode('utf-8'))
            # 写入指定文件
            with open(filepath_name,'wb') as f:
                f.write(html)
        
def test_download_web():

    download_sina = Download_web()

    download_sina.download_web_to("www.sina.com.cn","./sina.html")