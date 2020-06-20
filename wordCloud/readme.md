# WordCloud

- connpassのニックネームを入力すると、参加したconnpassのイベントと主催者名から、ワードクラウドを生成するWebアプリです。
- PyDataFukuokaのハンズオンに触発されて作成しました。 https://pydatafukuoka.connpass.com/event/176637/

## 使用したPythonライブラリ

- ワードクラウド生成：word_cloud https://github.com/amueller/word_cloud
- 形態素解析：Janome https://mocobeta.github.io/janome/en/
- Webフレームワーク：Dash https://plotly.com/dash/

## Dashでワードクラウド作成する際に参考にしました。

- https://stackoverflow.com/questions/58907867/how-to-show-wordcloud-image-on-dash-web-application
