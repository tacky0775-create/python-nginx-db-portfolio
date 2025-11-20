📌 プロジェクト名
Python + Flask + NGINX + Docker + MariaDB Web アプリ


📖 概要
Docker Compose を使ってFlask (Python)、NGINX、MariaDB
の3コンテナ構成の Web アプリを構築するプロジェクトです。
ブラウザからアクセスすると、DB に保存されたメッセージを表示します。


🚀 使用技術
Python 3
Flask
NGINX
MariaDB 10.11
Docker / Docker Compose
Git / GitHub


📂 ディレクトリ構成（例）
python-nginx-db-portfolio/
│── app/
│   ├── app.py
│   └── Dockerfile
│── nginx/
│   └── default.conf
│── db/（※.gitignore 対象）
│── docker-compose.yml
│── README.md


🏃 コンテナの起動方法
1. Docker Compose で立ち上げる
docker compose up -d

2. ブラウザにアクセス
http://localhost


🛠️ データベースの作成（初回のみ）
docker exec -it mariadb mysql -u root -p

パスワード：password

DB内でテーブル作成：

USE sample_db;

CREATE TABLE greetings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255)
);

INSERT INTO greetings (message)
VALUES ("Hello from MariaDB!");


📦 コンテナの停止
docker compose down


📜 ライセンス
This project is released under the MIT License.
