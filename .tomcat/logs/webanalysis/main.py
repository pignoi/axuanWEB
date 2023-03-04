import ip2location
import os,time
import xlwt

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('analysis')
type = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'STSong'
type.font = font
worksheet.col(0).width = 5000
worksheet.col(1).width = 10000

rec = os.listdir('fwjl')
iplist = []
for file in rec:
    ofile = open(f'fwjl/{file}')
    lines = ofile.readlines()
    for line in lines:
        ipt = line.split()[0]
        iplist.append(ipt)

ipi = []
[ipi.append(i) for i in iplist if not i in ipi]

count = 0
for ip in ipi:
    tim = iplist.count(ip)
    while True:
        loc = ip2location.ip2loc2(ip)
        if loc != 0:
            break
    worksheet.write(count,0,ip,type)
    worksheet.write(count,1,loc,type)
    worksheet.write(count,2,tim,type)
    # time.sleep(1)
    count += 1
#    print(count)
    workbook.save('analysis_oct11.xls')
