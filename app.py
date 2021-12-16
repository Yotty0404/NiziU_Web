from flask import Flask, request, redirect, url_for, flash, render_template, send_from_directory
from werkzeug.utils import secure_filename
from datetime import timedelta
import os
import numpy as np

from predict import detect_face


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
            return render_template('index.html', lbl=lbl, data=data, isImageLoadFailure=True)
        # データの取り出し
        file = request.files['face_image']
        # ファイル名がなかった時の処理
        if file.filename == '':
            print('ファイルがありません2')
            return render_template('index.html', lbl=lbl, data=data, isImageLoadFailure=True)
        # ファイルのチェック
        if file:
            print('OK')

            stream = request.files['face_image'].stream
            img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
            data = detect_face(app.root_path, img_array)

            if data == False:
                return render_template('index.html', lbl=lbl, data=[[],[],[]], isImageLoadFailure=True)

            lbl = 'そっくり度...'
        return render_template('index.html', lbl=lbl, data=data, isImageLoadFailure=False)
    else:
        return render_template('index.html', lbl=lbl, data=data, isImageLoadFailure=False)

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/favicon.ico')
@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img/'), 'logo.png')

@app.route('/apple-touch-icon-120x120-precomposed.png')
@app.route('/apple-touch-icon-120x120.png')
@app.route('/apple-touch-icon-precomposed.png')
@app.route('/apple-touch-icon.png')
@app.route('/icon.png')
def icon():
    return send_from_directory(os.path.join(app.root_path, 'static/img/'), 'logo_white.png')
