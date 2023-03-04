from flask import request
import time,datetime,os

def allow_form(filename):
    filetype = filename.split('.')[-1]
    typel = ['png','jpg','jpeg','docx','doc','xls','xlsx','ppt','pptx','pdf','html','py','c','zip']
    if filetype in typel:
        return [1,filetype]
    else:
        return [0]

def db1_upload():

    mes = request.form.get('daily')
    mes1 = mes.split('\r\n')
    deal1 = '    <h4>'+'</h4>\n    <h4>'.join(mes1)+'</h4>'

    now_time = time.strftime('%Y.%m.%d %H:%M')

    pics = request.files.getlist('daily_pic')

    now_max = 1
    alrea = os.listdir('/web/static/rec_pic')
    now_day = time.strftime('%Y%m%d')
    day_count = []
    for day_pic in alrea:
        if now_day in day_pic:
            count = eval(day_pic.split('_')[1].split('.')[0])
            day_count.append(count)
    if day_count != []:
        now_max = max(day_count) + 1
    else:
        now_max = 1

    once_pic = []
    for pic in pics:
        if pic and allow_form(pic.filename)[0] == 1:
            new_fname = r'/web/static/db1/' + f'{now_day}_{now_max}.{allow_form(pic.filename)[1]}'
            pic.save(new_fname)  #保存文件到指定路径
            once_pic.append(rf'/db1/{now_day}_{now_max}.{allow_form(pic.filename)[1]}')
            now_max += 1
        else:
            re_mes1 = '上传图片格式出错，请重新上传'

    # pic_count = len(once_pic)
    # if pic_count == 0:
    #     pic_mes = ''
    # if pic_count > 3:
    #     row = 3
    #     pic_mes = "    <img src='" + f"' width='{592/row}px'></img>\n    <img src='".join(once_pic)+f"' width='{592/row}px'></img>"
    # if pic_count == 1 or pic_count == 2: 
    #     row = pic_count
    #     pic_mes = "    <img src='" + f"' width='{592/row}px'></img>\n    <img src='".join(once_pic)+f"' width='{592/row}px'></img>"

    fil_link = """    <li><a href='+"/up/mac_photoshop.dmg" download="mac_photoshop.dmg">MAPSD</a></li>"""
    "    <li><a href='" + f"' width='{592/row}px'></img>\n    <img src='".join(once_pic)+f"' width='{592/row}px'></img>"
    

    deal2 = f"""
<div class="nav">
<h3>{now_time}</h3>
{deal1}
{pic_mes}
</div>
<p></p>
    """

    filet = open('.inside','r+')
    already = filet.read()
    filet.seek(0,0)
    filet.write(deal2+already)

    ok_html = """
<html class="client-js ve-available" lang="zh-Hans-CN" dir="ltr"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style>
.nav {{ margin:0 auto;
        width:600px;
        border: 2px solid #D4CD49;}}

.input{{ margin:0 auto;
        width:600px;
        height:300px;
        border: 2px solid #D4CD49;}}
<head>
	<title>Welcome to cxHOME!</title>
	<link rel="icon" href="/favicon.ico" type="image/x-icon">
	<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">

</head>

<body>
    <h2>上传成功，五秒后返回主界面</h2>
</body>

<footer>
	<div class="end">
        <p></p>
        <a href="https://beian.miit.gov.cn/">冀ICP备2021017338号</a>
    </div>
</footer>

    """

    return '上传成功'
