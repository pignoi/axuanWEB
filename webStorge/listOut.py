import os
from flask import request
import json

class upload:
    def __init__(self):
        pass
    
    def getArgs(self):
        user = request.args.get("user")
        passwd = request.args.get("passwd")
        
        userData = json.load(open("webStorge/user.json"))
        
        if user in userData.keys():
            
            if passwd == userData[user]["passwd"]:
                if userData[user]["state"] != "OK":
                    dict1 = {"Wait":"申请已提交，请等待管理员审核。", "No":"审核不通过，请重新联系管理员。"}
                    return dict1[userData[user]["state"]]
                else:
                    self.dir = userData[user]["dir"]
                    return "All right."
            else:
                return "Password is wrong."

        else:
            return "Username is wrong."
        
    def listOut(self):
        checkID = self.getArgs()
        
        if checkID == "All right.":
            surl = self.dir[7:]     # /static/^......
            
            flist = os.listdir(f"./{self.dir}")
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
        else:
            return checkID
        
    def deleteFile(self):
        filename = request.args.get("file")
        checkID = self.getArgs()
        
        if checkID == "All right.":
            surl = self.dir[7:]     # /static/^......
            os.rename(f"./static/{surl}/{filename}", f"./tmpTest/{filename}")
        else:
            return checkID
        
    