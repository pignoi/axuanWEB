import random,os
from PIL import Image
import urllib.request  
import urllib.parse

six_box = []
five_box = []
four_box = []
three_box = []

sixs_source=urllib.request.urlopen(f'http://www.axuan.wang/up/six_box')
sixs_box = sixs_source.readlines()[0].split()
for i in sixs_box:
    six_box.append(i.decode('UTF-8'))

fives_source = urllib.request.urlopen(f'http://www.axuan.wang/up/five_box')
fives_up = fives_source.readlines()[0].split()
for i in fives_up:
    five_box.append(i.decode('UTF-8'))

fours_source=urllib.request.urlopen(f'http://www.axuan.wang/up/four_box')
fours_box = fours_source.readlines()[0].split()
for i in fours_box:
    four_box.append(i.decode('UTF-8'))

threes_source = urllib.request.urlopen(f'http://www.axuan.wang/up/three_box')
threes_up = threes_source.readlines()[0].split()
for i in threes_up:
    three_box.append(i.decode('UTF-8'))

'絮语'

six_ups = []
five_ups = []

six_source=urllib.request.urlopen(f'http://www.axuan.wang/up/six_up')
six_up = six_source.readlines()[0].split()
for i in six_up:
    six_ups.append(i.decode('UTF-8'))
five_source = urllib.request.urlopen(f'http://www.axuan.wang/up/five_up')
five_up = five_source.readlines()[0].split()
for i in five_up:
    five_ups.append(i.decode('UTF-8'))


six_final = []
five_final = []

for ganyuan1 in six_box:
    if ganyuan1 in six_ups:
        pass
    else:
        six_final.append(ganyuan1)

for ganyuan2 in five_box:
    if ganyuan2 in five_ups:
        pass
    else:
        five_final.append(ganyuan2)

def get_card(times,no_six):
    six_prob = 1 
    five_prob = 3
    four_prob = 11
    three_prob = 61
    box = []
    for time in range(times):
        val = random.uniform(1,101)
        if no_six < 50:
            six_baodi = 0
        else:
            six_baodi = no_six - 50
        if val >= six_prob and val <= (five_prob + 2*six_baodi):
            if val <= (six_prob + five_prob + 2*six_baodi) / 2:
                box.append(random.choice(six_ups))
            else:
                box.append(random.choice(six_final))
            no_six = 0
        elif val > five_prob + 2*six_baodi and val <= four_prob + 2*2*six_baodi/3:
            if val <= (five_prob + 2*six_baodi + four_prob + 2*2*six_baodi/3) / 2:
                box.append(random.choice(five_ups))
            else:
                box.append(random.choice(five_box))
            no_six += 1
        elif val > four_prob + 2*2*six_baodi/3 and val <= three_prob + 3*2*six_baodi/3:
            box.append(random.choice(four_box))
            no_six += 1
        elif val > (three_prob + 3*2*six_baodi/3) and val <= 101:
            box.append(random.choice(three_box))
            no_six += 1
    return box

def get_pic(each):
    utf_name = each.encode('UTF-8')
    url_name = str(utf_name).upper().split("'")[1].split('\\X')[1:]
    final_name = '%' + '%'.join(url_name)
    photo=urllib.request.urlopen(f'http://www.axuan.wang/pic/%E7%AB%8B%E7%BB%98_{final_name}_1.png')
    w=photo.read()
    f=open(f'立绘_{each}_1.png','wb')
    f.write(w)
    f.close()

a = int(input('请输入要抽取的次数：'))
b = int(input('请输入之前连续没有出六星的次数：'))

get_cards = get_card(a, b)
for gets in get_cards:
    get_pic(gets)
    im = Image.open(f'立绘_{gets}_1.png')
    if gets in four_box:
        print(f'⭐️⭐️⭐️⭐️\n{gets}')
        im.show()
        input()
    if gets in three_box:
        print(f'⭐️⭐️⭐️\n{gets}')
        im.show()
        input()
    if gets in five_box:
        print(f'⭐️⭐️⭐️⭐️⭐️\n{gets}')
        im.show()
        input()
    if gets in six_box:
        print(f'⭐️⭐️⭐️⭐️⭐️⭐️\n{gets}')
        im.show()
        input()
    os.system(f'del 立绘_{gets}_1.png')

input('按回车键退出……')
