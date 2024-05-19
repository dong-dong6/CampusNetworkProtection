import requests
from bs4 import BeautifulSoup

import HTML_parsing
def print_dict_line_by_line(data_dict):
    for key, value in data_dict.items():
        print(f"'{key}': '{value}'")
# 第一步：发送GET请求获取登录页面的内容
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

response = requests.get(get_url, headers=get_headers)

# 第二步：解析响应内容以提取所需的参数
response_content = response.content.decode('gbk')
#print(soup)
param_list = ['v46ip', 'v4serip']

extracted_params = HTML_parsing.extract_js_variables_from_html(response_content, param_list)

# 打印提取的结果
print("提取的参数值:")
for param, value in extracted_params.items():
    print(f"{param}: {value}")