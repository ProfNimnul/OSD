# -*-coding: utf-8-*-
import os
from easygui import diropenbox
import pprint


dirname = diropenbox(msg="Выберите папку с файлами")
if not dirname:
    dirname = os.curdir


listdir = os.listdir(dirname)
print(len(listdir))
fileparams = dict()  # тут хранятся данные о файле - будет словарь словарей
# на один префикс хранится имя файла, его длина, тип (файл, папка)
files = dict()

for f in listdir:
    try: 
        fullpath=dirname+"\\"+f
        prefix = f.split()[0]
        if  not files.get(prefix,None):
            files.update({prefix:{"filename": f, "filelenght": os.path.getsize(fullpath)}})
      
            continue
    except Exception:
        continue

    os.remove(fullpath)
pprint.pprint(len(files))
pprint.pprint(files)
    

pass
