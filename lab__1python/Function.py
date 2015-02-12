__author__ = 'pyshankov'
import pandas as pd
import urllib2
import os
import glob
from time import gmtime, strftime
#coding: utf-8
def read (fileName):
    df = pd.read_csv( "Download/%s"%fileName ,index_col=False, header=1)
    print list(df.columns.values)
   # print df[:3]



def read_and_find_max(fileName,year):
    df = pd.read_csv('Download/%s'%fileName,index_col=False, header=1)

    yr=df[df['year']==year]
    print "in %s max value VHI:"%year
    max1 = max(yr.VHI)

    return max1



def read_and_find_min(fileName,year):
    df = pd.read_csv('Download/%s'%fileName,index_col=False, header=1)
    yr=df[df['year']==year]
    print "in %s min value VHI:"%year
    min1 = min(yr.VHI)

    return min1



def read_and_find_drought(fileName,percent):
    df = pd.read_csv('Download/%s'%fileName,index_col=False, header=1)
    a=df[(df['VHI']<=percent) & (df['VHI']>=0)]
    print "drought on this area"
    return a

def read_and_find_drought_max(fileName,percent):
    #str1 = '%Area_VHI_LESS_15'
    df = pd.read_csv('Download/%s'%fileName,index_col=False, header=1)
    a=df[(df['VHI']<=percent) & (df['VHI']>=0)]
    #max1=max(a["%Area_VHI_LESS_15"])
    z=df[  df["%Area_VHI_LESS_15"]==max(df["%Area_VHI_LESS_15"])]
    print "drought on this area max"
    return z

def download(areaNumber,area):
    url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R%s.txt" %areaNumber
    vhi_url = urllib2.urlopen(url)
    time=strftime("%Y-%m-%d %H:%M:%S", gmtime())
    out = open('Download/%s.csv'%(areaNumber+" "+area+' '+time),'wb')
    out.write(vhi_url.read())
    out.close()
    return time




def remov(path):
    files = glob.glob('%s/*'%path)
    for f in files:
        os.remove(f)
