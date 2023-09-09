import time,datetime

def own_main():
    now_show = time.strptime(time.strftime('%Y-%m-%d-%H-%M-%S'),'%Y-%m-%d-%H-%M-%S')

    now = time.strptime(time.strftime('%Y-%m-%d'),'%Y-%m-%d')
    login = f'你登入的时间是{now_show[0]}年{now_show[1]}月{now_show[2]}日{now_show[3]}时{now_show[4]}分{now_show[5]}秒'

    textf = open('./.inside_own').readlines()
    text = ''.join(textf)

    html = f"""
<html class="client-js ve-available" lang="zh-Hans-CN" dir="ltr"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style>
body{{margin: 0;}}
.nav {{ margin:0 0 0 25%;
        width:70%;
        border: 2px solid #D4CD49;}}

.input{{ margin:0 0 0 25%;
        width:70%;
        height:300px;
        border: 2px solid #D4CD49;}}

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

.mes{{
    width:100%;
    height:100%;
    position:fixed;
    z-index:80;
}}

.top{{
    margin: 0 0 0 0;
    width:100%;
    height:50px;
    position:fixed;
    border:0.5px solid #ff0;
    background:blue;
    z-index:80;
}}

.info_show {{
    margin:100px 0 0 0;
    width:15%;
    height:300px;
    float:left;
    border:2px solid #D4CD49;
    background:green;
    z-index:80;
}}

.main {{
    margin:60px 0 0 0;
    position:absolute;
    z-index:60;
}}

.title{{
    margin:0 0 0 25%;
    width:70%
}}

</style>
<head>
	<title>pignoi Blog</title>
	<link rel="icon" href="/favicon.ico" type="image/x-icon">
	<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
</head>

<body>
    <div class='top'>
        <h3>导航栏</h3>
    </div>

    <div class='info_show'>
        <h3>个人介绍区域</h3>
    </div>

    <div class="main">
        <div class="title">
            <h1 style='text-align:center;font-family:Times'> The Record of pignoi </h1>
            <h3 style='text-align:center;font-family:STSong'> {login} </h3>
        </div>

        {text}
        <div class='nav'>
            <form action="/own/uploa" method="post" enctype="multipart/form-data">
            <textarea  style="font-family:STSong;font-size:18px; width:100%" cols="80" rows="8" style="OVERFLOW:visual" name='own_daily'></textarea>
            <input type="file" name="own_daily_pic" multiple>
            <input type='submit' name='submit'>
            </form>
        </div>

        <footer>
	        <div class="end">
                <p></p>
                <a href="https://beian.miit.gov.cn/">冀ICP备2021017338号</a>
            </div>
        </footer>
</html>
    </div>

</body>


    """

    return html
