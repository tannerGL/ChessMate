# Flask Server for Web Application
# @Author Tanner Lindsay
# 11/26/2022

import sqlite3
import db.chess_mate_data_base_handler as cmdb
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from stockfish.stockfish import Stockfish

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tbuhquw98kd7hda0kdk2hbtrq2j4k3l2p1h5th9q'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')


@app.route('/process_creation', methods=['POST'])
def process_creation():
    args = request.form
    user = args.get('username')
    email = args.get('email')
    password = args.get('password')

    handler = cmdb.DBHandler()

    signal = handler.create_account(user, email, password)

    if False in signal:
        return 'False'
    return 'True'


@app.route('/login')
def login():
    args = request.args
    user = args.get('username')
    password = args.get('password')


    if None not in (user, password):
        return render_template('index.html')

    return render_template('login.html')



@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/move/<current_fen>/<move>')
def stockfish_query_move(current_fen, move):
    stockfish_engine = Stockfish()

    fen, status = stockfish_engine.check_move_and_get_fen(current_fen, move)

    if status > 0:
        score_or_bad_move = stockfish_engine.analyse_position()
    else:
        score_or_bad_move = "ILLEGAL OR INVALID MOVE"
    
    return (fen, score_or_bad_move)

# @app.route('/create', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']

#         if not title:
#             flash('Title is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
#                          (title, content))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))

#     return render_template('create.html')

# @app.route('/<int:id>/edit', methods=('GET', 'POST'))
# def edit(id):
#     post = get_post(id)

#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']

#         if not title:
#             flash('Title is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('UPDATE posts SET title = ?, content = ?'
#                          ' WHERE id = ?',
#                          (title, content, id))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))

#     return render_template('edit.html', post=post)

# @app.route('/<int:id>/delete', methods=('POST',))
# def delete(id):
#     post = get_post(id)
#     conn = get_db_connection()
#     conn.execute('DELETE FROM posts WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
#     flash('"{}" was successfully deleted!'.format(post['title']))
#     return redirect(url_for('index'))