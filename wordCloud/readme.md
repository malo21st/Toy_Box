# WordCloud

- connpassのニックネームを入力すると、参加したconnpassのイベントと主催者名から、ワードクラウドを生成するWebアプリです。
- PyDataFukuokaのハンズオンに触発されて作成しました。 https://pydatafukuoka.connpass.com/event/176637/

## 使い方

- 環境は、各自で頑張って構築してください。
- ターミナルから　python app.py で、Webアプリ起動。
- ブラウザを起動して　http://localhost:8050/　にアクセス。
- 停止は、 Ctrl + c

## ファイル構成

- app.py　WebフレームワークDashで作成したWebアプリ本体
- connpass_api.py　connpassのAPIで、参加イベントからキーワードと頻度を取得
- ipag.ttf　日本語を表示するための日本語フォント

## 使用したPythonライブラリ

- ワードクラウド生成：word_cloud https://github.com/amueller/word_cloud
- 形態素解析：Janome https://mocobeta.github.io/janome/en/
- Webフレームワーク：Dash https://plotly.com/dash/

## Dashでワードクラウド作成する際に参考にしました。

- https://stackoverflow.com/questions/58907867/how-to-show-wordcloud-image-on-dash-web-application
