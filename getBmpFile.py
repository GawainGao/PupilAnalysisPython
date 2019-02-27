import os

def getBmpFile(path):
    f_list = os.listdir(path)
    file_list = []
    for i in f_list:
        if 'pl' in i:
            if '.png' in i or '.bmp' in i:
                file_list.append(i)
    #print(file_list)
    return file_list