#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------- 分类规则配置 START ----------------

_compClassTab = {
    # 此开关控制是否区分来源不同的同型部件，如“朦”与“胺”的“月”部，后者来源于“肉”
    # 若对变体部件做区分，则生成文件以{源部件}：{格式}》{变体部件}的形式做标注
    # 除非打算梳理构造表，否则不建议关掉此Flag
    "variantChar": True,

    # 部件分类表
    # 每一个集合的序号需选取为从1起2的次方数，即1、2、4、8、16、32……
    # 部件集合为该结构下有别于默认格式的部件
    "rCompTab": {
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
    },

    # 在此标注借用其他结构分类表的结构
    # e.g 左下包围结构需要特殊对待的部件与左右结构相同
    "sameCompTab": {
        '左下包围': '左右',
        '上中下': '上下',
    },

    # 复合结构判定，决定是否对hanzi-jiegou.json中记录的复合结构做判定
    # 默认直接判定为默认部件
    # e.g “森”字下部件为“木”“木”，“木”部件处于部件分类表上下结构的4集合中，符合(左4, 右4)，所以得到下表定义的（第三个）4
    "recursionTab": {
        '上下': {
            '左右': [
                [ (4, 4), 4 ]
            ]
        }
    },

    # 部件组合判定表，数据格式为[ (主部件, 次部件), '结构说明' ]
    # 0代表默认部件，即不在部件分类表rCompTab中的部件
    # -1代表任意部件
    # 多个集合用'|'分隔，如（1 | 2, 4 | 8），只要部件存在于其中一个集合即可通过判定
    # 判定列表是有序的，请务必考虑好判定的优先级
    "cCompTab": {
        '左右': [
            [ (0, 0), '(1：1)' ],
            [ (1, 1), '(1：1)' ],
            [ (1, 0), '(1：2)' ],
            [ (0, 1), '(2：1)' ]
        ],
        '左上包围': [
            [ (1, -1), '(v1：2h1：2)' ],
            [ (2, -1), '(v1：2h1：1)' ],
            [ (4, -1), '(v2：1h1：2)' ],
            [ (0, -1), '(v1：1h1：2)' ]
        ],
        '左下包围': [
            [ (-1, 1), '(1：1)' ],
            [ (-1, 0), '(1：2)' ]
        ],
        '上下': [
            [ (16, 4), '(0：1)' ],
            [ (1, 4), '(1：2)' ],
            [ (1, -1), '(0：1)' ],
            [ (-1, 2), '(1：0)' ],
            [ (4, 4), '(1：1)' ],
            [ (4, 8), '(0：1)' ],
            [ (4, -1), '(1：2)' ],
            [ (8, 4), '(1：0)' ],
            [ (-1, 4), '(2：1)' ],
            [ (-1, -1), '(1：1)' ]
        ],
        # 上中下结构对应的结果太多, 依据情况添加即可
        '上中下': [
            [ (1, 4, 0), '(0：1：2)' ],
            [ (1, 0, 0), '(0：2：2)' ],
            [ (1, 0, 4), '(0：2：1)' ],
            [ (1, 1, 4), '(0：0：1)' ],
            [ (0, 4, 2), '(2：1：0)' ],
            [ (1, 4, 1), '(0：1：0)' ],
            [ (0, 4, 0), '(2：1：2)' ],
            [ (4, 0, 1 | 2), '(1：2：0)' ],
            [ (4, 1, 4), '(1：0：1)' ],
            [ (4, 4, 4), '(1：1：1)' ],
            [ (4, 0, 4), '(1：2：1)' ],
            [ (0, 0, 4), '(2：2：1)' ],
            [ (4, 4, 0), '(1：1：2)' ],
            [ (0, 4, 4), '(2：0：0)' ]
        ],
        '上三包围': [
            [ (1, -1), '(v1：2h1：2)' ],
            [ (2, -1), '(v1：2h1：2：2)' ],
            [ (-1, -1), '(v1：1h1：2)' ]
        ],
        '上半包围': [
            [ (1, -1), '(1：2)' ],
            [ (2, -1), '(2：1)' ],
            [ (-1, -1), '(1：1)' ]
        ]
    }
}

# ---------------- 分类规则配置 END ----------------

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

def genGlyphTab(file = 'glyph.json', compClassTab = None):
    if compClassTab == None: compClassTab = _compClassTab
    
    cCompTab = compClassTab['cCompTab']
    sameCompTab = compClassTab['sameCompTab']
    rCompTab = compClassTab['rCompTab']
    recursionTab = compClassTab['recursionTab']
    variantChar = compClassTab['variantChar']

    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    ch.init()
    glyphTab = dict()

    def ratioToFormat(format, comps):
        # 不在在判定表中的结构返回空串
        if format not in cCompTab:
            return ''

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
        if fmt in sameCompTab:
            fmt = sameCompTab[fmt]

        for i in range(0, len(comps)):
            for f, cList in rCompTab.get(fmt, {}).items():
                if isinstance(comps[i], dict) and fmt in recursionTab and comps[i]['format'] in recursionTab[fmt]:
                    for rRule in recursionTab[fmt][comps[i]['format']]:
                        ok = True
                        for j in range(0, len(rRule[0])):
                            ok &= rRule[0][j] == -1 or comps[i]['components'][j] in rCompTab[fmt][rRule[0][j]]
                        if ok:
                            flags[i] |= rRule[1]
                elif isinstance(comps[i], str) and comps[i] in cList:
                    flags[i] |= f

        i = 0
        while True:
            ok = True
            for j in range(0, len(cCompTab[format][i][0])):
                ok &= (cCompTab[format][i][0][j] & flags[j]) != 0 or cCompTab[format][i][0][j] == flags[j] or cCompTab[format][i][0][j] == -1
            if ok:
                ratio = cCompTab[format][i][1]
                break
            i += 1
            
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
                    else:
                        c = c[-1]
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
        if attrs['format'] == '单体':
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
                tFile = open(os.path.join(path, fileName), 'w', encoding='utf-8')
                tFile.close()
    
    return fileList

if __name__ == '__main__':
    genGlyphTab()