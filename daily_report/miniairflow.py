import time,datetime
import os

def BashOpeater(bashcmd):
    os.system(bashcmd)

while True:
    time.sleep(300)
    nowa = datetime.datetime.now()
    if nowa.hour == 9 and nowa.minute >= 0:
        BashOpeater("sh /home/wenserver/XMU-dailyreport/XMUreport.sh")
