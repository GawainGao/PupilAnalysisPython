# -*- coding:utf-8 -*-
# This code is used for cattle group to analysis the pictures automatically taken

#The file-tree
#
# ---input.py>---main.py-------o---getPath.py<---------os
#                    |         |
#                    |         o----getBmpFile.py<-----os
#                    |         |
#                    |         o----mkdir.py<----------os
#                    |         |
#                    |         o----getAviFile.py<-----os
#                    v
#               extract.py<-----shutil & os



import cv2
import xlwt
import os
import numpy as np
import matplotlib.pyplot as plt

import getAviFile
import mkdir
import getBmpFile
import getPath

#cattles = [826, 827, 828, 829, 830, 831, 832, 833]
#cattles = {'class1':'816', 'class2':'817', 'class3':'799', 'class4':'814', 'class6':'811', 'class7':'815', 'class8':'813', 'class9':'Unknown'}
#cattles = {'class1':'816', 'class2':'817', 'class3':'799', 'class4':'814', 'class5':'810', 'class6':'811', 'class7':'815', 'class8':'813', 'class9':'799'}
#cattles = {'class1':'816', 'class2':'817', 'class3':'799', 'class4':'814', 'class5':'810', 'class6':'811', 'class7':'815', 'class8':'813', 'class9':'814'}
#cattles = {'class1':'795', 'class3':'801', 'class4':'798', 'class5':'799', 'class6':'800', 'class7':'797', 'class8':'794'}

#cattles = {'class8':'813', 'class9':'814'}
#cattles = {'class7':'815', 'class8':'813', 'class9':'799'}
#VA = {'class1':'28.75', 'class2':'30.00', 'class3':'40.00', 'class4':'27.50', 'class5':'41.25', 'class6':'19.17', 'class7':'30.83', 'class8':'37.08', 'class9':'73.75'}
#VA = {'class1':'45.83', 'class3':'71.25', 'class4':'57.50', 'class5':'64.17', 'class6':'78.33', 'class7':'78.33', 'class8':'62.08'}


#cattles = {'class1':'816', 'class2':'817', 'class3':'799', 'class4':'814', 'class5':'810', 'class6':'811', 'class7':'815', 'class8':'813'}
#cattles = {'class3':'799', 'class4':'814', 'class5':'810', 'class6':'811', 'class7':'815', 'class8':'813'}
#cattles = {'class1':'795', 'class4':'798', 'class5':'799', 'class6':'800', 'class7':'797', 'class8':'794'}
#cattles = {'class5':'799', 'class6':'800', 'class7':'797', 'class8':'794'}
#VA = {'class1':'29.58', 'class4':'39.58', 'class5':'41.25', 'class6':'58.33', 'class7':'54.58', 'class8':'30.83'}
cattles = {'class7':'863'}
# cattles = {'class10':'863'}
# input_path = '/Volumes/WA01_1/finalset WA01 2016 2 18983s - done checked/'
# input_path = '/Volumes/HD-LCU3/masumoto/WA02/2015-7 image/810/'
# input_path = '/Volumes/HD-LCU3/masumoto/WA02/2015-7 image/'
input_path = '/Volumes/WA06/finalset WA06 2016 3/'
# cattles = {'ipr':'810'}
# cattles = {'799 green bule':'799','810 light bule':'810','811 bule':'811','813 red':'813','814 green':'814','815 red and bule':'815','816 red and yellow':'816','817 yellow':'817'}
# cattles = {'799 bule green':'799','811 bule':'811','813 red':'813','814 green':'814','816 red and yelllow':'816','817 yellow':'817'}
# cattles = {'799':'799'}
# cattles = {'799':'799','810':'810','811':'811','813':'813','814':'814','815':'815','816':'816','817':'817'}
# cattles = {'810':'810','811':'811','813':'813'}
# cattles = {'810':'810','811':'811','813':'813'}
# cattles = {'810 light bule':'810','813 red':'813'}
# cattles = {'811':'811'}
#VA = {'817':'57.08'}
day = 19
#day = [6, 5, 18, 2]
# day = [22]
low = 9
high = 48



VedioFlag = True #is used for check if there is 'avi' file inside the folder or just the pictures
for llx in cattles:
    #pathNameGroup = getPath('/Volumes/WA03-1/WA03 2016 4/' + str(llx), 11, [10, 18, 21], [16, 43, 34])
    #pathNameGroup = getPath.getPath('/Volumes/WA03-1/WA03 2016 5/' + str(llx), 9, [10, 18, 21], [16, 43, 34])
    #pathNameGroup = getPath.getPath('/Volumes/WA02-4/finalset WA02 2016 1 34013s/' + llx, 19, [0, 0, 0], [0, 0, 0])
    pathNameGroup = getPath.getPath(input_path + llx, day, low, high)

    #pathNameGroup = getPath('/Volumes/WA03-1/WA03 2016 1/833', 19, [10, 18, 21], [16, 43, 34])
    #print(pathNameGroup)

    for count in range(len(pathNameGroup)):
    #for count in range(0,1):
        pathNameBack = pathNameGroup[count]
        #pathName = '/Volumes/WA03-1/WA03 2016 1/833/' + pathNameBack

        #pathName = '/Volumes/WA03-1/WA03 2016 4/' + str(llx) + '/' + pathNameBack
        #pathName = '/Volumes/WA03-1/WA03 2016 5/' + str(llx) + '/' + pathNameBack
        #pathName = '/Volumes/WA02-4/finalset WA02 2016 1 34013s/' + llx + '/' + pathNameBack
        pathName = input_path + llx + '/' + pathNameBack
        #print(pathName)

        #Get the cattle number and the picture taking date
        aa = pathName.split('/')
        #print(aa[4])
        #print(aa[5])
        print(aa)
        bb = aa[-1].split('_')    #The date folder always be the last one
        print('Check!!!', bb)
        #print(bb[1], ' ', bb[2], ' ', bb[3])
        date = bb[1] + '/' + bb[2] + '/' + bb[3]
        #cattle_num = aa[4]
        #print(cattles[llx])
        cattle_num = cattles[llx]

        #Set the destination folder
        dstpathName = '/Volumes/Transcend/Data' + pathName[8:] + '/result'
        mkdir.mkdir(dstpathName)

        #Start a excel book
        book = xlwt.Workbook(encoding='utf-8')
        sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)
        sheet1.write(0,0,'ファイル名：読み込んだ時のセッション名をファイル名とする')
        sheet1.write(1,4,'牛ビタミンA推定説明変数の画像とのCSVデータ関連付け（各画像データから特徴量の抽出） 画像読み取りソフト活用による特徴量のエクセル取込みイメージ')
        sheet1.write(2,0,'画像取込み確認  （チェック）       Confirmation of Input picture numerical ananysis')
        sheet1.write(2,1,' ') #Waiting for check
        sheet1.write(2,4,' ')
        sheet1.write(2,5,'→画像から特徴量特定して挿入する箇所')
        sheet1.write(2,12,'R,G,Bの各占有率を以下に定義する。特徴量から自動計算する。')
        sheet1.write(3,0,'　牛番号　　Cattle　No　　　　　　首輪画像から識別')
        sheet1.write(3,1,cattle_num)
        sheet1.write(3,4,'注）牛の個体識別タグと牛番号の対応が必要')
        sheet1.write(3,12,'r=R/(R+G+B)')
        sheet1.write(4,0,'生年月日     Birth Date　　　〇〇/〇〇/〇〇')
        sheet1.write(4,1,' ')
        sheet1.write(4,4,'注）牛の年齢がビタミンA濃度に影響')
        sheet1.write(4,12,'g=G/(R+G+B)')
        sheet1.write(5,0,'画像撮影日時 Taking picture date　time 〇〇/〇〇/〇〇/・・・・')
        sheet1.write(5,1,date)
        sheet1.write(5,12,'b=B/(R+G+B)')
        sheet1.write(6,0,'飲水量')
        sheet1.write(6,1,' ')
        sheet1.write(7,0,'ビタミンA濃度  　　　　　　　　　　　　　　　　Viamain A concentration')
        sheet1.write(7,1,'画像番号')
        sheet1.write(8,1,'Picture No')
        sheet1.write(7,2,'短径・長径　　　　　　　　　特徴量　　')
        sheet1.write(9,2,'長径X　　　　')
        sheet1.write(9,3,'短径Y')
        sheet1.write(7,4,'瞳孔収縮率（短径／長径）')
        sheet1.write(8,4,'Shirink ratio')
        sheet1.write(7,5,'眼底色　　　　　　Eye bottom color')
        sheet1.write(8,5,'楕円面積')
        sheet1.write(9,5,'S=π×（X/２）×（Y/2）')
        sheet1.write(8,6,'眼底楕円内のG,G,B平均と分散')
        sheet1.write(9,6,'R平均')
        sheet1.write(9,7,'R分散')
        sheet1.write(9,8,'G平均')
        sheet1.write(9,9,'G分散')
        sheet1.write(9,10,'B平均')
        sheet1.write(9,11,'B分散')
        sheet1.write(8,12,'RGB占有率')
        sheet1.write(9,12,'r')
        sheet1.write(9,13,'g')
        sheet1.write(9,14,'b')

        sheet1.write(7,15,'瞳孔色　　　　　　　　Pupil　color')
        sheet1.write(8,24,'RGB占有率')
        sheet1.write(9,15,'LEDリング中心ｘ')
        sheet1.write(9,16,'LEDリング中心y')
        sheet1.write(9,17,'LEDリンク半径')
        sheet1.write(9,18,'R平均　R mean')
        sheet1.write(9,19,'R分散')
        sheet1.write(9,20,'G平均　G mean')
        sheet1.write(9,21,'G分散')
        sheet1.write(9,22,'B平均　B Mean')
        sheet1.write(9,23,'B分散')
        sheet1.write(9,24,'r')
        sheet1.write(9,25,'g')
        sheet1.write(9,26,'b')

        #First get the avi file and divide into frames
        #pathName = '/Volumes/WA03_3/WA03 2016 6'
        aviPath = getAviFile.getAviFile(pathName)
        if aviPath == False:
            VedioFlag = False

        if not aviPath == False:

            print(aviPath)
            cap = cv2.VideoCapture(pathName + '/' + aviPath)
            if (cap.isOpened() == False):
                print("Error opening the avi file")
            wid = int(cap.get(3))
            hei = int(cap.get(4))
            framerate = int(cap.get(5))
            framenum = int(cap.get(7))
            video = np.zeros((framenum, hei, wid, 3), dtype='float16') #Save into the parameter video
            cnt = 0
            print("frames_num:", framenum, "frames_rate:", framerate, "width:", wid, "height:", hei)

            while(cap.isOpened()):
                ret,frame = cap.read()
                #cv2.imshow('%d'%cnt, frame)
                #cv2.waitKey(20)

                dstName = 'sdividel' + str(cnt) + '.jpg'
                cv2.imwrite(dstpathName + '/'+ dstName, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

                #frame = frame.astype('float16')/255
                #video[cnt] = frame

                if cnt == 90: #When reach to 90th frame, break
                    break
                #print(cnt)
                cnt+=1
            cap.release()
            cv2.destroyAllWindows()

            #print(video[10])
            #for i in range(10, video.size):

            for i in range(10, 89):
                srcImg = cv2.imread(dstpathName + '/' + 'sdividel' + str(i) + '.jpg')
                #cv2.imshow('Display', srcImg)
                #cv2.waitKey(0)
                if not len(cv2.split(srcImg)) == 3:
                    break
                B, G, R = cv2.split(srcImg)
                HSV = cv2.cvtColor(srcImg, cv2.COLOR_BGR2HSV)
                #cv2.imshow('HSV', HSV)
                #cv2.waitKey(0)
                H, S, V = cv2.split(HSV)
                #cv2.imshow('B', B) #is useful
                #cv2.waitKey(0)
                #cv2.imshow('G', G)
                #cv2.waitKey(0)
                #cv2.imshow('R', R)
                #cv2.waitKey(0)
                #cv2.imshow('H', H) #is useful
                #cv2.waitKey(0)
                #cv2.imshow('S', S)
                #cv2.waitKey(0)
                #cv2.imshow('V', V)
                #cv2.waitKey(0)
                lower_blue = np.array([150, 132, 107])
                upper_blue = np.array([210, 210, 210])
                lower_h = np.array([102, 0, 0])
                upper_h = np.array([125, 255, 255])

                mask = cv2.inRange(srcImg, lower_blue, upper_blue)
                mask1 = cv2.inRange(HSV, lower_h, upper_h)

                mask = cv2.medianBlur(mask, 7)
                mask1 = cv2.medianBlur(mask1, 7)

                cv2.bitwise_not(mask, mask)
                cv2.bitwise_not(mask1,mask1)

                #cv2.imshow('mask', mask)
                #cv2.waitKey(0)

                #cv2.imshow('mask1', mask1)
                #cv2.waitKey(0)

                contours, hierarch = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                if not len(contours):
                    sheet1.write(i, 1, 'Bad picture')
                    sheet1.write(i, 2, 'Bad picture')  # 10-2-short
                    sheet1.write(i, 3, 'Bad picture')  # 10-3-long
                    sheet1.write(i, 4, 'Bad picture')
                    sheet1.write(i, 5, 'Bad picture')
                    sheet1.write(i, 6, 'Bad picture')
                    sheet1.write(i, 7, 'Bad picture')
                    sheet1.write(i, 8, 'Bad picture')
                    sheet1.write(i, 9, 'Bad picture')
                    sheet1.write(i, 10, 'Bad picture')
                    sheet1.write(i, 11, 'Bad picture')
                    sheet1.write(i, 12, 'Bad picture')
                    sheet1.write(i, 13, 'Bad picture')
                    sheet1.write(i, 14, 'Bad picture')
                    break

                area = []
                for j in range(len(contours)):
                    area.append(cv2.contourArea(contours[j]))
                area.sort(reverse=True)
                if area[0] <= 100000:
                    limit_area = area[0]
                else:
                    if len(area) > 1:
                        limit_area = area[1]
                    else:
                        limit_area = 0
                for j in range(len(contours)):
                    if limit_area == 0:
                        sheet1.write(i, 1, 'Bad picture')
                        sheet1.write(i, 2, 'Bad picture')  # 10-2-short
                        sheet1.write(i, 3, 'Bad picture')  # 10-3-long
                        sheet1.write(i, 4, 'Bad picture')
                        sheet1.write(i, 5, 'Bad picture')
                        sheet1.write(i, 6, 'Bad picture')
                        sheet1.write(i, 7, 'Bad picture')
                        sheet1.write(i, 8, 'Bad picture')
                        sheet1.write(i, 9, 'Bad picture')
                        sheet1.write(i, 10, 'Bad picture')
                        sheet1.write(i, 11, 'Bad picture')
                        sheet1.write(i, 12, 'Bad picture')
                        sheet1.write(i, 13, 'Bad picture')
                        sheet1.write(i, 14, 'Bad picture')
                        break
                    if limit_area - 50 <= cv2.contourArea(contours[j]) <= limit_area + 50:
                        #print('check out')
                        #print(contours[j])
                        #cv2.drawContours(srcImg, contours, j, (0,0,255), cv2.FILLED)
                        min_rect = cv2.minAreaRect(contours[j])
                        box = cv2.boxPoints(min_rect)
                        box = np.int0(box)
                        cv2.drawContours(srcImg, [box], 0, (0,255,0), 3)
                        #print('long&width', min_rect[1])
                        #sheet1.write(i,0,VA[llx])
                        sheet1.write(i,1,str(i))  #10-1-frame
                        if min_rect[1][0] < min_rect[1][1]:
                            short = int(min_rect[1][0])
                            long = int(min_rect[1][1])
                        else:
                            short = int(min_rect[1][1])
                            long = int(min_rect[1][0])
                        sheet1.write(i, 2, short)  #10-2-short
                        sheet1.write(i, 3, long)  #10-3-long
                        ccx, ccy = min_rect[0]
                        widd, longg = min_rect[1]
                        if not long == 0:
                            ratio = short / long
                        else:
                            ratio = 0
                            break

                        if short == 0:
                            break
                        #print(round(ratio, 2))
                        #print('ccx&ccy:', ccx, ' ', ccy)
                        sheet1.write(i, 4, round(ratio,2)) #10-4-ratio
                        sheet1.write(i, 5, int(3.1415926 * long * short / 4))

                        #Judge inside a oval or not                 Judge outside a circle or not
                        #(x-cx)^2/a^2 + (y-cx)^2/b^2 <= 1           (x-cx)^2 + (y-cx)^2 >= radius^2
                        #a = long / 2
                        #b = short / 2
                        #cx = ccx, cy = ccy
                        #radius ~ b / 2

                        B_list = []
                        G_list = []
                        R_list = []
                        #print('frame', i)
                        for xx in range(int(ccx - longg / 2), int(ccx + longg / 2)):
                            for yy in range(int(ccy - longg / 2), int(ccy + longg / 2)):
                                oval_j = (xx - ccx)*(xx - ccx) / (long/2) / (long/2) + (yy - ccy)*(yy - ccy) / (short / 2) / (short / 2)
                                circle_j = (xx - ccx)*(xx - ccx) + (yy - ccy)*(yy - ccy)

                                if oval_j <= 0.9:
                                    if circle_j >= (short / 4) * (short / 4):
                                        if 0 < xx < B.shape[0]:
                                            if 0 < yy < B.shape[1]:
                                                if B[yy][xx] < 200 and G[yy][xx] < 200 and R[yy][xx] < 200:
                                                    srcImg[yy][xx] = (0, 255, 0)
                                                #if B[yy][xx] < 200:
                                                    B_list.append(B[yy][xx])
                                                #if G[yy][xx] < 200:
                                                    G_list.append(G[yy][xx])
                                                #if R[yy][xx] < 200:
                                                    R_list.append(R[yy][xx])
                        # print(int(cx-radius*1.5-20), ' ', int(cx-radius*1.5), ' ', int(cy-15), ' ', int(cy+30))
                        # print(len(B_list), ' ', B_list)
                        # print('bm:',np.mean(B_list),'bv:',np.std(B_list),'gm:',np.mean(G_list),'gv:',np.std(G_list),'rm:',np.mean(R_list),'rv:',np.std(R_list))
                        # print(R_list)
                        if len(B_list):
                            rr = int(np.mean(R_list))
                            gg = int(np.mean(G_list))
                            bb = int(np.mean(B_list))
                            if not rr+gg+bb:
                                rp = 0
                                gp = 0
                                bp = 0
                                sheet1.write(i, 6, 'Bad picture')
                                sheet1.write(i, 7, 'Bad picture')
                                sheet1.write(i, 8, 'Bad picture')
                                sheet1.write(i, 9, 'Bad picture')
                                sheet1.write(i, 10, 'Bad picture')
                                sheet1.write(i, 11, 'Bad picture')
                                sheet1.write(i, 12, 'Bad picture')
                                sheet1.write(i, 13, 'Bad picture')
                                sheet1.write(i, 14, 'Bad picture')
                            else:
                                rp = rr / (rr + gg + bb)
                                gp = gg / (rr + gg + bb)
                                bp = bb / (rr + gg + bb)
                                sheet1.write(i, 6, int(np.mean(R_list)))
                                sheet1.write(i, 7, int(np.std(R_list)))
                                sheet1.write(i, 8, int(np.mean(G_list)))
                                sheet1.write(i, 9, int(np.std(G_list)))
                                sheet1.write(i, 10, int(np.mean(B_list)))
                                sheet1.write(i, 11, int(np.std(B_list)))
                                sheet1.write(i, 12, str(int(rp * 100)) + '%')
                                sheet1.write(i, 13, str(int(gp * 100)) + '%')
                                sheet1.write(i, 14, str(int(bp * 100)) + '%')
                        else:
                            sheet1.write(i, 6, 'Bad picture')
                            sheet1.write(i, 7, 'Bad picture')
                            sheet1.write(i, 8, 'Bad picture')
                            sheet1.write(i, 9, 'Bad picture')
                            sheet1.write(i, 10, 'Bad picture')
                            sheet1.write(i, 11, 'Bad picture')
                            sheet1.write(i, 12, 'Bad picture')
                            sheet1.write(i, 13, 'Bad picture')
                            sheet1.write(i, 14, 'Bad picture')



                cv2.imwrite(dstpathName + '/' + 'sdividel' + str(i) + '.jpg', srcImg, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
                #cv2.imshow('Final', srcImg)
                #cv2.waitKey(0)

            print('check point 0')

        if VedioFlag == False:


            for i in range(10, 50):
                srcImg = cv2.imread(pathName + '/' + 'no' + str(i-9) + '.bmp')
                # cv2.imshow('Display', srcImg)
                # cv2.waitKey(0)
                if not len(cv2.split(srcImg)) == 3:
                    break
                B, G, R = cv2.split(srcImg)
                HSV = cv2.cvtColor(srcImg, cv2.COLOR_BGR2HSV)
                # cv2.imshow('HSV', HSV)
                # cv2.waitKey(0)
                H, S, V = cv2.split(HSV)
                # cv2.imshow('B', B) #is useful
                # cv2.waitKey(0)
                # cv2.imshow('G', G)
                # cv2.waitKey(0)
                # cv2.imshow('R', R)
                # cv2.waitKey(0)
                # cv2.imshow('H', H) #is useful
                # cv2.waitKey(0)
                # cv2.imshow('S', S)
                # cv2.waitKey(0)
                # cv2.imshow('V', V)
                # cv2.waitKey(0)
                lower_blue = np.array([150, 132, 107])
                upper_blue = np.array([210, 210, 210])
                lower_h = np.array([102, 0, 0])
                upper_h = np.array([125, 255, 255])

                mask = cv2.inRange(srcImg, lower_blue, upper_blue)
                mask1 = cv2.inRange(HSV, lower_h, upper_h)

                mask = cv2.medianBlur(mask, 7)
                mask1 = cv2.medianBlur(mask1, 7)

                cv2.bitwise_not(mask, mask)
                cv2.bitwise_not(mask1, mask1)

                # cv2.imshow('mask', mask)
                # cv2.waitKey(0)

                # cv2.imshow('mask1', mask1)
                # cv2.waitKey(0)

                contours, hierarch = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                if not len(contours):
                    sheet1.write(i, 1, 'Bad picture')
                    sheet1.write(i, 2, 'Bad picture')  # 10-2-short
                    sheet1.write(i, 3, 'Bad picture')  # 10-3-long
                    sheet1.write(i, 4, 'Bad picture')
                    sheet1.write(i, 5, 'Bad picture')
                    sheet1.write(i, 6, 'Bad picture')
                    sheet1.write(i, 7, 'Bad picture')
                    sheet1.write(i, 8, 'Bad picture')
                    sheet1.write(i, 9, 'Bad picture')
                    sheet1.write(i, 10, 'Bad picture')
                    sheet1.write(i, 11, 'Bad picture')
                    sheet1.write(i, 12, 'Bad picture')
                    sheet1.write(i, 13, 'Bad picture')
                    sheet1.write(i, 14, 'Bad picture')
                    break

                area = []
                for j in range(len(contours)):
                    area.append(cv2.contourArea(contours[j]))
                area.sort(reverse=True)
                if area[0] <= 100000:
                    limit_area = area[0]
                else:
                    if len(area) > 1:
                        limit_area = area[1]
                    else:
                        limit_area = 0
                for j in range(len(contours)):
                    if limit_area == 0:
                        sheet1.write(i, 1, 'Bad picture')
                        sheet1.write(i, 2, 'Bad picture')  # 10-2-short
                        sheet1.write(i, 3, 'Bad picture')  # 10-3-long
                        sheet1.write(i, 4, 'Bad picture')
                        sheet1.write(i, 5, 'Bad picture')
                        sheet1.write(i, 6, 'Bad picture')
                        sheet1.write(i, 7, 'Bad picture')
                        sheet1.write(i, 8, 'Bad picture')
                        sheet1.write(i, 9, 'Bad picture')
                        sheet1.write(i, 10, 'Bad picture')
                        sheet1.write(i, 11, 'Bad picture')
                        sheet1.write(i, 12, 'Bad picture')
                        sheet1.write(i, 13, 'Bad picture')
                        sheet1.write(i, 14, 'Bad picture')
                        break
                    if limit_area - 50 <= cv2.contourArea(contours[j]) <= limit_area + 50:
                        # print('check out')
                        # print(contours[j])
                        # cv2.drawContours(srcImg, contours, j, (0,0,255), cv2.FILLED)
                        min_rect = cv2.minAreaRect(contours[j])
                        box = cv2.boxPoints(min_rect)
                        box = np.int0(box)
                        cv2.drawContours(srcImg, [box], 0, (0, 255, 0), 3)
                        # print('long&width', min_rect[1])
                        # sheet1.write(i,0,VA[llx])
                        sheet1.write(i, 1, str(i))  # 10-1-frame
                        if min_rect[1][0] < min_rect[1][1]:
                            short = int(min_rect[1][0])
                            long = int(min_rect[1][1])
                        else:
                            short = int(min_rect[1][1])
                            long = int(min_rect[1][0])
                        sheet1.write(i, 2, short)  # 10-2-short
                        sheet1.write(i, 3, long)  # 10-3-long
                        ccx, ccy = min_rect[0]
                        widd, longg = min_rect[1]
                        if not long == 0:
                            ratio = short / long
                        else:
                            ratio = 0
                            break

                        if short == 0:
                            break
                        # print(round(ratio, 2))
                        # print('ccx&ccy:', ccx, ' ', ccy)
                        sheet1.write(i, 4, round(ratio, 2))  # 10-4-ratio
                        sheet1.write(i, 5, int(3.1415926 * long * short / 4))

                        # Judge inside a oval or not                 Judge outside a circle or not
                        # (x-cx)^2/a^2 + (y-cx)^2/b^2 <= 1           (x-cx)^2 + (y-cx)^2 >= radius^2
                        # a = long / 2
                        # b = short / 2
                        # cx = ccx, cy = ccy
                        # radius ~ b / 2

                        B_list = []
                        G_list = []
                        R_list = []
                        # print('frame', i)
                        for xx in range(int(ccx - longg / 2), int(ccx + longg / 2)):
                            for yy in range(int(ccy - longg / 2), int(ccy + longg / 2)):
                                oval_j = (xx - ccx) * (xx - ccx) / (long / 2) / (long / 2) + (yy - ccy) * (yy - ccy) / (
                                short / 2) / (short / 2)
                                circle_j = (xx - ccx) * (xx - ccx) + (yy - ccy) * (yy - ccy)

                                if oval_j <= 0.9:
                                    if circle_j >= (short / 4) * (short / 4):
                                        if 0 < xx < B.shape[0]:
                                            if 0 < yy < B.shape[1]:
                                                if B[yy][xx] < 200 and G[yy][xx] < 200 and R[yy][xx] < 200:
                                                    srcImg[yy][xx] = (0, 255, 0)
                                                    # if B[yy][xx] < 200:
                                                    B_list.append(B[yy][xx])
                                                    # if G[yy][xx] < 200:
                                                    G_list.append(G[yy][xx])
                                                    # if R[yy][xx] < 200:
                                                    R_list.append(R[yy][xx])
                        # print(int(cx-radius*1.5-20), ' ', int(cx-radius*1.5), ' ', int(cy-15), ' ', int(cy+30))
                        # print(len(B_list), ' ', B_list)
                        # print('bm:',np.mean(B_list),'bv:',np.std(B_list),'gm:',np.mean(G_list),'gv:',np.std(G_list),'rm:',np.mean(R_list),'rv:',np.std(R_list))
                        # print(R_list)
                        if len(B_list):
                            rr = int(np.mean(R_list))
                            gg = int(np.mean(G_list))
                            bb = int(np.mean(B_list))
                            if not rr + gg + bb:
                                rp = 0
                                gp = 0
                                bp = 0
                                sheet1.write(i, 6, 'Bad picture')
                                sheet1.write(i, 7, 'Bad picture')
                                sheet1.write(i, 8, 'Bad picture')
                                sheet1.write(i, 9, 'Bad picture')
                                sheet1.write(i, 10, 'Bad picture')
                                sheet1.write(i, 11, 'Bad picture')
                                sheet1.write(i, 12, 'Bad picture')
                                sheet1.write(i, 13, 'Bad picture')
                                sheet1.write(i, 14, 'Bad picture')
                            else:
                                rp = rr / (rr + gg + bb)
                                gp = gg / (rr + gg + bb)
                                bp = bb / (rr + gg + bb)
                                sheet1.write(i, 6, int(np.mean(R_list)))
                                sheet1.write(i, 7, int(np.std(R_list)))
                                sheet1.write(i, 8, int(np.mean(G_list)))
                                sheet1.write(i, 9, int(np.std(G_list)))
                                sheet1.write(i, 10, int(np.mean(B_list)))
                                sheet1.write(i, 11, int(np.std(B_list)))
                                sheet1.write(i, 12, str(int(rp * 100)) + '%')
                                sheet1.write(i, 13, str(int(gp * 100)) + '%')
                                sheet1.write(i, 14, str(int(bp * 100)) + '%')
                        else:
                            sheet1.write(i, 6, 'Bad picture')
                            sheet1.write(i, 7, 'Bad picture')
                            sheet1.write(i, 8, 'Bad picture')
                            sheet1.write(i, 9, 'Bad picture')
                            sheet1.write(i, 10, 'Bad picture')
                            sheet1.write(i, 11, 'Bad picture')
                            sheet1.write(i, 12, 'Bad picture')
                            sheet1.write(i, 13, 'Bad picture')
                            sheet1.write(i, 14, 'Bad picture')

                cv2.imwrite(dstpathName + '/' + 'sdividel' + str(i) + '.jpg', srcImg,
                            [int(cv2.IMWRITE_JPEG_QUALITY), 95])
                # cv2.imshow('Final', srcImg)
                # cv2.waitKey(0)

            print('check point 0')



        #The first part finished
        #Let's go to the second part
        #Now we use the pl pictures
        f_l = getBmpFile.getBmpFile(pathName)
        #print(f_l)
        for i in range(len(f_l)):
            #print(f_l[i])
            srcImage = cv2.imread(pathName + '/' + f_l[i])
            #cv2.imshow('No', srcImage)
            #cv2.waitKey(0)
            B, G, R = cv2.split(srcImage)
            HSV = cv2.cvtColor(srcImage, cv2.COLOR_BGR2HSV)
            #cv2.imshow('HSV', HSV)
            #cv2.waitKey(0)
            H, S, V = cv2.split(HSV)
            # cv2.imshow('B', B) #is useful
            # cv2.waitKey(0)
            # cv2.imshow('G', G)
            # cv2.waitKey(0)
            # cv2.imshow('R', R)
            # cv2.waitKey(0)
            # cv2.imshow('H', H) #is useful
            # cv2.waitKey(0)
            # cv2.imshow('S', S)
            # cv2.waitKey(0)
            # cv2.imshow('V', V)
            # cv2.waitKey(0)
            lower = np.array([235, 0, 0])
            upper = np.array([255, 255, 255])
            masks = cv2.inRange(srcImage, lower, upper)

            #cv2.imshow('M', masks)
            #cv2.waitKey(0)

            cv2.bitwise_not(masks, masks)
            contours, _ = cv2.findContours(masks, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            area = []
            for j in range(len(contours)):
                area.append(cv2.contourArea(contours[j]))
            area.sort(reverse=True)
            if area[0] <= 100000:
                limit_area = area[0]
            else:
                if len(area) > 1:
                    limit_area = area[1]
                else:
                    limit_area = 0
            for j in range(len(contours)):
                if limit_area == 0:
                    sheet1.write(i + 10, 15, 'Bad picture')
                    sheet1.write(i + 10, 16, 'Bad picture')
                    sheet1.write(i + 10, 17, 'Bad picture')
                    sheet1.write(i + 10, 18, 'Bad picture')
                    sheet1.write(i + 10, 19, 'Bad picture')
                    sheet1.write(i + 10, 20, 'Bad picture')
                    sheet1.write(i + 10, 21, 'Bad picture')
                    sheet1.write(i + 10, 22, 'Bad picture')
                    sheet1.write(i + 10, 23, 'Bad picture')
                    sheet1.write(i + 10, 24, 'Bad picture')
                    sheet1.write(i + 10, 25, 'Bad picture')
                    sheet1.write(i + 10, 26, 'Bad picture')
                    break
                if limit_area - 5 <= cv2.contourArea(contours[j]) <= limit_area + 5:
                    # print('check out')
                    # print(contours[j])
                    # cv2.drawContours(srcImage, contours, j, (0,0,255), cv2.FILLED)
                    min_rect = cv2.minAreaRect(contours[j]) #Find the center area
                    # print(min_rect[0])
                    x, y = min_rect[0]
                    #cv2.imshow('show', srcImage)
                    #cv2.waitKey(0)

                    circle = np.zeros(srcImage.shape[:2], dtype="uint8")
                    cv2.circle(circle, (int(x), int(y)), 50, 255, -1)
                    #cv2.imshow("Circle", circle)
                    #cv2.waitKey(0)

                    gray = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
                    masked = cv2.bitwise_and(gray, gray, mask=circle)
                    #cv2.imshow('masked', masked)
                    #cv2.waitKey(0)

                    ret, thresh1 = cv2.threshold(masked, 140, 255, cv2.THRESH_BINARY)
                    #cv2.bitwise_not(thresh1, thresh1)
                    #cv2.imshow('thresh1', thresh1)
                    #cv2.waitKey(0)

                    second_contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    #print(len(second_contours))
                    #Thought out a new method to merge the points
                    if not len(second_contours):
                        break
                    total_c = np.vstack((second_contours[m] for m in range(len(second_contours))))
                    #print(total_c)
                    (cx,cy), radius = cv2.minEnclosingCircle(total_c)
                    cv2.circle(srcImage, (int(cx),int(cy)), int(radius), (0, 255, 0), 3)
                    #print(cx, ' ', cy, ' ', radius)

                    #Left one                     Right one
                    #x - radius * 1.5 - 20        x + radius * 1.5
                    #y - 15                       y - 15
                    #x - radius * 1.5             x + radius * 1.5 + 20
                    #y + 30                       y + 30
                    cv2.rectangle(srcImage, (int(cx-radius*1.5-20), int(cy-15)), (int(cx-radius*1.5), int(cy+30)), (0,255,0), 3)
                    cv2.rectangle(srcImage, (int(cx+radius*1.5), int(cy-15)), (int(cx+radius*1.5+20), int(cy+30)), (0,255,0), 3)


                    #cv2.waitKey(0)
                    #print(B)
                    B_list = []
                    G_list = []
                    R_list = []
                    for xx in range(int(cx-radius*1.5-20), int(cx-radius*1.5)):
                        for yy in range(int(cy-15), int(cy+30)):
                            if 0 < xx < B.shape[1]:
                                if 0 < yy < B.shape[0]:
                                    srcImage[yy][xx] = (255,0,0)
                                    B_list.append(B[yy][xx])
                                    G_list.append(G[yy][xx])
                                    R_list.append(R[yy][xx])

                    for xx in range(int(cx + radius * 1.5), int(cx + radius * 1.5 + 20)):
                        for yy in range(int(cy - 15), int(cy + 30)):
                            if 0 < xx < B.shape[1]:
                                if 0 < yy < B.shape[0]:
                                    srcImage[yy][xx] = (255, 0, 0)
                                    B_list.append(B[yy][xx])
                                    G_list.append(G[yy][xx])
                                    R_list.append(R[yy][xx])
                    #print(int(cx-radius*1.5-20), ' ', int(cx-radius*1.5), ' ', int(cy-15), ' ', int(cy+30))
                    #print(len(B_list), ' ', B_list)
                    #print('bm:',np.mean(B_list),'bv:',np.std(B_list),'gm:',np.mean(G_list),'gv:',np.std(G_list),'rm:',np.mean(R_list),'rv:',np.std(R_list))
                    #cv2.imshow('Final', srcImage)
                    cv2.imwrite(dstpathName + '/' + 'pl' + str(i) + '.jpg', srcImage, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
                    if len(B_list):
                        rr = int(np.mean(R_list))
                        gg = int(np.mean(G_list))
                        bb = int(np.mean(B_list))
                        rp = rr / (rr + gg + bb)
                        gp = gg / (rr + gg + bb)
                        bp = bb / (rr + gg + bb)
                        sheet1.write(i + 10, 15, int(cx))
                        sheet1.write(i + 10, 16, int(cy))
                        sheet1.write(i + 10, 17, int(radius))
                        sheet1.write(i + 10, 18, int(np.mean(R_list)))
                        sheet1.write(i + 10, 19, int(np.std(R_list)))
                        sheet1.write(i + 10, 20, int(np.mean(G_list)))
                        sheet1.write(i + 10, 21, int(np.std(G_list)))
                        sheet1.write(i + 10, 22, int(np.mean(B_list)))
                        sheet1.write(i + 10, 23, int(np.std(B_list)))
                        sheet1.write(i + 10, 24, str(int(rp * 100)) + '%')
                        sheet1.write(i + 10, 25, str(int(gp * 100)) + '%')
                        sheet1.write(i + 10, 26, str(int(bp * 100)) + '%')
                    else:
                        sheet1.write(i + 10, 15, 'Bad picture')
                        sheet1.write(i + 10, 16, 'Bad picture')
                        sheet1.write(i + 10, 17, 'Bad picture')
                        sheet1.write(i + 10, 18, 'Bad picture')
                        sheet1.write(i + 10, 19, 'Bad picture')
                        sheet1.write(i + 10, 20, 'Bad picture')
                        sheet1.write(i + 10, 21, 'Bad picture')
                        sheet1.write(i + 10, 22, 'Bad picture')
                        sheet1.write(i + 10, 23, 'Bad picture')
                        sheet1.write(i + 10, 24, 'Bad picture')
                        sheet1.write(i + 10, 25, 'Bad picture')
                        sheet1.write(i + 10, 26, 'Bad picture')

        book.save(dstpathName + '/res.xls')
