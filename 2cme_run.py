from datetime import datetime,timedelta
import pandas as pd
#from dateutil import parser

def parsefile(filename):
    fhandle=open(filename,'r')
    lines=fhandle.readlines()
    fhandle.close()
    retarr=[]
    for line in lines:
        p=line.split()
        retarr.append((p[0]))
    return retarr


# final_time_lag=[56,
#                 38,30,50,63,53,62,26,40,68,48,52,
#                 43,65,61,157,69,52,44,56,33,47,69,70,52,44,
#                 51,46,32,79,54,43,38,32,45,50,46,45,49,
#                 37,36,58,39,56,61,39,64,43,34,53,45,57,37,
#                 44,28,48,40,29,46,50,30,27,44,49,
#                 62,41,62,60,53,   
#                 30,58,67]

final_time_lag=[1120,
                760, 600, 1000, 1260, 1060, 1240, 520, 800, 1360, 960, 1040,
                860, 1300, 1220, 3140, 1380, 1040, 880, 1120, 660, 940, 1380, 1400, 1040, 880, 
                1020, 920, 640, 1580, 1080, 860, 760, 640, 900, 1000, 920, 900, 
                980, 740, 720, 1160, 780, 1120, 1220, 780, 1280, 860, 680, 1060, 900, 1140,
                740, 880, 560, 960, 800, 580, 920, 1000, 600, 540, 880,
                980, 1240, 820, 1240, 1200,
                1060, 600, 1160, 1340]
time_shift=560

symh_before_110=[]
symh_after_90=[]
symh_before=[]
symh_after=[]
SI_slope=[]
SI_size=[]
vx_glob=[]
vx_jump_size=[]
n_glob=[]
n_jump_size=[]
pd_jump_size=[]



IP_date_file= ['CME_2010-02-15/WI_H0_MFI_API_CME_2010-02-15.txt' #53 min OK
    ,'CME_2011-08-04/WI_H0_MFI_API_CME_2011-08-04.txt', #38 min OK
    'CME_2011-08-05/WI_H0_MFI_API_CME_2011-08-05.txt', #30 min,  OK ALE SKAREDE DATA
    'CME_2011-11-12/WI_H0_MFI_API_CME_2011-11-12.txt', #50 min
    'CME_2011-11-11/WI_H0_MFI_API_CME_2011-11-11.txt', #63 min 
    'CME_2011-09-26/WI_H0_MFI_API_CME_2011-09-26.txt', #53 min DIVNE
    'CME_2011-09-25/WI_H0_MFI_API_CME_2011-09-25.txt', #62 min DIVNE
    'CME_2011-07-11/WI_H0_MFI_API_CME_2011-07-11.txt', #26 min DIVNE
    'CME_2011-06-04/WI_H0_MFI_API_CME_2011-06-04.txt', #40 min TIEZ  SA TO UPLNE NEZHLADI
    'CME_2011-04-18/WI_H0_MFI_API_CME_2011-04-18.txt', #68 min
    'CME_2011-02-18/WI_H0_MFI_API_CME_2011-02-18.txt', #48 min JE TO POSTACUJUCE????, SI SA MUSI POSUNUT O 2 MIN
    'CME_2011-02-14/WI_H0_MFI_API_CME_2011-02-14.txt', #52 min JEDINE PEKNE!!!!

    'CME_2012-11-26/WI_H0_MFI_API_CME_2012-11-26.txt', #43 min OK
    'CME_2012-11-23/WI_H0_MFI_API_CME_2012-11-23.txt', #65 min OK
    'CME_2012-11-12/WI_H0_MFI_API_CME_2012-11-12.txt', #61 min DIVNE
    'CME_2012-10-31/WI_H0_MFI_API_CME_2012-10-31.txt', #157 min OK
    'CME_2012-10-08/WI_H0_MFI_API_CME_2012-10-08.txt', #69 min OK
    'CME_2012-09-30/WI_H0_MFI_API_CME_2012-09-30.txt', #52 min OK
    'CME_2012-09-04/WI_H0_MFI_API_CME_2012-09-04.txt', #44 min NIE SHOCK
    'CME_2012-09-03/WI_H0_MFI_API_CME_2012-09-03.txt', #56 min DIVNE UKAZAT, PRENAHRAT DATA
    'CME_2012-07-14/WI_H0_MFI_API_CME_2012-07-14.txt', #33 min OK?
    'CME_2012-06-16/WI_H0_MFI_API_CME_2012-06-16.txt', #47 min OK?
    'CME_2012-05-21/WI_H0_MFI_API_CME_2012-05-21.txt', #69 min OK?
    'CME_2012-04-23/WI_H0_MFI_API_CME_2012-04-23.txt', #70 min OK ?
    'CME_2012-03-07/WI_H0_MFI_API_CME_2012-03-07.txt', #52 min OK
    'CME_2012-01-22/WI_H0_MFI_API_CME_2012-01-22.txt', #44 min OK?

    'CME_2013-08-20/WI_H0_MFI_API_CME_2013-08-20.txt', #51 min OK? 
    'CME_2013-05-24/WI_H0_MFI_API_CME_2013-05-24.txt', #46 min KRASNY SHOCK ALE DIVNY SYM_H???
    'CME_2013-05-25/WI_H0_MFI_API_CME_2013-05-25.txt', #32 min OK?
    'CME_2013-05-31/WI_H0_MFI_API_CME_2013-05-31.txt', #79 min OK?
    'CME_2013-12-13/WI_H0_MFI_API_CME_2013-12-13.txt', #54 min OK?
    'CME_2013-10-02/WI_H0_MFI_API_CME_2013-10-02.txt', #43 min OK?
    'CME_2013-07-18/WI_H0_MFI_API_CME_2013-07-18.txt', #38 min OK?
    'CME_2013-07-12/WI_H0_MFI_API_CME_2013-07-12.txt', #32 min OK?
    'CME_2013-07-09/WI_H0_MFI_API_CME_2013-07-09.txt', #45 min OK?
    'CME_2013-06-27/WI_H0_MFI_API_CME_2013-06-27.txt', #50 min OK?
    'CME_2013-04-13/WI_H0_MFI_API_CME_2013-04-13.txt', #46 min OK?
    'CME_2013-03-17/WI_H0_MFI_API_CME_2013-03-17.txt', #45 min ZLE DATA, ZOBER Z WI_H1_SWE
    'CME_2013-02-16/WI_H0_MFI_API_CME_2013-02-16.txt', #49 min OK?


    'CME_2014-12-21/WI_H0_MFI_API_CME_2014-12-21.txt', #37 min OK? 
    'CME_2014-12-23/WI_H0_MFI_API_CME_2014-12-23.txt', #36 min OK? UKAZAT!
    'CME_2014-09-11/WI_H0_MFI_API_CME_2014-09-11.txt', #58 min OK? UKAZAT! 
    'CME_2014-09-12/WI_H0_MFI_API_CME_2014-09-12.txt', #39 min OK?
    'CME_2014-07-02/WI_H0_MFI_API_CME_2014-07-02.txt', #56 min OK?
    'CME_2014-07-06/WI_H0_MFI_API_CME_2014-07-06.txt', #61 min OK? UKAZAT!
    'CME_2014-02-20/WI_H0_MFI_API_CME_2014-02-20.txt', #39 min ZLE DATA, ZOBER Z WI_H1_SWE
    'CME_2014-02-27/WI_H0_MFI_API_CME_2014-02-27.txt', #64 min OK? UKAZAT
    'CME_2014-01-07/WI_H0_MFI_API_CME_2014-01-07.txt', #43 min OK, PEKNE
    'CME_2014-01-09/WI_H0_MFI_API_CME_2014-01-09.txt', #34 min OK?
    'CME_2014-06-23/WI_H0_MFI_API_CME_2014-06-23.txt', #53 min OK?
    'CME_2014-06-07/WI_H0_MFI_API_CME_2014-06-07.txt', #45 min OK?
    'CME_2014-03-25/WI_H0_MFI_API_CME_2014-03-25.txt', #57 min OK?

    'CME1_2015-06-22/WI_H0_MFI_API_CME1_2015-06-22.txt', #44 min OK 
    'CME2_2015-06-22/WI_H0_MFI_API_CME2_2015-06-22.txt', #28 min OK
    'CME_2015-03-17/WI_H0_MFI_API_CME_2015-03-17.txt', #48 min OK
    'CME_2015-12-19/WI_H0_MFI_API_CME_2015-12-19.txt', #40 min OK
    'CME_2015-11-04/WI_H0_MFI_API_CME_2015-11-04.txt', #29 min ZOBER Z WI_H1_SWE?
    'CME_2015-09-20/WI_H0_MFI_API_CME_2015-09-20.txt', #46 min OK
    'CME_2015-08-15/WI_H0_MFI_API_CME_2015-08-15.txt', #50 min OK
    'CME_2015-06-25/WI_H0_MFI_API_CME_2015-06-25.txt', #30 min ZMENIT NA 2015-06-24, 13:04, WI_H1_SWE
    'CME_2015-06-24/WI_H0_MFI_API_CME_2015-06-24.txt', #27 min OK
    'CME_2015-06-21/WI_H0_MFI_API_CME_2015-06-21.txt', #44 min OK
    'CME_2015-05-06/WI_H0_MFI_API_CME_2015-05-06.txt', #49 min OK

    'CME_2016-03-14/WI_H0_MFI_API_CME_2016-03-14.txt', #62 min OK 
    'CME_2016-01-18/WI_H0_MFI_API_CME_2016-01-18.txt', #41 min OK WI_H1_SWE
    'CME_2016-11-09/WI_H0_MFI_API_CME_2016-11-09.txt', #62 min OK
    'CME_2016-10-12/WI_H0_MFI_API_CME_2016-10-12.txt', #60 min OK

    'CME_2016-07-19/WI_H0_MFI_API_CME_2016-07-19.txt', #53 min OK

    'CME_2017-10-24/WI_H0_MFI_API_CME_2017-10-24.txt', #25 min OK
    'CME_2017-05-27/WI_H0_MFI_API_CME_2017-05-27.txt', #58 min OK
    'CME_2017-07-08/WI_H0_MFI_API_CME_2017-07-08.txt' #67 min OK
]


flog= open('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/tables/table_with_SC_jump.tex',"w+")
flog.write('IP DATE & SC jump value & speed& Bz\\\\ \n')
flog.write('\\hline \n') 

SHOCK_date=[]

for ind_shock,each_file in enumerate(IP_date_file):
    #print(final_time_lag[ind_shock])
    sep='/'
    IP_date=(each_file.split(sep,1)[0])  
    SHOCK_date.append(IP_date)       
    #filein='/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/'+str(each_file) 
    filein='/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/'+str(each_file)  

    execfile('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/data_codes/codes/2cme_exectute.py')
flog.close()


#df = pd.DataFrame({ "Shock date" : SHOCK_date , "SI slope" : SI_slope, "SI size" : SI_size , "SYM-H before" : symh_before
#, "SYM-H before 110%" : symh_before_110 , "SYM-H after" : symh_after , "SYM-H ater 90%" : symh_after_90
#,"vx jump size" : vx_jump_size, "n jump size" : n_jump_size, "pd jump size" : pd_jump_size , "DB mag" : DB_mag, "sqrt DB mag" : sqrt_DB_mag})


#df.to_csv("/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/SI_SYMH/SI_slope.csv", index=False)


#WI_H1_SWE stahuj data z tadeto
    
  


