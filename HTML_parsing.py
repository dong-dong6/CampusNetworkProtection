from bs4 import BeautifulSoup
import re

def extract_js_variables_from_html(input_string, param_list):
    # print(input_string)
    print("进行数据解析")
    """
    从输入字符串中提取指定参数的值。
    
    参数：
    -input_string：要搜索的字符串。
    -param_list：要搜索的参数名称列表。
    
    退货：
    将参数名称作为关键字，并将其相应的值作为值的字典。
    """
    # 初始化一个空字典以存储结果
    results = {}

    ## 循环浏览列表中的每个参数
    for param in param_list:
        # 创建正则表达式模式以匹配参数并提取其值
        # 该模式假设参数后面跟着一个“=”，然后是它的值，
        # 在组（.*？）中捕获的；当遇到分号或空白时，它将停止捕获。
        pattern = fr"{param}=['\"](.*?)['\"]"

        # Search for the pattern in the input string
        match = re.search(pattern, input_string)

        # If a match is found, add the parameter and its value to the results dictionary
        if match:
            results[param] = match.group(1)
    print(results)
    return results


