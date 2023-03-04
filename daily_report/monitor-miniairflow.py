import os

maincmd = r"/usr/bin/python3 /home/webserver/web/daily_report/miniairflow.py &"
os.system(maincmd)

pidcmd = r'ps -aux | grep "/usr/bin/python3 /home/webserver/web/daily_report/miniairflow.py"'
getre = os.popen(pidcmd,"r").read()
thepid = getre.split()[1]
with open("/home/webserver/web/static/miniairflow-server.pid","w+") as f:
    f.write(thepid)
