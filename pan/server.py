import flask, os, sys, time, datetime, json
from flask import request,redirect,abort
from wsgiref.simple_server import make_server

from webStorge.listOut import upload

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
        with open("static/首页.html") as f:
            return "".join(f.readlines())
    else:
        abort(404)

@server.route('/upload', methods=['get'])
def upload_ddd():
    return '<form action="/upload/do" method="post" enctype="multipart/form-data">\n<input type="file" name="img" multiple>\n<button type="submit">上传</button></form>'

@server.route('/weblogin', methods=["get"])
def login():
    with open("./webStorge/loginPage.html") as f:
        return "".join(f.readlines())

@server.route("/upload/login", methods=["POST"])
def logindo():
    user = request.form.get("user")
    passwd = request.form.get("passwd")
    
    userData = json.load(open("./webStorge/user.json"))
    
    if user in userData.keys():
        
        if passwd == userData[user]["passwd"]:
            if userData[user]["state"] != "OK":
                dict1 = {"Wait":"申请已提交，请等待管理员审核。", "No":"审核不通过，请重新联系管理员。"}
                return dict1[userData[user]["state"]]
            else:
                return f"/webstorge?user={user}&passwd={passwd}"
        else:
            return "Password is wrong."

    else:
        return "Username is wrong."
    
@server.route("/register", methods=["GET"])
def register():
    with open("./webStorge/registerPage.html") as f:
        return "".join(f.readlines())

@server.route("/upload/register", methods=["POST"])
def registerdo():
    user = request.form.get("user")
    passwd = request.form.get("passwd")
    nickname = request.form.get("nickname")
    
    userData = json.load(open("./webStorge/user.json"))
    
    if user in userData.keys():
        return "用户名重复，请重新输入。"
    else:
        userData[user] = {"passwd":passwd, "dir":f"storgeDir/{user}", "state":"Wait", "limit":"1Gb", "nickname":nickname}
        os.mkdir(f"./storgeDir/{user}")
        with open("./webStorge/user.json","w") as f:
            f.write(json.dumps(userData, indent=4,sort_keys=False, ensure_ascii=False))
        return "注册成功，请联系管理员进行审核！"
    
@server.route("/checkSize", methods=["POST"])
def checksize():
    user = request.form.get("user")
    toAdd = float(request.form.get("allsize"))
    userData = json.load(open("./webStorge/user.json"))
    userLimit = float(userData[user]["limit"].split("Gb")[0])
    userDir = userData[user]["dir"]
    
    files = os.listdir(userDir)
    fsize = toAdd
    for f in files:
        fsize += os.path.getsize(userDir +"/"+ f)
    
    if fsize/1024/1024/1024 > userLimit:
        return "储存超过上限。"
    else:
        return f"{fsize/1024/1024/1024:.2f}Gb/{userLimit:.2f}Gb"
    

@server.route('/webstorge',methods=["get"])
def webstorge():
    user = request.args.get("user")
    passwd = request.args.get("passwd")
    
    userData = json.load(open("./webStorge/user.json"))
    
    if user in userData.keys():
        
        if passwd == userData[user]["passwd"]:
            if userData[user]["state"] != "OK":
                dict1 = {"Wait":"申请已提交，请等待管理员审核。", "No":"审核不通过，请重新联系管理员。"}
                return dict1[userData[user]["state"]]
            else:
                with open("./webStorge/improve_upload.html") as f:
                    return "".join(f.readlines())
        else:
            return "Password is wrong."

    else:
        return "Username is wrong."

@server.route('/upload/do', methods=['post'])
def upload_do():
    user = request.args.get("user")
    passwd = request.args.get("passwd")
    
    userData = json.load(open("./webStorge/user.json"))
    
    if user in userData.keys():
        
        if passwd == userData[user]["passwd"]:
            dir = userData[user]["dir"]
        else:
            return "Password is wrong."

    else:
        return "Username is wrong."
    
    fname = request.files.getlist('img')
    for f in fname:
        if f and allow_f(f.filename):
            t = time.strftime('%Y%m%d_%H%M%S_')
            new_fname = rf'./{dir}/' + t + f.filename
            f.save(new_fname)
        elif f and allow_f(f.filename) == 0:
            return '不允许的上传文件格式'
        else:
            return '请上传文件'
        
    init = upload()
    return init.listOut()

@server.route("/upload/checkList", methods=["get"])
def cL():
    init = upload()
    return init.listOut()

@server.route("/upload/delete", methods=["GET","POST"])
def fD():
    init = upload()
    init.deleteFile()
    return init.listOut()

@server.route("/download", methods=["get"])
def dF():
    init = upload()
    
    return init.download()


if __name__ == '__main__':

    server.run('127.0.0.1',8083,debug=True)

