#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import json
import sys

SOURCE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def loadJson(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def genConstrucTable():
    return loadJson(os.path.join(SOURCE_PATH, 'hanzi-jiegou.json'))

def queryComponent(queryComp, table):
    def recursionQuery(compList):
        ok = False
        for comp in compList:
            if isinstance(comp, dict):
                ok |= recursionQuery(comp['components'])
            else:
                c = comp
                if len(c) > 1 and c[1] == '>':
                    c = c[2]
                if c == queryComp:
                    ok = True
                else:
                    attrs = table.get(c)
                    if attrs != None:
                        ok |= recursionQuery(attrs["components"])
        return ok
    
    results = ""
    for char, attrs in table.items():
        if char == queryComp or recursionQuery(attrs["components"]):
            results += char
    
    print(results)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        table = genConstrucTable()
        queryComponent(sys.argv[1], table)
