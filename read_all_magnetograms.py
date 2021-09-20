import shutil
import os
from datetime import datetime
import numpy as np


DATES=['CME_2014-12-21','CME_2014-12-23','CME_2014-09-11','CME_2014-09-12','CME_2014-07-02'
,'CME_2014-06-23','CME_2014-06-07','CME1_2015-06-22','CME2_2015-06-22','CME_2015-03-17'
,'CME_2015-12-19','CME_2015-11-04','CME_2015-09-20','CME_2015-08-15','CME_2015-06-25'
,'CME_2015-06-24','CME_2015-06-21','CME_2015-05-06','CME_2016-03-14','CME_2016-01-18'
,'CME_2016-11-09','CME_2016-10-12','CME_2016-07-19','CME_2017-10-24','CME_2017-05-27'
,'CME_2017-07-08']

for folder in DATES:

    file_list = []    
    file_list = os.listdir('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/'+str(folder)+'/magnetograms/')


    files = []
    files = [x for x in file_list if ".sec" in x]

    a=[]
    listOfLines = list()
    #filepath + filename
    for name in sorted(files):
        print(name)
        with open('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/'+str(folder)+'/magnetograms/' + name) as fn:
            lines = fn.readlines()
            #print (lines[0])
            for line in lines:
                if line[:4].isdigit():
                    #print(line)
                    p=line.split()
                    a.append(p)
            #for line in fn:
            #    listOfLines.append(line.strip())            

    def Extract(lst): 
        for i in range (0,6):
            return [item[i] for item in lst] 

    datum=[]
    cas=[]
    Bx=[]
    By=[]
    Bz=[]
    for line in range(len(a)):
        for item in range(0,6):
            if item == 0 :
                datum.append(a[line][item])
            if item == 1 :
                cas.append(a[line][item])
            if item == 3:
                Bx.append(a[line][item])
            if item == 4:
                By.append(a[line][item])
            if item == 5:
                Bz.append(a[line][item])

    np.savetxt('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/'+str(folder)+'/magnetograms/m_'+str(folder)+'_sec.txt', np.transpose([datum,cas,Bx,By,Bz]),fmt='%s %s %s %s %s', delimiter=' ')


    #join=[str(datum[i])+' '+str(cas[i])for i in range(len(datum)) ]

    #datetime_object=[]
    #for i in range(len(join)):
    #    datetime_object.append(datetime.strptime(join[i], '%Y-%m-%d %H:%M:%S.%f'))





