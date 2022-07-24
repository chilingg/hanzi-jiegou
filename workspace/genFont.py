import os
import sys
import json

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(FILE_PATH)
GLYPH_PATH = os.path.join(FILE_PATH, 'glyphs')
SYMBOL_PATH = os.path.join(FILE_PATH, 'symbols')
FONT_FILE_PATH = os.path.join(PROJECT_PATH, 'font')
TEMP_GLYPH_FILE = 'tempGlyph.svg'

def loadJson(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def start():
    if not os.path.exists(FONT_FILE_PATH):
        os.mkdir(FONT_FILE_PATH)

    cllib = os.path.join(PROJECT_PATH, 'clsvg')
    if os.path.exists(cllib):
        sys.path.append(cllib)
       
def finish():
    if os.path.exists(TEMP_GLYPH_FILE):
        os.remove(TEMP_GLYPH_FILE)
 
def writeTempGlyphFromShape(shape, tag, attrib):
    newRoot = svgfile.ET.Element(tag, attrib)
    newRoot.text = '\n'
    styleElem = svgfile.ET.Element('style', { 'type': 'text/css' })
    styleElem.text = '.st0{fill:#000000;}'
    styleElem.tail = '\n'
    newRoot.append(styleElem)

    newRoot.append(shape.toSvgElement({ 'class': 'st0' }))
    newTree = svgfile.ET.ElementTree(newRoot)
    newTree.write(TEMP_GLYPH_FILE, encoding = "utf-8", xml_declaration = True)

def genGroupFromPath(filepath):
    tree = svgfile.parse(filepath)
    root = tree.getroot()

    g = bezierShape.GroupShape()
    for child in root:
        tag = svgfile.unPrefix(child.tag)
        if tag != 'style':
            paths = bezierShape.createPathfromSvgElem(child, tag)
            if len(paths):
                shape = bezierShape.BezierShape()
                shape.extend(paths[0])
                g |= bezierShape.GroupShape(shape)
    return g

def importGlyph():
    GLYPH_TAG = 'svg'
    GLYPH_ATTRIB = {
        'version': '1.1',
        'id': 'glyph',
        'x': '0px',
        'y': '0px',
        'viewBox': '0 0 720 900',
        'style': 'enable-background:new 0 0 720 900;',
        'space': 'preserve'
        }

    font = fontforge.open(os.path.join(FILE_PATH, 'Empty.sfd'))

    styleElem = svgfile.ET.Element('style', { 'type': 'text/css' })
    styleElem.text = '.st0{fill:#000000;}'
    styleElem.tail = '\n'

    numList = [0, 0]
    for path in [GLYPH_PATH, SYMBOL_PATH]:
        fileList = os.listdir(path)
        num = len(fileList)
        count = 0
        for filename in fileList:
            if(filename[-4:] == '.svg'):
                if(len(filename) == 5):
                    char = filename[0]
                    code = ord(char)
                    count += 1
                elif(filename[:-4].isdecimal()):
                    n = int(filename[:-4])
                    if(n < 128):
                        code = n
                        char = chr(code)
                else:
                    raise Exception('Unknown File Name: ' + filename)

                print("(%d/%d)%s: import glyph '%s' %d from %s" % (count, num, font.fontname, char, code, filename))
                
                tree = svgfile.parse(os.path.join(path, filename))
                root = tree.getroot()

                newRoot = svgfile.ET.Element(root.tag, root.attrib)
                newRoot.text = '\n'
                newRoot.append(styleElem)
                for child in root:
                    tag = svgfile.unPrefix(child.tag)
                    if tag != 'style':
                        paths = bezierShape.createPathfromSvgElem(child, tag)
                        if len(paths):
                            shape = bezierShape.BezierShape()
                            shape.extend(paths)
                            newRoot.append(shape.toSvgElement({ 'class': 'st0' }))
                            
                newTree = svgfile.ET.ElementTree(newRoot)
                newTree.write(TEMP_GLYPH_FILE, encoding = "utf-8", xml_declaration = True)

                glyph = font.createChar(code)
                glyph.importOutlines(TEMP_GLYPH_FILE)
                glyph.width = int(root.attrib['viewBox'].split()[2])

        numList[0], numList[1] = numList[1], num

    print("%s: The Font has %d glyphs, of which %d are symbol" % (font.fontname, numList[0], numList[1]))
    print("Generate font sfd file in %s" % os.getcwd())
    font.save()
    font.close()

if __name__ == '__main__':
    start()

    import fontforge
    from clsvg import svgfile
    from clsvg import bezierShape

    importGlyph()
    
    finish()