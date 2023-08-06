import os
from flask import request

def listOut():
    flist = os.listdir("./static/up_files")
    fstr = ""
    for f in flist:
        fmes = f.split("_")
        fstr += f"""<ul><li>{'_'.join(fmes[2:])}</li><li>{fmes[0]+' '+fmes[1]}</li><li><a href=http://new.axuan.wang/up_files/{f} download='{'_'.join(fmes[2:])}'>下载</a> <button type='button' id='remove' onclick="getDelete('{f}')">删除</button></ul>\n"""
    return f"""    
    
    <ul>
    <li><h3>文件名称</h3></li> <li><h3>上传时间</h3></li> <li><h3>操作</h3></li>
    </ul>
    {fstr}
    """
    
def deleteFile():
    filename = request.args.get("file")
    os.rename(f"./static/up_files/{filename}", f"./tmpTest/{filename}")
    
    