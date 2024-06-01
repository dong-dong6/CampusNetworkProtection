import requests
import time
import connect
import os
# # 设置不进行代理
os.environ['http_proxy'] = ''
os.environ['https_proxy'] = ''
# 定义常用网站列表
websites = [
    'https://baidu.com',
    'https://microsoft.com',
]

# 定义 ping 网站函数
def ping_website(url):
    try:
        response = requests.get(url, timeout=5)
        print(response.status_code)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"错误pinging {url}: {e}")
        return None

# 主函数
def main():
    while True:
        for website in websites:
            status_code = ping_website(website)
            if status_code:
                print(f"{website} 网站正常，状态码: {status_code}")
            else:
                if connect.check()==False:
                    connect.connect()
        time.sleep(10)

if __name__ == "__main__":
    main()
    #connect.check()
