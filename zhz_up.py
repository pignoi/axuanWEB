from flask import request,render_template,redirect
import time,datetime,os

def allow_form(filename):
    filetype = filename.split('.')[-1]
    typel = ['png','jpg','jpeg','gif']
    if filetype in typel:
        return [1,filetype]
    else:
        return [0]

def zhz_upload():

    mes = request.form.get('daily')   # 接受文字
    pics = request.files.getlist('daily_pic')    # 接受图片
    mes1 = mes.split('\r\n')
    if mes1.count("") == len(mes1) and pics==[]:
        return redirect("/zhz")
    else:
        deal1 = ""
        for singleLine in mes1:
            if singleLine != "":
                deal1 += f'    <h4 class="mainfi">{singleLine}</h4>\n'
            else:
                deal1 += '    <h5 class="mainfi"></h5>\n'

        now_time = time.strftime('%Y.%m.%d %H:%M')

### 图片部分

        now_max = 1
        alrea = os.listdir('static/rec_pic')
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
                new_fname = r'static/rec_pic/' + f'{now_day}_{now_max}.{allow_form(pic.filename)[1]}'
                pic.save(new_fname)  #保存文件到指定路径
                once_pic.append(rf'rec_pic/{now_day}_{now_max}.{allow_form(pic.filename)[1]}')
                re_mes1 = '图片上传成功'
                now_max += 1
            else:
                re_mes1 = '上传图片格式出错，请重新上传'

        pic_count = len(once_pic)
        if pic_count == 0:
            pic_mes = ''
        if pic_count >= 3:
            row = 3
            pic_mes = "    <div class=pic>\n        <img src='" + f"' width={98/row}%></img>\n        <img src='".join(once_pic)+f"' width={98/row}%'></img>\n    </div>"
        if pic_count == 2: 
            row = pic_count
            pic_mes = "    <div class=pic>\n        <img src='" + f"' width={98/row}%></img>\n        <img src='".join(once_pic)+f"' width={98/row}%'></img>\n    </div>"
        if pic_count == 1: 
            row = pic_count
            pic_mes = "    <div class=pic_single>\n        <img src='" + f"' width={98/row}%></img>\n        <img src='".join(once_pic)+f"' width={98/row}%'></img>\n    </div>"
        

        deal2 = f"""
<div class="nav">
<h3 class="mainfi">{now_time}</h3>
{deal1}
{pic_mes}
</div>
<p></p>
        """

        filet = open('.inside','r+')
        already = filet.read()
        filet.seek(0,0)
        filet.write(deal2+already)

        return redirect("/zhz")

