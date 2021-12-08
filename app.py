from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
from datetime import timedelta
import os

#Flaskオブジェクトの生成
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg'])

def allwed_file(filename):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
def upload_file():
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
        if file and allwed_file(file.filename):
            # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
            print('OK')
        return render_template('index.html')
    else:
    	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

