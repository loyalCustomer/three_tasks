import hashlib
import os

supported_algo = ['md5','sha1','sha256']
def get_hash(algo,name,f_dir):
    f_path = os.path.join(f_dir,name)
    if os.path.exists(f_path)== False:
        return ('NOT FOUND')
    if algo not in supported_algo:
        return ('NOT SUPPORTED')
    if algo =='md5':
        hash_value = hashlib.md5()
    elif algo =='sha1':
        hash_value = hashlib.sha1()
    else:
        hash_value = hashlib.sha256()
    with open(f_path, "rb") as f:
        data = f.read()
        hash_value.update(data)
        return hash_value.hexdigest()

def hash_check(input_file, file_dir):
    if os.path.exists(input_file) == False:
        print ('Исходный файл не найден')
        exit()        
    with open(input_file) as f:
            data = f.read()
    for line in data.splitlines():
        params = line.split()
        name = params[0]
        algo = params[1].lower()
        checksum = params [2]
        hash_value = get_hash(algo,name,file_dir)
        if hash_value==checksum:
            print (name, 'OK')
        elif hash_value == 'NOT FOUND':
            print (name, 'NOT FOUND')
        elif hash_value == 'NOT SUPPORTED':
            print (name, 'HASH TYPE', algo.upper(), 'IS NOT SUPPORTED' )
        else:
            print (name, 'FAIL')

hash_check('input_file.txt',r"C:\Users\User\projects\three_tasks")