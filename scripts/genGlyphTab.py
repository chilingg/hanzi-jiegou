#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys

if sys.path.count(os.path.dirname(os.path.realpath(__file__))) == 0:
    sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
    import check as ch
    sys.path = sys.path[1:]
else:
    index = sys.path.index(os.path.dirname(os.path.realpath(__file__)))
    if index != 0:
        sys.path[0], sys.path[index] = sys.path[index], sys.path[0]
        import check as ch
        sys.path[0], sys.path[index] = sys.path[index], sys.path[0]
    else:
        import check as ch

def genGlyphTab(file = 'glyph.json'):

    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    ch.init()
    glyphTab = dict()

    lrSmall2 = '乚丨乙八卜匕冫厂刁丁刂刀儿二阝丩几九卩㔾丂力了七人入亻十乂讠又'
    lrSmall3 = '才叉川寸彳亍巛大凡飞干个工广弓及己巾久彐孑孓口亏么马门女丬乞千犭刃夊三上勺尸士巳扌彡饣氵纟山土乇丸万亡卫兀卂习下乡小忄夕丫也已义于与弋幺丈之子夂'
    lrSmall4 = '币卞不刅长尺丑歹斗方分夫父丰丐户火见斤今巨井开亢六仑木牜廿牛内匹片爿攴攵气欠区犬壬冗日少升手殳礻水太天韦文无五午王冘牙尹尤友予匀允夭爻元月云支止中爪专㝉曰'
    lrSmall5 = '衤钅石禾玉田白目示未立甘生米糸页羊舟虫耒耳肉足言辛圭'
    lrSmall = lrSmall2 + lrSmall3 + lrSmall4 + lrSmall5

    tbSmall1 = '一卜二冖十厶亠艹口宀三上士工山土亡小牛亼灬冃㓁爫㣺'
    tbSmall2 = '乙八匕丁儿几九㔾了七人入川大干巾久乇万兀下丫已于之子巳不木廿壬午止𣎵廾'
    tbSmall = tbSmall1 + tbSmall2

    ltSmall = '广厃又尸厂疒毛倝歹㫃才'

    ltrSmall = '门戊凡几目戉冂戌宀网戕产'

    thSmall = '癶八人入乃六廾'

    def ratioToFormat(format, comps):
        small1 = False
        small2 = False
        small3 = False
        ratio = ''
        
        if format == '左右':
            small1 = isinstance(comps[0], str) and lrSmall.count(comps[0][0])
            small2 = isinstance(comps[1], str) and lrSmall.count(comps[1][0])
            if small1 == small2:
                ratio = '(1：1)'
            elif small1:
                ratio = '(1：2)'
            elif small2:
                ratio = '(2：1)'
        elif format == '左上包围':
            ratio = '(v1：1h1：2)'
            if ltSmall.count(comps[0][0]):
                ratio = '(v1：2h1：2)'
        elif format == '左下包围':
            ratio = '(1：2)'
            if isinstance(comps[1], str) and lrSmall.count(comps[1][-1]):
                ratio = '(1：1)'
        elif format == '上下':
            if isinstance(comps[0], dict):
                if comps[0]['format'] == '左右':
                    small1 = tbSmall.count(comps[0]['components'][0]) and tbSmall.count(comps[0]['components'][1])
            else:
                small1 = tbSmall.count(comps[0][0])
            if isinstance(comps[1], dict):
                if comps[1]['format'] == '左右':
                    small2 = tbSmall.count(comps[1]['components'][0]) and tbSmall.count(comps[1]['components'][1])
            else:
                small2 = tbSmall.count(comps[1][0])
            
            if comps[0] == '一' or comps[1] == '一':
                ratio = '(0)'
            elif small1 == small2:
                ratio = '(1：1)'
            elif small1:
                ratio = '(1：2)'
            elif small2:
                ratio = '(2：1)'
        elif format == '上中下':
            small1 = isinstance(comps[0], str) and tbSmall.count(comps[0][0])
            small2 = isinstance(comps[1], str) and tbSmall.count(comps[1][0])
            small3 = isinstance(comps[2], str) and tbSmall.count(comps[2][0])

            if small1 == small2 and small2 == small3:
                ratio = '(1：1：1)'
            else:
                rn = { True: 1, False: 2 }
                ratio = '(%d：%d：%d)' % (rn[small1], rn[small2], rn[small3])
        elif format == '上三包围':
            ratio = '(v1：1h1：2)'
            if ltrSmall.count(comps[0][0]):
                ratio = '(v1：2h1：2)'
        elif format == '上半包围':
            ratio = '(1：1)'
            if thSmall.count(comps[0][0]):
                ratio = '(1：2)'
        
        return ratio

    def recursionQuery(char, format, comps, command):
        ratio = ratioToFormat(format, comps)

        for i in range(0, len(comps)):
            c = comps[i]
            if c == None:
                continue
            if isinstance(c, dict):
                recursionQuery(char, '%s%s%d%s' % (format, ratio, i, c['format']), c['components'], command)
                continue

            cmd = command
            if len(c) > 1:
                if c[1] == '>':
                    cmd = command + c[1:]
                    c = c[0]
                elif c[1] != '-':
                    raise Exception('Unexpected expression: ' + c)
            if 'source' in ch._jiegou_dict.get(c, {}):
                cmd += '>' + c
                c = ch._jiegou_dict[c]['source']

            fmt = format + ratio + str(i) + cmd
            content = glyphTab.setdefault(c, dict())
            if fmt in content:
                content[fmt] += char
            else:
                content[fmt] = char

    for char, attrs in ch._jiegou_dict.items():
        if attrs["format"] == '单体':
            glyphTab.setdefault(char, dict())['单体'] = char
        else:
            recursionQuery(char, attrs['format'], attrs['components'], '')

    def recursionQueryFormat(format, comps, command):
        ratio = ratioToFormat(format, comps)
        compFmtList = []

        for i in range(0, len(comps)):
            c = comps[i]
            if c == None:
                continue
            if isinstance(c, dict):
                compFmtList.extend(recursionQueryFormat('%s%s%d%s' % (format, ratio, i, c['format']), c['components'], command))
                continue

            cmd = command
            if len(c) > 1 and c[1] == '>':
                cmd = command + c[1:]
                c = c[0]

            compFmtList.append([c, format + ratio + str(i) + cmd])
        return compFmtList

    temp = dict()
    for comp, attr in glyphTab.items():
        for fmt, requester in attr.items():
            temp.setdefault(requester, []).append([ comp, fmt ])
    for req, attr in temp.items():
        if len(attr) > 1:
            for comp, fmt in attr:
                del glyphTab[comp][fmt]
            
            count = 0
            for c in ch._jiegou_dict[req[0]]['components']:
                if isinstance(c, dict):
                    count += len(c['components'])
                else:
                    count += 1
                    
            unNeed = '单体'
            if count != len(attr):
                unNeed = '-' + ''.join([s[0] for s in attr])
            glyphTab.setdefault(req[0], {})[unNeed] = req

    temp = set()
    for attr in glyphTab.values():
        for requester in attr.values():
            temp |= set(requester)
    if len(temp) != len(ch._jiegou_dict):
        raise Exception('Unexpected number of characters: %d - %d' % (len(temp), len(ch._jiegou_dict)))

    print('字符总数: ', len(ch._jiegou_dict))
    print('基础组件: ', len(glyphTab))
    num = 0
    for root in glyphTab.values():
        num += len(root)
    print('全部组件: ', num)

    ch.saveJson(glyphTab, file)

def genGlyphFiles(path='glyph', tabFile='glyph.json'):
    import re

    if not os.path.exists(path):
        os.mkdir(path)

    for comp, attr in ch.loadJson(tabFile).items():
        for fmt in attr.keys():
            fileName = re.sub('>', '》', os.path.join(path, '%s：%s.svg' % (comp, fmt)))
            tFile = open(fileName, "w", encoding='utf-8')
            tFile.close()

if __name__ == '__main__':
    genGlyphTab()