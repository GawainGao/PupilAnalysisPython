import os

def getPath(path, day, low, high):
    f_list = os.listdir(path)
    #path is '/Volumes/WA03-1/WA03 2016 1/827/...
    file_list = []
    #low1, low2, low3 = low
    #high1, high2, high3 = high
    #print(low1, low2, low3)
    #print(high1, high2, high3)
    for i in f_list:
        if i == 'short' or i == 'Z_short' or i == 'red or pink':
            continue
        print(i)
        ss = i.split('_')
        print('Check', ss)
        if len(ss) <= 1:
            continue
        print(ss[3])
        print(ss[4])
        #print(ss[5])
        if int(ss[3]) == day and int(ss[4]) == low and int(ss[5]) == high:
        #if int(ss[3]) in day:
            print(i)
            file_list.append(i)
    return file_list
