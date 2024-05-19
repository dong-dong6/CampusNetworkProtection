import requests

# 目标URL
url = 'http://172.16.30.98/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
# 发起GET请求
response = requests.get(url,headers=headers)

# 检查是否有Cookies
if response.cookies:
    for cookie in response.cookies:
        print(f"Cookie Name: {cookie.name}, Value: {cookie.value}")
else:
    print("No Cookies returned")

# 打印状态码和响应体的前100个字符作为示例
print(f"Status Code: {response.status_code}")
print(f"Response Body Sample: {response.text[:10000]}")
