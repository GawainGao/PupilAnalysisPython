import os

def file_name(file_dir):
    L=[]
    for dirpath, dirnames, filenames in os.walk(file_dir):
        for file in filenames :
            if os.path.splitext(file)[1] == '.xls':
                L.append(os.path.join(dirpath, file))
    return L

file_name('/Volumes/Transcend/Datas/WA03-1/')