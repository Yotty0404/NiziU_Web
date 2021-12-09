from flask import Flask, request, redirect, url_for, flash, render_template, send_from_directory
from werkzeug.utils import secure_filename
from datetime import timedelta
import os

#Flaskオブジェクトの生成
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    data = [[],[],[]]
    lbl = ''
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
            lbl = 'そっくり度...'
            data = [['tesuto','72.3%'],['test2','52.1%'],['test3','35.5%']]
        return render_template('index.html', lbl=lbl, data=data)
    else:
        return render_template('index.html', lbl=lbl, data=data)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/favicon.ico')
@app.route('/apple-touch-icon.png')
@app.route('/apple-touch-icon-precomposed.png')
@app.route('/icon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img/'), 'pearl_Icon.jpg')
