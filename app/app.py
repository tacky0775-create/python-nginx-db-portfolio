from flask import Flask, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    """MariaDBに接続する関数"""
    return mysql.connector.connect(
        host="db",
        user="root",
        password="password",
        database="sample_db"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # POSTリクエスト（フォーム送信）が来たらDBに書き込む
    if request.method == "POST":
        new_message = request.form.get("message")
        if new_message:
            cursor.execute("INSERT INTO greetings (message) VALUES (%s)", (new_message,))
            conn.commit()

    # DBから全メッセージを取得
    cursor.execute("SELECT message FROM greetings ORDER BY id DESC")
    messages = cursor.fetchall()

    conn.close()

    # HTMLを生成
    html = "<h1>メッセージ一覧</h1><ul>"
    for (msg,) in messages:
        html += f"<li>{msg}</li>"
    html += "</ul>"

    html += """
    <form method="POST">
        <input type="text" name="message" placeholder="新しいメッセージ">
        <button type="submit">追加</button>
    </form>
    """

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
