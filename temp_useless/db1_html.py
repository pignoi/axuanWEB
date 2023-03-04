import time, datetime

def db_main1():
    now_show = time.strptime(time.strftime('%Y-%m-%d-%H-%M-%S'),'%Y-%m-%d-%H-%M-%S')

    # begin = time.strptime('2021-03-19','%Y-%m-%d')
    # now = time.strptime(time.strftime('%Y-%m-%d'),'%Y-%m-%d')
    # years = now[0] - begin[0]
    # months = now[1] - begin[1]
    # days = now[2] - begin[2]
    total = (datetime.date(now[0],now[1],now[2]) - datetime.date(begin[0],begin[1],begin[2])).days
    login = f'你登入的时间是{now_show[0]}年{now_show[1]}月{now_show[2]}日{now_show[3]}时{now_show[4]}分{now_show[5]}秒'
    # rel = f'截至目前，我们在一起已经{years}年, {months}个月, {days}天, 总共{total}天'

    textf = open('./.db_inside').readlines()
    text = ''.join(textf)

    html = f"""
<html class="client-js ve-available" lang="zh-Hans-CN" dir="ltr"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style>
.nav {{ margin:0 auto;
        width:600px;
        border: 2px solid #D4CD49;}}

.input{{ margin:0 auto;
        width:600px;
        height:300px;
        border: 2px solid #D4CD49;}}

.end {{ text-align: center;
        top:100%;}}
</style>
<head>
	<title>Love Blog</title>
	<link rel="icon" href="/favicon.ico" type="image/x-icon">
	<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
</head>

<body>
	<h1 style='text-align:center'>新生赛第一轮资料</h1>
    <h3 style='text-align: center'> {login} </h3>

    {text}
    <div class='nav'>
        <form action="/zhz/uploa" method="post" enctype="multipart/form-data">
        <textarea  cols="80" rows="8" style="OVERFLOW:visual" name='daily'></textarea>
        <input type="file" name="daily_pic" multiple>
        <input type='submit' name='submit'>
        </form>
    </div>
</body>


<footer>
	<div class="end">
        <p></p>
        <a href="https://beian.miit.gov.cn/">冀ICP备2021017338号</a>
    </div>
</footer>

    """

    return html
