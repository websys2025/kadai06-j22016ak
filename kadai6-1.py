import requests

APP_ID = "d645fe1349e27f39ef1cc4b0281868675a455205"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

#人口統計を表示させる
params = {
    "appId": APP_ID,                     # アプリID
    "statsDataId": "0003445078",         # 統計データID（今回は国勢調査の人口データ）
    "metaGetFlg": "Y",                   # メタ情報（分類など）を取得
    "cntGetFlg": "N",                    # 件数取得は不要
    "explanationGetFlg": "Y",            # 解説文も取得する
    "annotationGetFlg": "Y",             # 注釈も取得する
    "sectionHeaderFlg": "1",             # セクションヘッダを取得
    "replaceSpChars": "0",               # 特殊文字の置き換えなし
    "lang": "J"                          # 日本語で取得
}



# APIリクエストを送信し、レスポンス（JSON）を取得
response = requests.get(API_URL, params=params)
data = response.json()

#統計の基本情報を出力
def print_info(stat_data):
    table_inf = stat_data["STATISTICAL_DATA"]["TABLE_INF"]
    print(f"統計名   : {table_inf['STAT_NAME']['$']}")
    print(f"タイトル : {table_inf['TITLE']['$']}")
    print(f"調査年月 : {table_inf['SURVEY_DATE']}")
    print(f"公開日   : {table_inf['OPEN_DATE']}")
    print()
    
#統計の解説文を出力
def print_explanation(stat_data):
    explanation = stat_data["STATISTICAL_DATA"].get("EXPLANATION")
    if explanation:
        print("解説")
        print(explanation.strip())
        print()

#データ本体（VALUE）を出力
def print_data(stat_data):
    print("データ")
    values = stat_data["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]
    for i, val in enumerate(values):
        area = val.get("@area", "不明")
        time = val.get("@time", "不明")
        cat01 = val.get("@cat01", "")
        value = val.get("$", "N/A")
        annotation = val.get("@annotation", "")
        print(f"{i+1:5}. 地域: {area}, 時点: {time}, 分類: {cat01}, 値: {value}{f'（注:{annotation}）' if annotation else ''}")
    
stat_data = data["GET_STATS_DATA"]
print_info(stat_data)
print_explanation(stat_data)
print_data(stat_data)