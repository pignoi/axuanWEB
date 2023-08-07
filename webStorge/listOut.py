import os
from flask import request
import json

def listOut():
    user = request.args.get("user")
    passwd = request.args.get("passwd")
    
    userData = json.load(open("webStorge/user.json"))
    
    if user in userData.keys():
        
        if passwd == userData[user]["passwd"]:
            dir = userData[user]["dir"]
        else:
            return "Password is wrong."

    else:
        return "Username is wrong."
    
    surl = dir[7:]     # /static/^......
    
    flist = os.listdir(f"./{dir}")
    fstr = ""
    for f in flist:
        fmes = f.split("_")
        fstr += f"""<ul><li>{'_'.join(fmes[2:])}</li><li>{fmes[0]+' '+fmes[1]}</li><li><a href=/{surl}/{f} download='{'_'.join(fmes[2:])}'>下载</a> <button type='button' id='remove' onclick="getDelete('{f}')">删除</button></ul>\n"""
    return f"""    
    
    <ul>
    <li><h3>文件名称</h3></li> <li><h3>上传时间</h3></li> <li><h3>操作</h3></li>
    </ul>
    {fstr}
    """
    
def deleteFile():
    filename = request.args.get("file")
    user = request.args.get("user")
    passwd = request.args.get("passwd")
    
    userData = json.load(open("webStorge/user.json"))
    
    if user in userData.keys():
        
        if passwd == userData[user]["passwd"]:
            dir = userData[user]["dir"]
        else:
            return "Password is wrong."

    else:
        return "Username is wrong."
    
    surl = dir[7:]     # /static/^......
    os.rename(f"./static/{surl}/{filename}", f"./tmpTest/{filename}")
    
    