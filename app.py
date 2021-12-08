from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
from datetime import timedelta
import os

#Flaskオブジェクトの生成
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    data = [[],[],[]]
# リクエストがポストかどうかの判別
    if request.method == 'POST':
        # ファイルがなかった場合の処理
        if 'face_image' not in request.files:
            print('ファイルがありません1')
        # データの取り出し
        file = request.files['face_image']
        # ファイル名がなかった時の処理
        if file.filename == '':
            print('ファイルがありません2')
        # ファイルのチェック
        if file:
            # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
            print('OK')
            data = [['tesuto','72.3%'],['test2','52.1%'],['test3','35.5%']]
        return render_template('index.html', data=data)
    else:
        return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)

