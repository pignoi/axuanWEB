import time, datetime

def zhz_main():
    now_show = time.strptime(time.strftime('%Y-%m-%d-%H-%M-%S'),'%Y-%m-%d-%H-%M-%S')

    begin = time.strptime('2021-03-19','%Y-%m-%d')
    now = time.strptime(time.strftime('%Y-%m-%d'),'%Y-%m-%d')
    years = now[0] - begin[0]
    months = now[1] - begin[1] 
    days = now[2] - begin[2]
    if days < 0:
        days = 31 + days
        months = months - 1
    if months < 0:
        months = 12 + months
        years = years - 1
    total = (datetime.date(now[0],now[1],now[2]) - datetime.date(begin[0],begin[1],begin[2])).days
    login = f'你访问的时间是{now_show[0]}年{now_show[1]}月{now_show[2]}日{now_show[3]}时{now_show[4]}分{now_show[5]}秒'
    rel = f'截至访问时间，我们在一起已经{years}年, {months}个月, {days+1}天, 总共{total}天'

    textf = open('./.inside').readlines()
    text = ''.join(textf)

    html = f"""
<html class="client-js ve-available" lang="zh-Hans-CN" dir="ltr"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style>
.nav {{ margin:0 auto;
        width:80%;
        border: 2px solid #6495ED;}}

.blank {{
        width:100%;
        height:200px;
        margin:0;
}}

.fixInput {{
        background:#E6E6FA;
        width:80%;
        height:200px;
        border: 2px solid #191970;
        position:fixed;
        bottom:0;
        left:0;right:0;
        margin:auto;}}        

.end {{ text-align: center;
        top:100%;}}

.mainfi {{
    font-family:STSong,"宋体",SimSun,Times;
    line-height:150%}}

.pic {{ margin:0 10% 10px 10%;
        width:80% 
}}
.pic_single {{ margin:0 20% 10px 20%;
        width:60% 
}}
</style>
<head>
	<title>Love Blog</title>
	<link rel="icon" href="/favicon.ico" type="image/x-icon">
	<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
</head>

<body>
	<h1 style='text-align:center;font-family:Times'> The Record of CXWang and HZZhang's Love </h1>
    <h3 style='text-align: center;font-family:STSong'> {login} </h3>
    <h3 style='text-align: center;font-family:STSong'> {rel} </h3>

    <div class='fixInput'>
        <form action="/zhz/uploa" method="post" enctype="multipart/form-data">
        <textarea  style="font-family:STSong;font-size:16px; width:100%" cols="80" rows="8" style="OVERFLOW:visual" name='daily'></textarea>
        <input type="file" name="daily_pic" multiple>
        <input type='submit' name='submit'>
        </form>
    </div>

    {text}
    <div class="blank"><div>
</body>


<footer>
	<div class="end">
        <p></p>
        <a href="https://beian.miit.gov.cn/">冀ICP备2021017338号</a>
    </div>
</footer>

    """

    return html
