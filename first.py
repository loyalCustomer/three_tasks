import os
import shutil
import ctypes
import sys
from xml.dom import minidom

def is_admin():
    """ Проверяем права"""
    try:
        #Если администратор вернет True
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Если пользователь администратор продолжаем скрипт дальше
    pass
else:
    #Перезапускаем скрипт с правами администратора
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
                                        __file__, None, 1)
    exit()

cf = minidom.parse('config.xml')
paths = cf.getElementsByTagName('file')

for path in paths:
    src_path = path.attributes['source_path'].value
    f_name = path.attributes['file_name'].value
    src = os.path.join(src_path, f_name)
    dst_path = path.attributes['destination_path'].value
    dst = os.path.join(dst_path, f_name)
    #проверяем, что исходный файл и папка назначения существуют
    if os.path.exists(src) and os.path.exists(dst_path):
        shutil.copyfile(src, dst, follow_symlinks=True)
    else:
        pass