#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import copy

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

    # 此开关控制是否区分来源不同的同型部件，如“朦”与“胺”的“月”部，后者来源于“肉”
    # 除非打算梳理构造表，否则不建议关掉此Flag
    variantChar = True

    rCompTab = {
        '左右': 
        {
            1: set([ '乚', '丨', '乙', '卜', '匕', '冫', '厂', '刁', '丁', '刂', '刀', '儿', '二', '阝', '丩', '几', '九', '卩', '㔾', '丂', '力', '了', '七', '人', '入', '亻', '十', '乂', '讠', '又', '才', '叉', '川', '寸', '彳', '亍', '巛', '大', '凡', '飞', '干', '个', '工', '广', '弓', '及', '己', '巾', '久', '彐', '孑', '孓', '口', '亏', '么', '马', '女', '丬', '千', '犭', '刃', '夊', '三', '上', '勺', '尸', '巳', '扌', '彡', '饣', '氵', '纟', '山', '土', '乇', '丸', '万', '亡', '卫', '兀', '习', '下', '乡', '小', '忄', '夕', '丫', '已', '义', '于', '与', '弋', '幺', '丈', '之', '子', '夂', '厶', '失', '㇆', '币', '卞', '不', '长', '尺', '丑', '歹', '斗', '方', '分', '夫', '父', '丰', '丐', '户', '火', '见', '斤', '井', '开', '亢', '六', '仑', '木', '牜', '廿', '牛', '内', '匹', '片', '爿', '攴', '攵', '欠', '区', '犬', '日', '少', '升', '手', '殳', '礻', '水', '太', '天', '韦', '文', '无', '五', '午', '王', '冘', '牙', '尤', '友', '予', '允', '夭', '爻', '元', '月', '云', '支', '止', '中', '曰', '贝', '车', '半', '宁', '屯', '𠂤', '旡', '冄', '圼', '臬', '瓦', '身', '去', '𠤏', '尗', '术', '卢', '衤', '钅', '石', '禾', '玉', '田', '白', '目', '示', '未', '立', '甘', '生', '米', '糸', '页', '羊', '舟', '虫', '耒', '耳', '肉', '足', '言', '辛', '圭', '舌', '享', '古', '求', '交', '正', '革', '巴', '邑', '百', '豸', '关', '矢', '鸟', '乌', '骨', '皀', '毛', '冎', '丘', '吕', '戈', '且', '旦', '豆', '缶', '龺', '占', '𢇍', '㡭', '㕣', '匚', '夬', '市', '巿', '节', '釆', '呙', '寽', '朿', '束', '甲', '京', '巨', '娄', '卡', '孚', '负', '兰', '良', '𡿪', '各', '皃', '吾', '丕', '步', '亲', '刍', '肖', '男', '帀', '司', '其', '屰', '寺', '𧴪', '鱼', '秃', '系', '里', '𦣞', '豙', '㐆', '仒', '肙', '乍', '宅', '召', '贞', '朱', '𠂔', '左', '艮', '另', '〢', '仌', '归-彐', '印-卩', '新-斤', '段-殳', '敢-攵', '辟-辛', '制-刂' ])
        },
        '上下': {
            1: set([ '一', '冖', '亠', '宀', '丿', '艹', '㓁', '爫', '⺮', '罒', '人', '卜', '山', '⺌', '囗', '⺈' ]),
            2: set([ '一', '灬', '冫' ]),
            4: set([ '一', '冖', '亠', '宀', '丿', '艹', '㓁', '爫', '⺮', '罒', '人', '卜', '山', '⺌', '囗', '⺈', '灬', '冫', '二', '厶', '十', '口', '三', '上', '士', '工', '土', '亡', '小', '少', '牛', '亼', '冃', '㣺', '心', '𠫓', '日', '曰', '屮', '囗', '巛', '巾', '乙', '八', '匕', '丁', '儿', '几', '九', '㔾', '了', '七', '入', '川', '大', '干', '久', '乇', '万', '兀', '下', '卞', '丫', '已', '于', '子', '巳', '不', '廿', '壬', '午', '止', '𣎵', '廾', '木', '雨', '皿', '又', '彐', '犬', '寸', '石', '文', '艸', '白', '䜌', '攵', '田', '丌', '力', '𤇾', '夂', '且', '旦', '火', '去', '比', '王', '女', '玉', '林', '从', '立', '臤', '臼', '申', '臣', '米', '欠', '元', '夕', '丂', '贝', '卉', '夊', '覀', '甘', '禾', '乃', '臥', '虫', '天', '之', '毌', '此', '甲', '北', '加', '戈', '刀', '羽', '臸', '示', '出', '母', '䀠', '疋', '亚', '並', '䇂', '匹', '𠂹', '甶', '禸', '西', '古', '巩', '益-皿', '高-冋', '甾-田', '欠-人', '责-贝', '贵-贝', '会-亼', '昔-日', '琴-今', '畏-甶', '璺-玉', '熏-黑', '齿-止' ]),
            8: set([ '满', '赣', '楙', '襄', '匿', '㕡', '孰', '薜', '薛', '雍', '俞', '算', '酋' ]),
            16: set([ '一', '⺌' ])
        },
        '左上包围': {
            1: set([ '广', '厃', '又', '尸', '厂', '疒', '毛', '㫃', '才', '户', '仁', '𠂆' ]),
            2: set([ '倝', '歹', '攸' ]),
            4: set([ '庚', '㾜', '鹿' ])
        },
        '上三包围': {
            1: set([ '门', '凡', '几', '目', '冂', '宀', '网' ]),
            2: set([ '戊', '戉', '戕' ])
        },
        '上半包围': {
            1: set([ '癶', '八', '人', '入', '六', '廾', '大', '穴', '乃', '学', '身', '六' ]),
            2: set([ '𡨄' ])
        }
    }

    lrSmall2 = '乚丨乙卜匕冫厂刁丁刂刀儿二阝丩几九卩㔾丂力了七人入亻十乂讠又'
    lrSmall3 = '才叉川寸彳亍巛大凡飞干个工广弓及己巾久彐孑孓口亏么马女丬千犭刃夊三上勺尸巳扌彡饣氵纟山土乇丸万亡卫兀习下乡小忄夕丫已义于与弋幺丈之子夂厶失㇆'
    lrSmall4 = '币卞不长尺丑歹斗方分夫父丰丐户火见斤井开亢六仑木牜廿牛内匹片爿攴攵欠区犬日少升手殳礻水太天韦文无五午王冘牙尤友予允夭爻元月云支止中曰贝车半宁屯𠂤旡冄圼臬瓦身去𠤏尗术卢'
    lrSmall5 = '衤钅石禾玉田白目示未立甘生米糸页羊舟虫耒耳肉足言辛圭舌享古求交正革巴邑百豸关矢鸟乌骨皀毛冎丘吕戈且旦豆缶龺占𢇍㡭㕣匚夬市巿节釆呙寽朿束甲京巨娄卡孚负兰良𡿪各皃吾丕步亲刍肖男帀司其屰寺𧴪鱼秃系里𦣞豙㐆仒肙乍宅召贞朱𠂔左艮'
    lrSmall = lrSmall2 + lrSmall3 + lrSmall4 + lrSmall5
    lrSmalls = [ '归-彐', '印-卩', '新-斤', '段-殳', '敢-攵', '辟-辛', '制-刂' ]

    tbZero = '一冖亠宀丿艹㓁爫⺮罒人卜山⺌囗⺈'
    bZero = '一灬冫'
    tbSmall1 = '二厶十口三上士工土亡小少牛亼冃㣺心𠫓日曰屮囗巛巾' + tbZero + bZero[1:]
    tbSmall2 = '乙八匕丁儿几九㔾了七入川大干久乇万兀下卞丫已于子巳不廿壬午止𣎵廾木雨皿又彐犬寸石文艸白䜌攵田丌力𤇾夂且旦火去比王女玉林从立臤臼申臣米欠元夕丂贝卉夊覀甘禾乃臥虫天之毌此甲北加戈刀羽臸示出母䀠疋亚並䇂匹𠂹甶禸西古巩'
    tbSmall = tbSmall1 + tbSmall2
    tbSmalls = [ '益-皿', '高-冋', '甾-田', '欠-人', '责-贝', '贵-贝', '会-亼', '昔-日', '琴-今', '畏-甶', '璺-玉', '熏-黑', '齿-止' ]
    tbLarge = '满赣楙襄匿㕡孰薜薛雍俞算酋'

    ltSmall = '广厃又尸厂疒毛㫃才户仁𠂆'
    ltSmall2 = '倝歹攸'
    ltLarge = '庚㾜鹿'

    ltrSmall = '门凡几目冂宀网'
    ltrSmallRL = '戊戉戕'

    thSmall = '癶八人入六廾大穴乃学身六'
    thLarge = '𡨄'

    def ratioToFormat(format, comps):
        small1 = False
        small2 = False
        small3 = False
        large1 = False
        large2 = False
        zero1 = False
        zero2 = False

        flags = [ 0, 0, 0 ]
        ratio = ''

        temp = []
        for comp in comps:
            if isinstance(comp, str) and comp[1:2] == '>':
                temp.append(comp[-1])
            else:
                temp.append(comp)
        comps = temp
        
        fmt = format
        if format == '左下包围':
            fmt = '左右'
        elif format == '上中下':
            fmt = '上下'

        for i in range(0, len(comps)):
            for f, cList in rCompTab.get(fmt, {}).items():
                if isinstance(comps[i], dict) and fmt == '上下' and comps[i]['format'] == '左右':
                    if comps[i]['components'][0] in rCompTab['上下'][4] and comps[i]['components'][1] in rCompTab['上下'][4]:
                        flags[i] |= 4
                elif isinstance(comps[i], str) and comps[i] in cList:
                    flags[i] |= f

        if format == '左右':
            if flags[0] == flags[1]:
                ratio = '(1：1)'
            elif flags[0]:
                ratio = '(1：2)'
            elif flags[1]:
                ratio = '(2：1)'
        elif format == '左上包围':
            ratio = '(v1：1h1：2)'
            if flags[0] == 1:
                ratio = '(v1：2h1：2)'
            elif flags[0] == 2:
                ratio = '(v1：2h1：1)'
            elif flags[0] == 4:
                ratio = '(v2：1h1：2)'
        elif format == '左下包围':
            ratio = '(1：2)'
            if flags[1]:
                ratio = '(1：1)'
        elif format == '上下':
            if flags[0] & 1:
                if (flags[1] & 4) and (flags[0] & 16) == 0:
                    ratio = '(1：2)'
                else:
                    ratio = '(0：1)'
            elif flags[1] & 2:
                ratio = '(1：0)'
            elif (flags[0] & 4) == (flags[1] & 4):
                ratio = '(1：1)'
            elif (flags[0] & 4):
                if flags[1] & 8:
                    ratio = '(0：1)'
                else:
                    ratio = '(1：2)'
            elif (flags[1] & 4):
                if flags[0] & 8:
                    ratio = '(1：0)'
                else:
                    ratio = '(2：1)'
        elif format == '上中下':
            if (flags[0] & 5) == (flags[1] & 5) and (flags[2] & 5) == (flags[1] & 5):
                ratio = '(1：1：1)'
            else:
                rn = { 5: 0, 6: 0, 7: 0, 4: 1, 0: 2 }
                ratio = '(%d：%d：%d)' % (rn[flags[0] & 5], rn[flags[1] & 5], rn[flags[2] & 7])
        elif format == '上三包围':
            ratio = '(v1：1h1：2)'
            if flags[0] == 1:
                ratio = '(v1：2h1：2)'
            elif flags[0] == 2:
                ratio = '(v1：2h1：2：2)'
        elif format == '上半包围':
            ratio = '(1：1)'
            if flags[0] == 1:
                ratio = '(1：2)'
            elif flags[0] == 2:
                ratio = '(2：1)'
        
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
            # elif c in ch._jiegou_dict and ch._jiegou_dict[c]['format'] != '单体' and (c not in ch._jiegou_dict[c]['components']):
            #     recursionQuery(char, ch._jiegou_dict[c]['format'], '%s%s%d' % (format, ratio, i), ch._jiegou_dict[c]['components'], command)
            #     continue

            cmd = command
            if len(c) > 1:
                if c[1] == '>':
                    if variantChar:
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