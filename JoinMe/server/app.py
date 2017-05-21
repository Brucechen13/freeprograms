import time,random,json
from flask import Flask, render_template,make_response, Response,request,jsonify
import pymysql


app = Flask(__name__)
app.debug = True

# 创建连接
def conMysql():
    conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', passwd='123456', db='test', charset='utf8')
    print(conn)
    

def savePic(picData):
    fileName = ('static/%d-%d.jpg' % (time.time(), random.randint(100,999)))
    print(fileName)
    with open(fileName, 'wb') as f:
        f.write(picData)

@app.route('/showpic')
def showPic():
    with open("static/IMG_20161231_153230.jpg", 'rb') as f:
        data = f.read()
        return Response(data,mimetype='image/jpeg')

@app.route('/user/setting')
def showSetting():
    data = {
    'hello'  : 'world',
        'number' : 3
}
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/user/getuser')
def getUserInfo():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'

@app.route('/user/register')
def registerUser():
    if findUser(request.args.get('phonenumber')):
        return "already used"
    return "register success"

@app.route('/activity/getall'):
    if userid in users:
        users = {'1':'john', '2':'steve', '3':'bill'}
        return jsonify({userid:users[userid]})
    else:
        return not_found() 

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(port=8888)
