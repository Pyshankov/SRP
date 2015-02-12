# -*- coding: cp1251 -*-
 #!/usr/bin/python
# -*-coding:utf-8-*-

import codecs

from Function import *#read,download,remov,read_and_find_max,read_and_find_drought,read_and_find_min

area = ["Cherkasy","Chernihiv","Chernivci","Crimea","Dnipropetrovs'k","Donets'k","Ivano-Frankivs'k","Kharkiv","Kherson",
        "Khmel'nyts'kyy","Kiev","Kiev City","Kirovohrad","Luhans'k"," L'viv","Mykolayiv","Odessa","Poltava"," Rivne",
        "Sevastopol'","Sumy","Ternopil'","Transcarpathia","Vinnytsya","Volyn","Zaporizhzhya","Zhytomyr"]

area.sort()

areaNumber=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
            '22','23','24','25','26','27']


downtime=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
            '22','23','24','25','26','27']
remov("Download")



p = u'абвгдежзийкл'  # note the 'u' prefix
print p

i = 0
while i<len(areaNumber):
    downtime[i] = download(areaNumber[i],area[i])
    i=i+1


i=13
# print read_and_find_max("%s.csv"%(areaNumber[i]+" "+area[i]+" "+downtime[i]),1985)
# print read_and_find_min("%s.csv"%(areaNumber[i]+" "+area[i]+" "+downtime[i]),1981)
#
# print read_and_find_drought("%s.csv"%(areaNumber[i]+" "+area[i]+" "+downtime[i]),15)

i=0
while i<len(areaNumber):
    print "%s.csv"%(areaNumber[i]+" "+area[i]+" "+downtime[i])
    print read_and_find_drought_max("%s.csv"%(areaNumber[i]+" "+area[i]+" "+downtime[i]),15)
    i=i+1
