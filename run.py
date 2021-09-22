# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, render_template
from portal_wrapper import *
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
async def root():
    return render_template('index.html')

@app.route('/api.json', methods=['POST'])
async def api():
    user_id = request.form.get('user_id', '')
    password = request.form.get('password', '')
    full = 'full' in request.form
    
    top_page = TopPage(user_id, password)
    board = Billboard(top_page)
    if full:
        board = FullBillBoard(board)
    body = list(board.post_iter())
    data = {
        'userId': user_id,
        'timestamp': datetime.now().timestamp(),
        'body': body
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)