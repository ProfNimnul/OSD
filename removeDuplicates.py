import os
from easygui import diropenbox

dirname = diropenbox(msg="Выберите папку с файлами")
if not dirname:
    dirname = os.curdir


listdir = os.listdir(dirname)

files=dict()

for f in listdir:
    prefix = f.split("{")[0]
    if files.get(prefix)==None:
        files.update({prefix:f})
        continue
    fullpath=dirname+"\\"+f
    os.remove(fullpath)
pass
