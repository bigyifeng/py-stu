Python：爬取网页数据

一般爬取的数据分为两种

1. 网页数据
2. 接口数据

### 网页数据

1. 模拟加载 html 并解析
2. 找到对应数据的 dom 元素
3. 将数据存起来，写入到磁盘

> 示例：使用 requests + BeautifulSoup，输出 csv 文件

```python
from os import name
import requests
from bs4 import BeautifulSoup
import csv

# 发送 GET 请求
url = "https://xxxx.html"
response = requests.get(url)

if response.status_code != 200:
    print("请求失败，状态码：", response.status_code)
else:
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

```

### 接口数据

1. 发送请求获取数据
2. 分析数据
3. 将数据存起来，写入到磁盘

> 示例：使用 requests + pandas，输出 xlsx 文件

```python
import requests
import pandas as pd


# 目标 API 接口 URL，假设有分页
url = "https://api.xxx.com/v1/prompt/list"


data_arr = []
for page in range(20):
    # 设置请求参数，包含分页信息
    params = {
        "page": page,
        "size": 12,
        "sort": {"view": -1},
        "topics": [],
        "type": "or",
        "collect": 0,
        "prompt": "",
    }

    # 发送 GET 请求
    response = requests.post(url, json=params)

    # 如果请求成功
    if response.status_code == 200:
        data = response.json()

        # 如果数据为空，说明没有更多数据，停止循环
        if not data:
            break

        for post in data["data"]:
            tags = ",".join(post["topics"])
            data_arr.append(
                [
                    post["_id"],
                    (post.get("zh", post["origin"])).get("title", ""),
                    (post.get("zh", post["origin"])).get("description", ""),
                    (post.get("zh", post["origin"])).get("prompt", ""),
                    tags,
                ]
            )

    else:
        print(f"请求失败，状态码：{response.status_code}")
        break

# 将数据转换为 pandas DataFrame
df = pd.DataFrame(data_arr, columns=["ID", "标题", "描述", "正文", "标签"])

# 保存到 Excel 文件
df.to_excel("ai-data.xlsx", index=False, engine="openpyxl")

print("爬取的数据已保存到 'ai-data.xlsx'")
```
