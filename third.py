import os
import sys
import time
import ctypes
import pathlib
import string
import random

#Класс обрабатывающий кейсы
class Test_case:
    def prep(case):
        if case.prep():
            exit()

    def run(case):
        print(case.run())
        
    def clean_up(case):
        print(case.clean_up())
    
    def execute(self):
        try:
            self.prep()
            print ('prep function succesufully done')
        except:
            print("Unexpected error:", sys.exc_info()[0])
        try:
            self.run ()
            print ('run function succesufully done')
        except:
            print("Unexpected error:", sys.exc_info()[0])
        try:
            self.clean_up()
            print ('clean_up function succesufully done')
        except:
            print("Unexpected error:", sys.exc_info()[0])

#Базовый класс
class Case:
    def __init__(self, id, name):
        self.id = id
        self.name = name

#Тест-кейс 1: Список файлов
#Производный класс, который наследует от Case
class Files_list(Case):
    def __init__(self, id, name):
        super().__init__(id, name)
        
    def prep(self):
        ''' Возвращает True если кол-во секунд прошедших с начала эпоxи Unix является чётным числом'''
        return time.time()%2 != 0
    
    def run(self):
        '''Возвращает список файлов в домашней директории'''
        home_dir = pathlib.Path.home()
        return os.listdir(home_dir) 
    
    def clean_up(self):
        '''Функция не выполняет никаких дйствий'''
        pass

#Тест-кейс 2: Случайный файл
class Random_file(Case):
    def __init__(self, id, name):
        super().__init__(id, name)

    def prep(self):
        '''Возвращает True если ОЗУ меньше 1 Гб'''
        return   get_memory_status() < 1
            
    def run(self):
        '''Создаёт файл размером 1024 Кб'''
        random_letter = random.choice(string.ascii_letters)
        f = 'file.txt'
        open(f, "w").write(random_letter*1048576)

    def clean_up(self):
        ''' Удаляет файл file.txt'''
        f_name = 'file.txt'
        f_path = os.getcwd()
        p = os.path.join(f_path, f_name)
        if os.path.isfile(p):
            os.remove(p)
                
#Возвращает объём оперативной памяти
def get_memory_status():
    kernel32 = ctypes.windll.kernel32
    c_ulong = ctypes.c_ulong
    class MEMORYSTATUS(ctypes.Structure):
        _fields_ = [
            ("dwLength", c_ulong),
            ("dwMemoryLoad", c_ulong),
            ("dwTotalPhys", c_ulong),
            ("dwAvailPhys", c_ulong),
            ("dwTotalPageFile", c_ulong),
            ("dwAvailPageFile", c_ulong),
            ("dwTotalVirtual", c_ulong),
            ("dwAvailVirtual", c_ulong)
        ]
    memoryStatus = MEMORYSTATUS()
    memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUS)
    kernel32.GlobalMemoryStatus(ctypes.byref(memoryStatus))
    return (memoryStatus.dwTotalPhys/(1024*1024)/1000)


list_file = Files_list(1, 'first')
file_random = Random_file(2, 'second')
test_case = Test_case.execute(file_random)
