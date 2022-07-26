import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(FILE_PATH)
TEMP_TASK_PATH = os.path.join(FILE_PATH, 'tasks')
COMP_PATH = os.path.join(FILE_PATH, 'components')
GLYPHTAB_FILE_PATH = os.path.join(FILE_PATH, 'glyph.json')

def genCompGlyph(compClassTab = None, tasksPath=TEMP_TASK_PATH, compPath=COMP_PATH):
    if not os.path.exists(os.path.join(PROJECT_PATH, 'hanzi-jiegou.json')):
        print('Not found hanzi-jiegou.json')
        return

    import sys
    sys.path.append(os.path.join(PROJECT_PATH, 'scripts'))
    import genGlyphTab as gen

    if not os.path.exists(compPath):
        os.mkdir(compPath)
    if not os.path.exists(tasksPath):
        os.mkdir(tasksPath)
        
    oldFiles = set()
    for filename in os.listdir(tasksPath):
        if(filename[-4:] == '.svg'):
            oldFiles.add(filename)
            
    gen.genGlyphTab(GLYPHTAB_FILE_PATH, compClassTab)
    newFiles = gen.genGlyphFiles(tasksPath, GLYPHTAB_FILE_PATH)
    
    compFiles = set(os.listdir(compPath))
    rFile = oldFiles - newFiles
    reFile = compFiles - newFiles

    print('删除%d个旧文件' % len(rFile))
    print('添加%d个新文件' % len(newFiles - oldFiles - compFiles))
    print('%d个组件不需要' % len(reFile))
    if len(reFile): print(reFile)

    for file in rFile: os.remove(os.path.join(tasksPath, file))
    for file in compFiles - reFile: os.remove(os.path.join(tasksPath, file))

if __name__ == '__main__':
    genCompGlyph()