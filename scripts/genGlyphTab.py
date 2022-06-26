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

    lrSmall2 = '乚丨乙卜匕冫厂刁丁刂刀儿二阝丩几九卩㔾丂力了七人入亻十乂讠又'
    lrSmall3 = '才叉川寸彳亍巛大凡飞干个工广弓及己巾久彐孑孓口亏么马门女丬乞千犭刃夊三上勺尸士巳扌彡饣氵纟山土乇丸万亡卫兀卂习下乡小忄夕丫也已义于与弋幺丈之子夂厶失'
    lrSmall4 = '币卞不长尺丑歹斗方分夫父丰丐户火见斤井开亢六仑木牜廿牛内匹片爿攴攵气欠区犬壬冗日少升手殳礻水太天韦文无五午王冘牙尹尤友予允夭爻元月云支止中专曰贝车半宁屯𠂤'
    lrSmall5 = '衤钅石禾玉田白目示未立甘生米糸页羊舟虫耒耳肉足言辛圭舌享古求交正革巴邑百豸关矢鸟乌骨皀毛冎丘吕戈且旦豆缶龺占𢇍㕣匚夬市节釆'
    lrSmall = lrSmall2 + lrSmall3 + lrSmall4 + lrSmall5
    lrSmalls = [ '归-彐', '印-卩', '新-斤', '段-殳', '敢-攵' ]

    tbZero = '一冖亠宀丿艹㓁爫⺮罒人卜山'
    bZero = '一灬'
    tbSmall1 = '二厶十卜口三上士工土亡小少牛亼冃㣺心𠫓日曰屮囗巛巾' + tbZero + bZero[1:]
    tbSmall2 = '乙八匕丁儿几九㔾了七入川大干久乇万兀下卞丫已于子巳不廿壬午止𣎵廾木雨皿又犬寸石文艸白䜌攵田丌力𤇾夂且火去比王女玉林从立臤臼申臣㕣米欠元夕丂贝卉夊覀甘禾乃臥虫天之毌'
    tbSmall = tbSmall1 + tbSmall2
    tbSmalls = [ '益-皿', '学-子', '高-冋', '甾-田', '欠-人', '责-贝' ]

    ltSmall = '广厃又尸厂疒毛㫃才户仁'
    ltSmall2 = '倝歹'
    ltLarge = '庚'

    ltrSmall = '门凡几目冂宀网产戊'

    thSmall = '癶八人入六廾大穴乃'

    def ratioToFormat(format, comps):
        small1 = False
        small2 = False
        small3 = False
        ratio = ''
        
        if format == '左右':
            if isinstance(comps[0], str):
                if comps[0][1:2] == '-':
                    small1 = lrSmalls.count(comps[0])
                else:
                    small1 = lrSmall.count(comps[0][0])
            elif comps[0]['format'] == '上下':
                    small1 = lrSmall.count(comps[0]['components'][0]) and lrSmall.count(comps[0]['components'][1])
            if isinstance(comps[1], str):
                if comps[1][1:2] == '-':
                    small2 = lrSmalls.count(comps[1])
                else:
                    small2 = lrSmall.count(comps[1][0])
            elif comps[1]['format'] == '上下':
                    small2 = lrSmall.count(comps[1]['components'][0]) and lrSmall.count(comps[1]['components'][1])

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
            elif ltSmall2.count(comps[0][0]):
                ratio = '(v1：2h1：1)'
            elif ltLarge.count(comps[0][0]):
                ratio = '(v2：1h1：2)'
        elif format == '左下包围':
            ratio = '(1：2)'
            if isinstance(comps[1], str) and lrSmall.count(comps[1][-1]):
                ratio = '(1：1)'
        elif format == '上下':
            if isinstance(comps[0], dict):
                if comps[0]['format'] == '左右':
                    small1 = tbSmall.count(comps[0]['components'][0]) and tbSmall.count(comps[0]['components'][1])
            else:
                if comps[0][1:2] == '-':
                    small1 = tbSmalls.count(comps[0])
                else:
                    small1 = tbSmall.count(comps[0][0])
            if isinstance(comps[1], dict):
                if comps[1]['format'] == '左右':
                    small2 = tbSmall.count(comps[1]['components'][0]) and tbSmall.count(comps[1]['components'][1])
            else:
                if comps[1][1:2] == '-':
                    small2 = tbSmalls.count(comps[1])
                else:
                    small2 = tbSmall.count(comps[1][0])
            
            if isinstance(comps[0], str) and tbZero.count(comps[0][0]):
                if small2:
                    ratio = '(1：2)' 
                else:
                    ratio = '(0：1)' 
            elif isinstance(comps[1], str) and bZero.count(comps[1][0]):
                if small1:
                    ratio = '(2：1)' 
                else:
                    ratio = '(1：0)'
            elif small1 == small2:
                ratio = '(1：1)'
            elif small1:
                ratio = '(1：2)'
            elif small2:
                ratio = '(2：1)'
        elif format == '上中下':
            small1 = isinstance(comps[0], str) and tbSmall.count(comps[0][0]) + tbZero.count(comps[0][0])
            small2 = isinstance(comps[1], str) and tbSmall.count(comps[1][0]) + tbZero.count(comps[1][0])
            small3 = isinstance(comps[2], str) and tbSmall.count(comps[2][0]) + tbZero.count(comps[2][0])

            if small1 == small2 and small2 == small3:
                ratio = '(1：1：1)'
            else:
                rn = { 2: 0, 1: 1, 0: 2 }
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

    def recursionQuery(char, format, pFormat, comps, command):
        ratio = ratioToFormat(format, comps)
        format = pFormat + format

        for i in range(0, len(comps)):
            c = comps[i]
            if c == None:
                continue
            if isinstance(c, dict):
                recursionQuery(char, c['format'], '%s%s%d' % (format, ratio, i), c['components'], command)
                continue

            cmd = command
            if len(c) > 1:
                if c[1] == '>':
                    cmd = command + c[1:]
                    c = c[0]
                elif c[1] != '-':
                    raise Exception('Unexpected expression: ' + c)
            if 'source' in ch._jiegou_dict.get(c, {}):
                cmd = '>' + c + cmd
                c = ch._jiegou_dict[c]['source']

            fmt = format + ratio + str(i) + cmd

            content = glyphTab.setdefault(c, dict())
            if fmt in content:
                content[fmt] += char
            else:
                content[fmt] = char

    for char, attrs in ch._jiegou_dict.items():
        if attrs["format"] == '单体':
            if 'source' in attrs:
                glyphTab.setdefault(attrs['source'], dict())['>'+char] = char
            else:
                glyphTab.setdefault(char, dict())['单体'] = char
        else:
            recursionQuery(char, attrs['format'], '', attrs['components'], '')

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
                if len(glyphTab[comp]) == 0:
                    del glyphTab[comp]
            
            count = 0
            for c in ch._jiegou_dict[req[0]]['components']:
                if isinstance(c, dict):
                    count += len(c['components'])
                else:
                    count += 1
                    
            need = '单体'
            if count != len(attr):
                need = ''.join([s[0] for s in attr])
            glyphTab.setdefault(req[0], {})[need] = req

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
    oldFiles = os.listdir(path)

    fileList = set()
    for comp, attr in ch.loadJson(tabFile).items():
        for fmt in attr.keys():
            fileName = re.sub('>', '》',  '%s：%s.svg' % (comp, fmt))
            fileList.add(fileName)
            if fileName not in oldFiles:
                tFile = open(os.path.join(path, fileName), "w", encoding='utf-8')
                tFile.close()
    
    return fileList

if __name__ == '__main__':
    genGlyphTab()