import os
import sys
import json
import re

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(FILE_PATH)
COMP_PATH =   os.path.join(FILE_PATH, 'components')
GLYPHTAB_FILE_PATH = os.path.join(FILE_PATH, 'glyph.json')
CHEKC_FILE_PATH = os.path.join(FILE_PATH, 'glyphs')

def checkGlyph(checkFilePath=CHEKC_FILE_PATH, compPath=COMP_PATH):
    def loadJson(file):
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)

    if not os.path.exists(checkFilePath):
        os.mkdir(checkFilePath)

    LIB = os.path.join(PROJECT_PATH, 'clsvg')
    if os.path.exists(LIB):
        sys.path.append(LIB)

    from clsvg import svgfile
    from clsvg import bezierShape

    glyphTable = loadJson(GLYPHTAB_FILE_PATH)
    fileList = os.listdir(compPath)
    charsList = {}

    count = 0
    for comp, fmts in glyphTable.items():
        for fmt, chars in fmts.items():
            fileName = '%s：%s.svg' % (comp, fmt)
            fileName = re.sub('>', '》',  '%s：%s.svg' % (comp, fmt))
            if fileName not in fileList:
                continue
            else:
                count += 1
                #print('(%d/%d)Process %s ...' % (count, len(fileList), fileName))

            tree = svgfile.parse(os.path.join(compPath, fileName))
            root = tree.getroot()

            shape = []
            for child in root:
                tag = svgfile.unPrefix(child.tag)
                if tag != 'style':
                    shape.append(bezierShape.createPathfromSvgElem(child, tag))

            for char in chars:
                if char not in charsList:
                    charsList[char] = []
                charsList[char].extend(shape)

    count = 0
    fileList = set(os.listdir(checkFilePath))
    for char, shape in charsList.items():
        count += 1
        #print('(%d/%d)Generating %s ...' % (count, len(charsList), char))

        newRoot = svgfile.ET.Element(root.tag, root.attrib)
        newRoot.text = '\n'
        styleElem = svgfile.ET.Element('style', { 'type': 'text/css' })
        styleElem.text = '.st0{fill:none;stroke:#000000;stroke-width:48;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:10;}'
        styleElem.tail = '\n'
        newRoot.append(styleElem)
        for path in shape:
            newRoot.append(path.toSvgElement({ 'class': 'st0' }))
        newTree = svgfile.ET.ElementTree(newRoot)

        fileName = char + '.svg'
        fileList.discard(fileName)
        newTree.write(os.path.join(checkFilePath, char + '.svg'), encoding = "utf-8", xml_declaration = True)
    
    for file in fileList: os.remove(os.path.join(checkFilePath, file))

if __name__ == '__main__':
    checkGlyph()