import os

def getAviFile(path):
    #print(path)
    if not os.path.exists(path):
        print('File not exist')
        return False
    f_list = os.listdir(path)
    #print(f_list)
    for i in f_list:
        if os.path.splitext(i)[1] == '.avi':
            #print('check2')
            #print(i)
            return i
    return False