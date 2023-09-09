import datetime as dt

mondict = {
        "Jan":"01",
        "Feb":"02",
        "Mar":"03",
        "Apr":"04",
        "May":"05",
        "Jun":"06",
        "Jul":"07",
        "Aug":"08",
        "Sep":"09",
        "Oct":"10",
        "Nov":"11",
        "Dec":"12"
        }

sourceFile = "/home/webserver/web/logs/access.log"
with open(sourceFile,"r") as sf:
    fileLine = sf.readlines()
    newLine = [f"{i.split(r'/')[0]}/{mondict[i.split(r'/')[1]]}/{r'/'.join(i.split(r'/')[2:])}" for i in fileLine]
    dateStart = dt.datetime.strptime(newLine[0].split()[3][1:].split(":")[0],"%d/%m/%Y")
    # print(dateStart+dt.timedelta(days=1))
    dataEnd = dt.datetime.strptime(newLine[-1].split()[3][1:].split(":")[0],"%d/%m/%Y")
    print(dateStart,dataEnd)

    nowaDay = dateStart
    oneRecord = []
    for oneDay in range(len(newLine)):
        toDate = dt.datetime.strptime(newLine[oneDay].split()[3][1:].split(":")[0],"%d/%m/%Y")
        if toDate == nowaDay:
            oneRecord.append(newLine[oneDay])
        if oneDay == len(newLine)-1:
            with open(f"/home/webserver/web/records/{dt.datetime.strftime(nowaDay, '%Y-%m-%d')}.log","w+") as f:
                for i in oneRecord:
                    f.write(f"{i}")
        elif toDate != nowaDay:
            with open(f"/home/webserver/web/records/{dt.datetime.strftime(nowaDay, '%Y-%m-%d')}.log","w+") as f:
                for i in oneRecord:
                    f.write(f"{i}")
            oneRecord = [newLine[oneDay]]
            nowaDay = nowaDay + dt.timedelta(days=1)
        