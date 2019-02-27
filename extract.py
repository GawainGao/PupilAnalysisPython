import os
import shutil

#cattles = ['826', '827', '828', '829', '830', '831', '832', '833']
#cattles = ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7', 'class8', 'class9']
#cattles = ['class1', 'class3', 'class4', 'class5', 'class6', 'class7', 'class8']
# cattles = ['class1', 'class2' ,'class3', 'class4', 'class5', 'class6', 'class7', 'class8']
# cattles = ['826','827','828','829','830','831','832','833']
# cattles = ['799','810','811','813','814','815','816','817']
cattles = ['class9', 'class4', 'class10', 'class6', 'class7', 'class8']
#names = ['WA03 2016 1', 'WA03 2016 4', 'WA03 2016 5']
#names = ['finalset WA02 2015 12 14282s']
#names = ['finalset WA02 2016 1 34013s']
#names = ['finalset WA01 2016 2 18983s - done checked']
names = ['finalset WA06 2015 10','finalset WA06 2015 12','finalset WA06 2016 1','finalset WA06 2016 2','finalset WA06 2016 3']
# names = ['WA02 2015 4', 'WA02 2015 11 -separated', 'WA02 2015 10 - separated', 'WA02 2015 9 - separated', 'WA02 2015 7', 'WA02 2015 6', 'WA02 2015 5']
out_path = '/Volumes/Transcend/Extracts/WA06/'
in_path = '/Volumes/Transcend/Datas/WA06/'

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print('--- new folder... ---')
        print('--- OK ---')
    else:
        print('--- There is a folder ---')


for i in names:
    for j in cattles:
        path = in_path + i + '/'+ j
        if os.path.exists(path):
            f_list = os.listdir(path)
        else:
            print('Empty')
            f_list = []
        if len(f_list):
            for k in f_list:
                ppath = in_path + i + '/' + j + '/' + k + '/result'
                outppath = out_path + i + '/' + j + '/' + k
                ff_list = os.listdir(ppath)
                for m in ff_list:
                    if os.path.splitext(m)[1] == '.xls':
                        mkdir(outppath)
                        shutil.copyfile(ppath + '/' + m, outppath + '/' + m)








