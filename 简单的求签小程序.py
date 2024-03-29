# -*- encoding:utf-8 -*-

"""
名称：求签啦
版本:1.1
作者：邱溪言
功能：用户输入数字，通过简单的计算求签
     加入时间戳
"""

import random
import datetime
import time

cur = datetime.datetime.now()
cm = cur.month
cd = cur.day

print('***********天灵灵，地灵灵，小邱算卦指定行，一天一卦，多了不灵啦~***********')
luckynum_str = input('请在十支签中选择一支（输入数字1~10）：')
luckynum = eval(luckynum_str)


def random_list(start, stop, length):
    if length >= 0:
        length = int(length)
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


ran_list = random_list(0, 10, 10)
rannum = ran_list[luckynum - 1]
rannumtwo = ran_list[luckynum - 2]


def compare(rannum, rannumtwo):
    if rannumtwo > rannum:
        if rannumtwo - rannum > 5:
            return '大吉'
        else:
            return '吉'
    elif rannumtwo < rannum:
        if rannum - rannumtwo > 6:
            return '末吉'
        else:
            return '半吉'
    else:
        return '头等签'


print('********************妈咪妈咪哄，算卦中...请稍候！********************')
time.sleep(1)

print(compare(rannum, rannumtwo))

print('***************************{}月{}日签文***************************'.format(cm, cd))


def pick():
    list_tdq = ['闲居山畔眺白云，昂首知我作何为。', '翘首望东天，遥望久方月。奈良春日时，三笠皎月同。', '川间育金石，顺水长漫步。天神忽降迹，欲睹此金石。',
                '久方云天宫殿间，何物美如天上星。', '藤开犹紫浪，遍满户庭间。浪涌魅人近，宿前久驻留。', '几朝年老翁，策杖花仙境。庭院除杂草，来宾香更胜。',
                '飘摇青柳丝，寄身春风里。狂风安然度，微风不折腰。', '庭前福至，种千寻竹。家门冬夏，得灵庇护。', '都鸟啼叫都城事，已知佳人何处归。',
                '岁末年将至，此龄亦增老。疾流不回首，酿酒亦更香。']
    list_dj = ['乍看春樱乍现，今朝所盼今迁。', '公道忠义在人心，苍苍翠柏禄马停。', '家业华禄达宝城，云中好箭得贵人。',
               '谷中福草永无断，万物灵气意相连。', '青鸟发啼声，芝书新振耳。苦待终成功，得享旧年盼。', '此院恰如盐灶中，晨风自来泊此湾。',
               '游龙亲临泽，河水染红叶。至今未曾闻，水中见浅影。', '青阳绿意得生机，本非霞气登天际。', '飘摇青柳丝，寄身春风里。狂风安然度，微风不折腰。',
               '除旧迎新石中宝，云外枯木逢春开。']
    list_j = ['闲居山畔眺白云，昂首知我作何为。', '翘首望东天，遥望久方月。奈良春日时，三笠皎月同。', '神灵作御杖，精雕木与银。神气蕴其间，千里得轻越。',
              '岁末年将至，此龄亦增老。疾流不回首，酿酒亦更香。', '川间育金石，顺水长漫步。天神忽降迹，欲睹此金石。',
              '山中红叶犹可见，前程美景在暗中。', '人间冥界均无事，难得一日可清闲。', '是非难辨，凡事宜忍。', '闲适如春樱，清净如秋水。',
              '时光如轮转，时运今再来。']
    list_bj = ['默念口中咒，所言非所思。', '吾身如浮萍，不敢言再会，幸得天眷顾，得挚友两三。', '应慎言，应慎行。',
               '天命如露滴，如幻更似虚，相逢若相知，逝去也足矣。', '胸中虽怀难言处，幸得有人问苦衷。', '沉浮尘世间，不必徒自添烦恼。',
               '诸事虽无常，自有潇洒意。', '春樱虽随风飘散，仍有余香风转廊。', '天上悬明月，清辉照万方，浮云随暂避，终不灭清光。',
               '身愿随心，对明月，有圆缺。']
    list_mj = ['是生灭法，多加小心。', '莫仿飞蛾事，徒然扑夜灯，阴阳自有道，相顺不相违。', '山火烧不尽，何人困烟熏。心念追何事，当随小溪行。',
               '红叶染衣袖，无根亦无痕。随潮打浪去，汐平在今宵。', '草木秋日褪绿意，大海白浪沫不改。', '鸟踏龙胆，庭院花散。至于野原，何不逍遥。',
               '阳间琵琶阴司鼓，阴阳相伴奏人心。', '袅袅青烟破山行，远近路人皆称奇。', '年年共赏百花盛，常恨此景太匆匆。',
               '蟋蟀唧唧人自咏，秋夜寥寥思未尽。']
    dict_suan = {"头等签": list_tdq, "大吉": list_dj, "吉": list_j, "半吉": list_bj, "末吉": list_mj }
    print(dict_suan[compare(rannum, rannumtwo)][rannum - 1])


pick()

input()
