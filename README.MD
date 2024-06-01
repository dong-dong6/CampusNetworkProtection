# CUST校园网守护程序

这是一个基于Python的项目，用于自动化检查特定网站的连通性并自动进行web认证。

## 开始

以下指导将帮助你在本地机器上获取并运行该项目的副本，以便进行开发和测试。

### 预备条件

你需要安装以下软件，并提供安装方法：

- Python 3.x
- BeautifulSoup
- requests
- lxml
- configparser

你可以使用pip安装Python包：

```bash
pip install beautifulsoup4 requests lxml configparser
```

### 安装

以下是一系列步骤，告诉你如何运行开发环境：

1. 克隆仓库到你的本地机器。
2. 导航到你克隆仓库的目录。
3. 运行 `main.py` 来启动程序。

## 使用

该项目的主要功能是ping一系列网站并维持稳定的连接。如果与网站的连接失败，程序将尝试重新连接。

在 `main.py` 中定义要ping的网站列表：

```python
websites = [
    'https://baidu.com',
]
```

你可以根据需要添加或删除此列表中的网站。

## 致谢

- 感谢所有帮助改进此项目的贡献者。