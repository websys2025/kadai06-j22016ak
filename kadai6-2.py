import requests
import pandas as pd

#神奈川県のデータセットを検索するAPI
# APIのURL（統計に関するデータセットを検索）
API_URL = "https://catalog.opendata.pref.kanagawa.jp/api/3/action/package_search"

# クエリパラメータ
params = {
    "q": "統計",    # 検索キーワード
    "rows": 100      # 取得件数（必要に応じて増減）
}

# APIリクエスト送信
response = requests.get(API_URL, params=params)
data = response.json()

# データセット情報を抽出
results = data["result"]["results"]

# 必要な情報だけをリスト化
datasets = []
for item in results:
    datasets.append({
        "title": item.get("title"),
        "name": item.get("name"),
        "organization": item.get("organization", {}).get("title", "N/A"),
        "url": f"https://catalog.opendata.pref.kanagawa.jp/dataset/{item.get('name')}"
    })

# pandasで表形式に
df = pd.DataFrame(datasets)

# 表示
print(df.head())
