import flask, os, sys, time, datetime, json
from flask import request,redirect,abort
from wsgiref.simple_server import make_server

import own_html,own_up

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import cv2

def ip_user():     # 获取访问者的ip以及useragent，判断是否在ban的范围之内，如果是返回值为0，后面会禁止访问
    with open(".banned_ip") as f:
        ip_lines = f.readlines()
    ip_ban = [i.split("\n")[0] for i in ip_lines]
    agent_ban = ["python-requests","Python-urllib","Go-http-client"]

    ip_add = request.remote_addr
    user_a = request.headers.get("User-Agent")

    if (ip_add in ip_ban):
        return 0
    else:
        for single_user in agent_ban:
            if single_user in user_a:
                return 0
        return 1

def allow_f(filename):
    all_list = ['png','jpg','jpeg','docx','doc','xls','xlsx','ppt','pptx','pdf','html','py','c','zip','']
    file_type = filename.split('.')[-1]
    if file_type in all_list:
        return 1
    else:
        return 1


interface_path = os.path.dirname(__file__)
sys.path.insert(0, interface_path)
server = flask.Flask(__name__,static_url_path='',static_folder='static',template_folder='template')

#    limiter = Limiter(
#    server,
#    key_func=get_remote_address,
#    default_limits=["10 per second", "500 per hour"],
#    storage_uri="memcached://0.0.0.0:11211",
#    storage_options={})

@server.errorhandler(404)    # 重定向404界面
def demo4(e):
    # ip_toban = request.remote_addr
    # with open(".banned_ip","a+") as f:
    #     f.seek(0)
    #     alban = f.readlines()
    #     if f"{ip_toban}\n" in alban:
    #         pass
    #     else:
    #         f.seek(0)
    #         f.write(f"{ip_toban}\n")
    return "404 ERROR!"

@server.errorhandler(429)    # 短时间内访问此数过多会重定向至429界面，然后加入黑名单
def demo429(e):
    ip_toban = request.remote_addr
    with open(".banned_ip","a+") as f:
        f.seek(0)
        alban = f.readlines()
        if f"{ip_toban}\n" in alban:
            pass
        else:
            f.seek(0)
            f.write(f"{ip_toban}\n")
    return redirect("https://bing.com")

@server.route('/')
def index():
    check = ip_user()
    if check == 1:
        return flask.render_template('首页.html')
    else:
        abort(404)

@server.route('/answer')
def answer():
    check = ip_user()
    if check == 1:
        return flask.render_template('answer.html')
    else:
        abort(404)

@server.route('/calc')
def calc():
    check = ip_user()
    if check == 1:
        return flask.render_template('calc.html')
    else:
        abort(404)

@server.route("/check",methods=['get'])
def check_posi():
    ip_addr = request.remote_addr
    user_ag = request.headers.get("User-Agent")
    user_co = request.headers.get("Cookie")

    return f"""<h3>ip={ip_addr}</h3>
    <h3>User-Agent={user_ag}</h3>
    <h3>Cookie={user_co}</h3>"""

@server.route('/own',methods=['get'])
def own():
    html = own_html.own_main()
    return html

@server.route('/own/uploa',methods = ['post'])
def own_uploa():
    return own_up.own_upload()

@server.route("/weblogin", methods=["get"])
def weblogin():
    return "<h1>目前相关功能已转移至以下链接，用户信息同步转移</h1><a href='http://pan.axuan.wang'>点击链接跳转</a>"

@server.route("/pics",methods=["get"])
def pics():
    get_pic = request.args.get("name")
    
    if (request.args.get("height") != None) and request.args.get("width") != None:
        height = int(request.args.get("height"))
        width = int(request.args.get("width"))

        image = cv2.imread(f"./static/pic/立绘_{get_pic}_1.png")
        img1 = cv2.resize(image,(height,width))
        cv2.imwrite('.temp.png',img1)
        with open('.temp.png', 'rb') as f:
            fimage = f.read()
        os.remove(".temp.png")
    else:
        with open(f"./static/pic/立绘_{get_pic}_1.png", 'rb') as f:
            fimage = f.read()


    resp = flask.Response(fimage, mimetype='image/png')
    
    return resp

# @server.route("/toStudent",methods=["get"])
# def student():
#     return flask.redirect("https://www.wjx.cn/vj/OtLoos5.aspx")

# @server.route("/toDriver",methods=["get"])
# def driver():
#     return flask.redirect("https://www.wjx.cn/vj/PcvQ5iW.aspx")

# @server.route("/restart",methods=["get"])
# def restart():
    
#     os.system("/usr/bin/python3 /home/webserver/web/daily_report/monitor-miniairflow.py &")
#     return redirect("/airflow.html")

# @server.route("/subscribe",methods=["get"])
# def subscribe():
#     a, response = vpnServer.check_token()

#     return response


if __name__ == '__main__':

    # print('----------relationship----------')
    # print(server.url_map)
    # app = make_server('0.0.0.0', 80, server)
    # app.serve_forever()

    server.run('127.0.0.1',8081,debug=True)

    # @server.route('/up/<name>')
    # def up(name):
    #   return flask.redirect(flask.url_for('static',filename=f'up_update/{name}'))

    # @server.route('/pic/<name>',methods=['get'])
    # def pic(name):
    #     return flask.redirect(flask.url_for('static',filename=f'fz_pics/{name}'))
