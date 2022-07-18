#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import json

SOURCE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

_jiegou_dict = dict()

def loadJson(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def saveJson(obj, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)

def saveFile(texts, file):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(texts)

def init():
    global _jiegou_dict
    _jiegou_dict = loadJson(os.path.join(SOURCE_PATH, 'hanzi-jiegou.json'))

def check():
    COMP_SIZE = {
        '上三包围': 2,
        '上下': 2, 
        '上下包围': 2, 
        '上中下': 3, 
        '上半包围': 2, 
        '下三包围': 2, 
        '下半包围': 2, 
        '全包围': 2,
        '右三包围': 2, 
        '右上包围': 2, 
        '右下包围': 2, 
        '左三包围': 2, 
        '左上包围': 2, 
        '左下包围': 2, 
        '左中右': 3, 
        '左右': 2, 
        '左右包围': 2
    }
    compList = set()
    formats = ['单体']

    def recursionQuery(fmt, comps):
        if fmt not in formats:
            formats.append(fmt)
        if len(comps) != COMP_SIZE[fmt]:
            raise Exception('Error number of components!')

        for c in comps:
            if c == None:
                continue
            if isinstance(c, dict):
                recursionQuery(c['format'], c['components'])
                continue

            if len(c) > 1:
                if c[1] != '-' and c[1] != '>':
                    raise Exception('Unexpected expression: ' + c)
                else:
                    if c[1] != '-' or c[2] not in comps:
                        c = c[0]

            if _jiegou_dict.get(c) == None:
                compList.add(c)

    for char, arrts in _jiegou_dict.items():
        if arrts["format"] == '单体':
            if len(arrts['components']):
                raise Exception('Single structure is not single!')
            compList.add(char)
        elif None in arrts['components'] and char in arrts['components']:
            compList.add(char)
        else:
            # if char in arrts['components']:
            #     raise Exception('Error Recursive component!')
            recursionQuery(arrts['format'], arrts['components'])

    print('components:\n', compList)
    formats.sort()
    print('formats:\n', formats)
    print('字符：%d，格式：%d，部件：%d' % (len(_jiegou_dict), len(formats), len(compList)))

if __name__ == '__main__':
    init()
    check()