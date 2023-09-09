import os
from flask import request,send_from_directory, make_response
from urllib.parse import quote
import json

class upload:
    def __init__(self):
        pass
    
    def getArgs(self):
        user = request.args.get("user")
        passwd = request.args.get("passwd")
        
        if user == None or passwd == None:
            user = request.form.get("user")
            passwd = request.form.get("passwd")
        
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
            
            flist = os.listdir(f"./{self.dir}")
            fstr = ""
            for f in flist:
                fmes = f.split("_")
                dateinfo = fmes[0][0:4] + "年" + fmes[0][4:6] + "月" + fmes[0][6:8] + "日&emsp;"+fmes[1][0:2]+":"+fmes[1][2:4]+":"+fmes[1][4:6]
                
                sizeinfo = os.path.getsize(f"./{self.dir}/{f}")
                if sizeinfo > 1024*1024*1024:
                    ssize = f"{sizeinfo/(1024*1024*1024):.2f} Gb"
                elif sizeinfo > 1024*1024:
                    ssize = f"{sizeinfo/(1024*1024):.2f} Mb"
                elif sizeinfo > 1024:
                    ssize = f"{sizeinfo/(1024):.2f} Kb"
                else:
                    ssize = f"{sizeinfo:.2f} b"
                fstr += f"""<ul><li>{'_'.join(fmes[2:])}</li><li>{dateinfo}</li><li>{ssize}</li><li><button type='button' id='download' onclick="download_files('{f}')">下载</button> <button type='button' id='remove' onclick="getDelete('{f}')">删除</button></ul>\n"""
            
            return f"""    
            
            <ul>
            <li><h3>文件名称</h3></li> <li><h3>上传时间</h3></li> <li><h3>文件大小</h3></li> <li><h3>操作</h3></li>
            </ul>
            {fstr}
            """
        else:
            return checkID
        
    def deleteFile(self):
        filename = request.args.get("file")
        checkID = self.getArgs()
        
        if checkID == "All right.":
            os.rename(f"./{self.dir}/{filename}", f"./tmpTest/{filename}")
        else:
            return checkID
        
    def download(self):
        filename = request.args.get("filename")
        checkID = self.getArgs()
        
        if checkID == "All right.":
            response = make_response(send_from_directory(f"./{self.dir}", filename, as_attachment=True))
            response.headers["Content-Disposition"] = "attachment;filename*=utf-8''{}".format(quote("_".join(filename.split("_")[2:])))
            response.headers["Content-Type"] = "application/octet-stream; charset=UTF-8"
            return response
        else:
            return checkID
        
    