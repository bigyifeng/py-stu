import requests
import csv
import pandas as pd


# 目标 API 接口 URL，假设有分页
url = "https://api.promptport.ai/v1/prompt/list"


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

# # 打开 CSV 文件准备写入
# with open("ai-data.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["ID", "标题", "描述", "正文", "标签"])  # 写入表头


# 两分钟240条
