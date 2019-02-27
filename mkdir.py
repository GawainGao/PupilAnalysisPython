import os

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print('--- new folder... ---')
        print('--- OK ---')
    else:
        print('--- There is a folder ---')