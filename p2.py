#-*- encoding=UTF-8 -*-

from flask import Flask,render_template,request,make_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

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

if __name__ == '__main__':
    app.run(debug=True)