# Game RankingAPI

- users
- scores

# objective

・ゲームのAPIサーバを想定
・ランキングとして使うスコアを登録する
・ランキングを表示するためのデータを取得する
・ランキングに保存するデータ
ユーザ名
スコア(整数値)
達成日時

# specification

python, Django REST Framework, Mysql, Docker

# Usage

`python manage.py runserver 0:5000`

user[GET, POST, PUT, DELETE]
`http://localhost:5000/users/`

score[GET, POST, PUT, DELETE]
`http://localhost:5000/scores/`


