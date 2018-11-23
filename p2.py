#-*- encoding=UTF-8 -*-

from flask import Flask,render_template,request,make_response,redirect,flash,get_flashed_messages
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
app.secret_key = 'now'

@app.route('/')
def index():
    res = ''
    for msg, cate in get_flashed_messages(with_categories=True):
        res = res + cate + msg + '<br>'
    res += 'hello'
    return res

@app.route('/w/<uid>/')
def w(uid):
    color = ('red', 'blue')
    return render_template("profile.html", uid=uid, color=color)

@app.route('/request')
def request_demo():
    res = request.args.get('key', 'defaultkey') + '<br>'
    res += request.url + request.path
    for property in dir(request):
        res = res + str(property) + str(eval('request.' + property)) + '<br>'
    response = make_response(res)
    response.set_cookie('haha')
    response.status = '404'
    res += '**********************************************************<br>'

    for property in dir(response):
        res = res + str(property) + str(eval('response.' + property)) + '<br>'
    return res

@app.route('/newpath')
def newPath():
    return 'newpath'

@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath', code=code)

@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('not_found.html', url=request.url), 404

@app.errorhandler(400)
def exception_page(error):
    return 'exception'

@app.route('/admin')
def admin():
    key = request.args.get('key')
    if key == 'admin':
        return 'hello admin'
    else:
        raise Exception()


@app.route('/login')
def login():
    app.logger.info('log success')
    flash('success', 'info')
    return 'ok'

@app.route('/log/<level>/<msg>')
def log(level, msg):
    dict = {'warn':logging.WARN, 'error':logging.ERROR, 'info':logging.INFO}
    if level in dict.keys():
        app.logger.log(dict[level], msg)
    return 'logged:' + msg

def set_logger():
    info_file_handler = RotatingFileHandler('E:\\logs\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('E:\\logs\\warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('E:\\logs\\error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)

if __name__ == '__main__':
    set_logger()
    app.run(debug=True)