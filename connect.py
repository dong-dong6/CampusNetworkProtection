import re
import requests
from bs4 import BeautifulSoup
import configparser
import HTML_parsing
import os

os.environ['http_proxy'] = ''
os.environ['https_proxy'] = ''


def extract_parameters(html):
    parameters = {}

    # Define regex patterns for each parameter
    patterns = {
        'uid': r"uid='([^']*)'",
        'v4ip': r"v4ip='([^']*)'",
        'zxopt': r"zxopt=(\d+)",
        'NID': r"NID='([^']*)'"
    }

    # Extract each parameter using the corresponding regex pattern
    for key, pattern in patterns.items():
        match = re.search(pattern, html)
        if match:
            parameters[key] = match.group(1)

    return parameters


def print_dict_line_by_line(data_dict):
    for key, value in data_dict.items():
        print(f"'{key}': '{value}'")


def check():
    get_url = "http://172.16.30.98"
    response = requests.get(get_url)
    response = BeautifulSoup(response.content, 'lxml', from_encoding='gbk')
    parameters = extract_parameters(str(response))
    if(parameters.get("zxopt")!='1'):
        print("未登录")
        return False
    print("已经登录")
    response = requests.get('http://6.ipw.cn')
    print("ipv6地址为"+response.content.decode('utf-8'))
    response = requests.get('http://4.ipw.cn')
    print("ipv4地址为"+response.content.decode('utf-8'))
    return True


def connect():
    session = requests.Session()
    #    第一步：发送GET请求获取登录页面的内容
    get_url = "http://172.16.30.98"

    get_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    response = session.get(get_url, headers=get_headers)

    # 第二步：解析响应内容以提取所需的参数
    soup = BeautifulSoup(response.content, 'lxml', from_encoding='gbk')
    # print(soup)
    response_content = response.content.decode('gbk')
    # print(soup)
    param_list = ['v46ip', 'v4serip']

    extracted_params = HTML_parsing.extract_js_variables_from_html(response_content, param_list)
    print_dict_line_by_line(extracted_params)

    # 循环这个请求，post_url =" http://172.16.30.98:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=172.16.30.98&iTermType=1&wlanuserip="+extracted_params.get("v46ip")+"&wlanacip=null&wlanacname=null&mac=00-00-00-00-00-00&ip="+extracted_params.get("v46ip")+"&enAdvert=0&queryACIP=0&jsVersion=2.4.3&loginMethod=1"

    post_url = "http://172.16.30.98:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=172.16.30.98&iTermType=1&wlanuserip=" + extracted_params.get(
        "v46ip") + "&wlanacip=null&wlanacname=null&mac=00-00-00-00-00-00&ip=" + extracted_params.get(
        "v46ip") + "&enAdvert=0&queryACIP=0&jsVersion=2.4.3&loginMethod=1"

    print("本次发送登录的post_url为"+post_url)

    # 初始化配置解析器
    config = configparser.ConfigParser()

    # 读取配置文件
    config.read('config.ini')

    # 获取配置项
    DDDDD = config['credentials']['DDDDD']
    upass = config['credentials']['upass']
    # 第三步：使用提取的参数发送POST请求
    post_data = {
        "DDDDD": DDDDD,
        "upass": upass,
        "R1": "0",
        "R2": "0",
        "R3": "0",
        "R6": "0",
        "para": "00",
        "0MKKey": "123456",
    }

    post_response = session.post(post_url, headers=get_headers, data=post_data, allow_redirects=True)
    # print(post_data.get("upass"))
    # 打印重定向后的最终URL和部分响应内容作为验证
    print("Final URL:", post_response.url)
    check()
    # print("Response content:", post_response.text[:1000])  # 打印响应内容的前1000个字符
