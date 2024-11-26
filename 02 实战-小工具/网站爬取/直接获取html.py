from os import name
import requests
from bs4 import BeautifulSoup
import csv

# 发送 GET 请求
url = "https://pypi.org/search/?q=p"
response = requests.get(url)

# 如果请求成功，打印网页内容的前500个字符
if response.status_code != 200:
    print("请求失败，状态码：", response.status_code)
else:
    # print(response.text)  # 打印网页前500个字符

    # 解析网页内容
    soup = BeautifulSoup(response.text, "html.parser")

    # 打印解析后的 HTML 内容（结构化）
    # print(soup.prettify()[:500])  # 打印前500个字符的结构化 HTML

    # 查找所有的名言卡片
    quotes = soup.find_all("a", class_="package-snippet")

    # 打开 CSV 文件准备写入
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["包名", "描述"])  # 写入表头

        # 提取每个名言的文本和作者
        for quote in quotes:
            name = quote.find(
                "span", class_="package-snippet__name"
            ).get_text()  # 获取名言内容
            version = quote.find(
                "span", class_="package-snippet__version"
            ).get_text()  # 获取作者
            des = quote.find(
                "p", class_="package-snippet__description"
            ).get_text()  # 获取作者
            print(f"包名：{name} {version}\n描述：{des}")
            writer.writerow([f"{name} {version}", des])  # 写入数据行

    print("数据写入完成")
