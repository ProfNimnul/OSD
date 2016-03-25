import os
from easygui import diropenbox
from os import path
import pprint


dirname = diropenbox(msg="Выберите папку с файлами")
if not dirname:
    dirname = os.curdir


listdir = os.listdir(dirname)
fileparams = dict() # тут хранятся данные о файле - будет словарь словарей
# на один префикс хранится имя файла, его длина, тип (файл, папка)
files=dict()

for f in listdir:
    fullpath=dirname+"\\"+f
    prefix = (f.split("}"))[0].split("{")[1]
   
    if not prefix in files:
        files.update({"prefix":prefix,"filename":f,"filelenght":os.path.getsize(fullpath)})
        
        pprint.pprint(files)
        continue
  
    
 #   os.remove(fullpath)
pass
