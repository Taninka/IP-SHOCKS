from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace, sum
import scipy
import matplotlib.cm as cm
from scipy import integrate
from scipy import signal
import matplotlib.dates as mdates
from matplotlib.colors import ListedColormap
import scipy.interpolate as interp
import matplotlib.ticker as plticker
import math
import pandas as pd
from itertools import combinations
import operator
import statistics 
from statistics import mean
from scipy.stats import pearsonr, spearmanr, kendalltau
import seaborn as sn
import matplotlib.ticker as mtick
from statistics import mean
from statistics import median

int_values = list(range(7, 20))

corr_7 = [] 
corr_8 = []
corr_9 = []
corr_10 = []
corr_11 = []
corr_12 = []
corr_13 = []
corr_14 = []
corr_15 = []
corr_16 = []
corr_17 = []
corr_18 = []
corr_19 = []

corr_7_corr = [] 
corr_8_corr = []
corr_9_corr = []
corr_10_corr = []
corr_11_corr = []
corr_12_corr = []
corr_13_corr = []
corr_14_corr = []
corr_15_corr = []
corr_16_corr = []
corr_17_corr = []
corr_18_corr = []
corr_19_corr = []

lag_7 = [] 
lag_8 = []
lag_9 = []
lag_10 = []
lag_11 = []
lag_12 = []
lag_13 = []
lag_14 = []
lag_15 = []
lag_16 = []
lag_17 = []
lag_18 = []
lag_19 = []

lag_7_corr = [] 
lag_8_corr = []
lag_9_corr = []
lag_10_corr = []
lag_11_corr = []
lag_12_corr = []
lag_13_corr = []
lag_14_corr = []
lag_15_corr = []
lag_16_corr = []
lag_17_corr = []
lag_18_corr = []
lag_19_corr = []

min_symh=[]
symh_at_ip=[]
max_int=[]

min_symh_corr=[]
symh_at_ip_corr=[]
max_int_corr=[]

IP_date_file = ['CME_2010-02-15/WI_H0_MFI_CME_2010-02-15.txt', #56 min

    'CME_2011-08-04/WI_H0_MFI_CME_2011-08-04.txt', #38 min OK
    'CME_2011-08-05/WI_H0_MFI_CME_2011-08-05.txt', #30 min,  OK ALE SKAREDE DATA
    'CME_2011-11-12/WI_H0_MFI_CME_2011-11-12.txt', #50 min
    'CME_2011-11-11/WI_H0_MFI_CME_2011-11-11.txt', #63 min 
    'CME_2011-09-26/WI_H0_MFI_CME_2011-09-26.txt', #53 min DIVNE
    'CME_2011-09-25/WI_H0_MFI_CME_2011-09-25.txt', #62 min DIVNE
    'CME_2011-07-11/WI_H0_MFI_CME_2011-07-11.txt', #26 min DIVNE
    'CME_2011-06-04/WI_H0_MFI_CME_2011-06-04.txt', #40 min TIEZ  SA TO UPLNE NEZHLADI
    'CME_2011-04-18/WI_H0_MFI_CME_2011-04-18.txt', #68 min
    'CME_2011-02-18/WI_H0_MFI_CME_2011-02-18.txt', #48 min JE TO POSTACUJUCE????
    'CME_2011-02-14/WI_H0_MFI_CME_2011-02-14.txt', #52 min JEDINE PEKNE!!!!

    'CME_2012-11-26/WI_H0_MFI_CME_2012-11-26.txt', #43 min OK
    'CME_2012-11-23/WI_H0_MFI_CME_2012-11-23.txt', #65 min OK
    'CME_2012-11-12/WI_H0_MFI_CME_2012-11-12.txt', #61 min DIVNE
    'CME_2012-10-31/WI_H0_MFI_CME_2012-10-31.txt', #157 min OK
    'CME_2012-10-08/WI_H0_MFI_CME_2012-10-08.txt', #69 min OK
    'CME_2012-09-30/WI_H0_MFI_CME_2012-09-30.txt', #52 min OK
    'CME_2012-09-04/WI_H0_MFI_CME_2012-09-04.txt', #44 min NIE SHOCK
    'CME_2012-09-03/WI_H0_MFI_CME_2012-09-03.txt', #56 min DIVNE UKAZAT, PRENAHRAT DATA
    'CME_2012-07-14/WI_H0_MFI_CME_2012-07-14.txt', #33 min OK?
    'CME_2012-06-16/WI_H0_MFI_CME_2012-06-16.txt', #47 min OK?
    'CME_2012-05-21/WI_H0_MFI_CME_2012-05-21.txt', #69 min OK?
    'CME_2012-04-22/WI_H0_MFI_CME_2012-04-22.txt', #70 min OK ?
    'CME_2012-03-07/WI_H0_MFI_CME_2012-03-07.txt', #52 min OK
    'CME_2012-01-22/WI_H0_MFI_CME_2012-01-22.txt', #44 min OK?

    'CME_2013-08-20/WI_H0_MFI_CME_2013-08-20.txt', #51 min OK? 
    'CME_2013-05-24/WI_H0_MFI_CME_2013-05-24.txt', #46 min KRASNY SHOCK ALE DIVNY SYM_H???
    'CME_2013-05-25/WI_H0_MFI_CME_2013-05-25.txt', #32 min OK?
    'CME_2013-05-31/WI_H0_MFI_CME_2013-05-31.txt', #79 min OK?
    'CME_2013-12-13/WI_H0_MFI_CME_2013-12-13.txt', #54 min OK?
    'CME_2013-10-02/WI_H0_MFI_CME_2013-10-02.txt', #43 min OK?
    'CME_2013-07-18/WI_H0_MFI_CME_2013-07-18.txt', #38 min OK?
    'CME_2013-07-12/WI_H0_MFI_CME_2013-07-12.txt', #32 min OK?
    'CME_2013-07-09/WI_H0_MFI_CME_2013-07-09.txt', #45 min OK?
    'CME_2013-06-27/WI_H0_MFI_CME_2013-06-27.txt', #50 min OK?
    'CME_2013-04-13/WI_H0_MFI_CME_2013-04-13.txt', #46 min OK?
    'CME_2013-03-17/WI_H0_MFI_CME_2013-03-17.txt', #45 min ZLE DATA, ZOBER Z WI_H1_SWE
    'CME_2013-02-16/WI_H0_MFI_CME_2013-02-16.txt', #49 min OK?


    'CME_2014-12-21/WI_H0_MFI_CME_2014-12-21.txt', #37 min OK? 
    'CME_2014-12-23/WI_H0_MFI_CME_2014-12-23.txt', #36 min OK? UKAZAT!
    'CME_2014-09-11/WI_H0_MFI_CME_2014-09-11.txt', #58 min OK? UKAZAT! 
    'CME_2014-09-12/WI_H0_MFI_CME_2014-09-12.txt', #39 min OK?
    'CME_2014-07-02/WI_H0_MFI_CME_2014-07-02.txt', #56 min OK?
    'CME_2014-07-06/WI_H0_MFI_CME_2014-07-06.txt', #61 min OK? UKAZAT!
    'CME_2014-02-20/WI_H0_MFI_CME_2014-02-20.txt', #39 min ZLE DATA, ZOBER Z WI_H1_SWE
    'CME_2014-02-27/WI_H0_MFI_CME_2014-02-27.txt', #64 min OK? UKAZAT
    'CME_2014-01-07/WI_H0_MFI_CME_2014-01-07.txt', #43 min OK, PEKNE
    'CME_2014-01-09/WI_H0_MFI_CME_2014-01-09.txt', #34 min OK?
    'CME_2014-06-23/WI_H0_MFI_CME_2014-06-23.txt', #53 min OK?
    'CME_2014-06-07/WI_H0_MFI_CME_2014-06-07.txt', #45 min OK?
    'CME_2014-03-25/WI_H0_MFI_CME_2014-03-25.txt', #57 min OK?
    'CME_2014-02-18/WI_H0_MFI_CME_2014-02-18.txt', #37 min OK

    'CME1_2015-06-22/WI_H0_MFI_CME1_2015-06-22.txt', #44 min OK 
    'CME2_2015-06-22/WI_H0_MFI_CME2_2015-06-22.txt', #28 min OK
    'CME_2015-03-17/WI_H0_MFI_CME_2015-03-17.txt', #48 min OK
    'CME_2015-12-19/WI_H0_MFI_CME_2015-12-19.txt', #40 min OK
    'CME_2015-11-04/WI_H0_MFI_CME_2015-11-04.txt', #29 min ZOBER Z WI_H1_SWE?
    'CME_2015-09-20/WI_H0_MFI_CME_2015-09-20.txt', #46 min OK
    'CME_2015-08-15/WI_H0_MFI_CME_2015-08-15.txt', #50 min OK
    'CME_2015-06-25/WI_H0_MFI_CME_2015-06-25.txt', #30 min ZMENIT NA 2015-06-24, 13:04, WI_H1_SWE
    'CME_2015-06-24/WI_H0_MFI_CME_2015-06-24.txt', #27 min OK
    'CME_2015-06-21/WI_H0_MFI_CME_2015-06-21.txt', #44 min OK
    'CME_2015-05-06/WI_H0_MFI_CME_2015-05-06.txt', #49 min OK

    'CME_2016-03-14/WI_H0_MFI_CME_2016-03-14.txt', #62 min OK 
    'CME_2016-01-18/WI_H0_MFI_CME_2016-01-18.txt', #41 min OK WI_H1_SWE
    'CME_2016-11-09/WI_H0_MFI_CME_2016-11-09.txt', #62 min OK
    'CME_2016-10-12/WI_H0_MFI_CME_2016-10-12.txt', #60 min OK
    'CME_2016-07-19/WI_H0_MFI_CME_2016-07-19.txt', #53 min OK

    'CME_2017-10-24/WI_H0_MFI_CME_2017-10-24.txt', #25 min OK
    'CME_2017-05-27/WI_H0_MFI_CME_2017-05-27.txt', #58 min OK
    'CME_2017-07-08/WI_H0_MFI_CME_2017-07-08.txt' #67 min OK
]
final_time_lag=[56,
                38,30,50,63,53,62,26,40,68,48,52,
                43,65,61,157,69,52,44,56,33,47,69,70,52,44,
                51,46,32,79,54,43,38,32,45,50,46,45,49,
                37,36,58,39,56,61,39,64,43,34,53,45,57,37,
                44,28,48,40,29,46,50,30,27,44,49,
                62,41,62,60,53,   
                30,58,67]

def date_to_mjd(year, month, day):
    if month == 1 or month == 2:
        yearp = year - 1
        monthp = month + 12
    else:
        yearp = year
        monthp = month
    if ((year < 1582) or
        (year == 1582 and month < 10) or
            (year == 1582 and month == 10 and day < 15)):
        B = 0
    else:
        A = math.trunc(yearp / 100.)
        B = 2 - A + math.trunc(A / 4.)
    if yearp < 0:
        C = math.trunc((365.25 * yearp) - 0.75)
    else:
        C = math.trunc(365.25 * yearp)
    D = math.trunc(30.6001 * (monthp + 1))
    jd = B + C + D + day + 1720994.5
    return jd - 2400000.5

def hmsm_to_days(hour=0, min=0, sec=0, micro=0):
    days = sec + (micro / 1.e6)
    days = min + (days / 60.)
    days = hour + (days / 60.)
    return days / 24.

def datetime_to_float(d):
    return d.timestamp()

def float_to_datetime(fl):
    return datetime.fromtimestamp(fl)


for ind_shock,each_file in enumerate( IP_date_file):
    sep = '/'
    IP_date = (each_file.split(sep, 1)[0])
    filein = '/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/' + \
        str(each_file)
    #ips_min_sec_to_date = hmsm_to_days(hour=IP_date.hour, min=IP_date.minute)
    #IPs_date = date_to_mjd(IP_date.year, IP_date.month, IP_date.day+ips_min_sec_to_date)


    year_dst = []
    sec_dst = []
    Dst = []
    SYM_H = []

    file = open('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/' +
                str(IP_date)+'/SYM_H_'+str(IP_date)+'.txt', 'r')
    lines = (file.readlines())
    for line in lines:
        if line[:4].isdigit():
            p = line.split()
            year_dst.append(int(p[0]))
            sec_dst.append(float(p[1]))
            SYM_H.append(float(p[2]))
    file.close()
    SYM_H1 = np.array(SYM_H)

    SYM_H2 = np.array(SYM_H)
    for ind, item in enumerate(SYM_H1):
        if item == 99999:
            if ind - 20 > 0 and ind + 20 < len(SYM_H1):
                SYM_H2[ind]=median(SYM_H1[ind-20:ind+20])
            else:
                SYM_H2[ind]=0
                
    SYMH_interp = interp.interp1d(np.arange(SYM_H2.size),SYM_H2)
    SYM_H = SYMH_interp(np.linspace(0, SYM_H2.size-1, SYM_H1.size))
    SYM_H_ = np.array(SYM_H)

    SYM_H_AFTER=SYM_H_[int(len(SYM_H_)/2):]
    min_symh.append(min(SYM_H_AFTER))

    date = []
    for i in range(len(sec_dst)):
        date.append(
            datetime(int(year_dst[i]), 1, 1) + timedelta(seconds=sec_dst[i]))

    df_S = pd.DataFrame({'date': date, 'symh': SYM_H_}, columns=['date', 'symh'])
    dfS=df_S.set_index('date').resample('60s').mean()
    dfS=dfS.reset_index()
    dfS['symh'] = dfS['symh'].interpolate()

    SYM_H_der = np.diff(SYM_H, n=1)

    # mvalue of SC
    res = np.roll(SYM_H, -1)-SYM_H
    res = res[int(len(SYM_H)/2)-100:int(len(SYM_H)/2)+100]
    ind = int(len(SYM_H)/2)-100+(np.argmax(res))
    symh_at_ip.append(SYM_H[ind])


    #plt.plot(date,SYM_H,color='yellowgreen',linewidth=0.5)
    #plt.axvline(x=date[int(len(SYM_H)/2)-100+ind], color='k', linestyle='--')    
    #plt.show()
    ################################################################################################################################################
    date_kindex = []
    kindex = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []

    file = open(
        '/Users/Taninka/Documents/skola_PhD/CASE_STUDY/data_codes/data/BDV_K-index.txt', 'r')
    lines = (file.readlines())
    for line in lines:
        p = line.split()
        date_kindex.append(p[0])
        one.append(int(p[1]))
        two.append(int(p[2]))
        three.append(int(p[3]))
        four.append(int(p[4]))
        five.append(int(p[5]))
        six.append(int(p[6]))
        seven.append(int(p[7]))
        eight.append(int(p[8]))
        kindex.append(float(p[9]))
    file.close()

    kindex_dt = []
    for i in range(len(date_kindex)):
        kindex_dt.append(datetime.strptime(date_kindex[i], '%d.%m.%Y'))

    # prienik datumov
    intersection_dt = sorted(set(kindex_dt).intersection(date))

    # zistujem prvy a posledny index
    first_index = kindex_dt.index(intersection_dt[0])
    last_index = kindex_dt.index(intersection_dt[-1])

    period = 16  # 2dni kedze mame 3hod intervaly
    kindex_dt = pd.date_range(
        start=kindex_dt[first_index-1], end=kindex_dt[last_index]+timedelta(hours=12), freq='3h')
    kindex_dt = kindex_dt[5:]

    # beriem 3 hodinove merania a ukladma to jedneho velkeeho pola
    k_index = []

    for i in range(len(kindex)):
        list_ = (one[i], two[i], three[i], four[i],
                 five[i], six[i], seven[i], eight[i])
        k_index.append(list_)

    k_index_reshape = np.reshape(k_index, (1, len(k_index)*8))

    kindex_all = []
    for i in range(len(k_index)*8):
        kindex_all.append(k_index_reshape[0][i])

    kindex_all = kindex_all[(first_index - 1) * 8:(last_index) * 8]
    ################################################################################################################################################
    year_v = []
    sec_v = []
    vx = []
    vy = []
    vz = []
    P_d=[]
    file = open('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/' +str(IP_date)+'/WI_H1_SWE_'+str(IP_date)+'.txt', 'r')
    lines = (file.readlines())
    for index, line in enumerate(lines):
        if line[:4].isdigit():
            p = line.split(',')
            year_v.append((p[0]))
            P_d.append(float(p[1]))
            vx.append(float(p[2]))  
            vy.append(float(p[3]))
            vz.append(float(p[4]))
    file.close()
    year_v = np.array(year_v)
    p_d=np.array(P_d)
    vx = np.array(vx)
    vy = np.array(vy)
    vz = np.array(vz)

    dtpd=[] 
    for i in range(len(year_v)):
        dtpd.append(datetime.strptime(year_v[i], '%Y-%m-%d %H:%M:%S.%f'))

    p_d=np.array(p_d)
    df = pd.DataFrame({'dtpd': dtpd, 'pd': p_d, 'vx': vx, 'vy': vy, 'vz': vz}, columns=['dtpd', 'pd', 'vx', 'vy', 'vz'])
    df2=df.set_index('dtpd').resample('60s').mean()
    df2=df2.reset_index()
    df2 = pd.concat([dfS,df2], join="outer", axis=1)
    df2.loc[np.where(df2['pd']>=10000)[0],'pd'] = np.nan
    df2.loc[np.where(df2['vx'] >=9999)[0],'vx'] = np.nan
    df2.loc[np.where(df2['vy'] >=9999)[0],'vy'] = np.nan
    df2.loc[np.where(df2['vz'] >=9999)[0],'vz'] = np.nan
    df2=df2.reset_index()
    df2['pd'] = df2['pd'].interpolate()
    df2['vx'] = df2['vx'].interpolate()
    df2['vy'] = df2['vy'].interpolate()
    df2['vz'] = df2['vz'].interpolate()
    df2['symh'] = df2['symh'].interpolate()

    if df2['date'].isnull().values.any():
        dtpd_list=df2['dtpd'].tolist()
    else:
        dtpd_list=df2['date'].tolist()

    pd_list=df2['pd'].tolist()
    pd_list=np.array(pd_list)

    vx_list=df2['vx'].tolist()
    vx_list=np.array(vx_list)

    vy_list=df2['vy'].tolist()
    vy_list=np.array(vy_list)

    vz_list=df2['vz'].tolist()
    vz_list=np.array(vz_list)

    SYM_H2=df2['symh'].tolist()
    SYM_H2=np.array(SYM_H2)

    ######################################################################################################################################################################
    # MAGNETIC FIELD
    year = []
    sec_B = []
    B_mag = []
    Bx = []
    By = []
    Bz2 = []

    #fhandle = open(filein, 'r')
    fhandle=open('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/' +
                str(IP_date)+'/WI_H0_MFI_'+str(IP_date)+'.txt', 'r')
    lines = (fhandle.readlines())
    for line in lines:
        if line[:4].isdigit():
            p = line.split()
            year.append(int(p[0]))
            sec_B.append(float(p[1]))
            B_mag.append(float(p[2]))
            Bx.append(float(p[3]))
            By.append(float(p[4]))
            Bz2.append(float(p[5]))
    fhandle.close()

    year = np.array(year)
    sec_B = np.array(sec_B)
    B_mag = np.array(B_mag)
    Bx = np.array(Bx)
    By = np.array(By)
    Bz2 = np.array(Bz2)

    utc_time_all = []
    for i in range(len(sec_B)):
        utc_time_all.append(
            datetime(int(year[i]), 1, 1) + timedelta(seconds=sec_B[i]))

    B_mag = B_mag[(B_mag > -10e30)]
    Bx = Bx[(Bx > -10e30)]
    By = By[(By > -10e30)]
    Bz_ = Bz2[(Bz2 > -10e30)]

    Bz_int = interp.interp1d(np.arange(Bz_.size), Bz_)
    Bz = Bz_int(np.linspace(0, Bz_.size-1, Bz2.size))

    utc_time = []
    for i in range(len(sec_B)):
        utc_time.append(datetime(int(year[i]), 1, 1) + timedelta(seconds=sec_B[i]))

    dfb = pd.DataFrame({'dtB': utc_time, 'Bz': Bz}, columns=['dtB', 'Bz'])
    dfb2=dfb.set_index('dtB').resample('60s').mean()
    dfb2=dfb2.reset_index()
    if df2['date'].isnull().values.any():
        dfb2 = pd.concat([df2['dtpd'],dfb2], join="outer", axis=1)
        if df2['dtpd'].isnull().values.any():
            dtB_list=dfb2['dtB'].tolist()  
        else:
            dtB_list=dfb2['dtpd'].tolist() 

    else:
        dfb2 = pd.concat([dfS['date'],dfb2], join="outer", axis=1)
        if df2['date'].isnull().values.any():
            dtB_list=dfb2['dtB'].tolist()  
        else:
            dtB_list=dfb2['date'].tolist()         
    #dfb2 = pd.concat([dfS['date'],dfb2], join="outer", axis=1)
    dfb2=dfb2.reset_index()
    dfb2['Bz'] = dfb2['Bz'].interpolate()

    Bz_list=dfb2['Bz'].tolist()
    Bz_list=np.array(Bz_list)


    ind_eq_B=[]
    for ind,item in enumerate(dtB_list):
        if item==dtpd_list[-1]:
            ind_eq_B.append(ind)
    Bz_list2=Bz_list[:ind_eq_B[0]+1]
    utc_time2=utc_time[:ind_eq_B[0]+1]

    ind_eq=[]
    if len(date) > len(dtpd_list):
        for ind,item in enumerate(date):
            if item==dtpd_list[-1]:
                ind_eq.append(ind)
        SYM_H2=SYM_H_[:ind_eq[0]+1]
        date2=date[:ind_eq[0]+1]
    else:
        for ind,item in enumerate(dtpd_list):
            if item==date[-1]:
                ind_eq.append(ind)    
        pd_list=pd_list[:ind_eq[0]+1]
        date2=dtpd_list[:ind_eq[0]+1]
    ##################################################################################################################
    #corrected symh
    dynamic_pressure=pd_list
    new_dt_pd=[]
    for ind, item in enumerate(date2):
        new_dt_pd.append(item + timedelta(minutes=final_time_lag[ind_shock]))

    dynamic_pressure=dynamic_pressure.tolist()
    delta_symh=[]
    for ind,item in enumerate(dynamic_pressure):
        delta_symh.append(20 * math.sqrt(item/1.6) + 20)

    for i in range(0,final_time_lag[ind_shock]):
        delta_symh.insert(0,None) 
    delta_symh=delta_symh[:len(delta_symh)-final_time_lag[ind_shock]]    

    corrected_symh=[]
    for ind,item in enumerate(delta_symh):
        if item is not None and ind <len(SYM_H2):
            corrected_symh.append(SYM_H2[ind] - delta_symh[ind]) 
        elif item is None:
            corrected_symh.append(None)
        else: 
            pass
    df_corr = pd.DataFrame({'symh_corr': corrected_symh}, columns=[ 'symh_corr'])
    df_corr=df_corr.reset_index()
    df_corr['symh_corr'] = df_corr['symh_corr'].interpolate(method='nearest').ffill().bfill()
    symh_corr_list=df_corr['symh_corr'].tolist()

    ##################################################################################################################    
    Bz_vx = (Bz_list2*vx_list)
    for specific_time in int_values:
        Bz_vx_integral = [None]*len(Bz_vx)
        for i in range(len(Bz_vx)):
            if i-specific_time*60 > 0 and i < len(Bz_vx):
                Bz_vx_integral[i] = ((Bz_vx[i-specific_time*60:i]).sum())
            else:
                Bz_vx_integral[i] = None

        # INTEGRAL OF Bz.vx
        Bz_integral = [None]*len(Bz_list2)

        # integral BZ only, cele to dam to for cyklu a pre kazde i si vygenerujem grafy
        for i in range(len(Bz_list2)):
            if i-specific_time*60 > 0 and i < len(Bz_list2):
                Bz_integral[i] = ((Bz_list2[i-specific_time*60:i]).sum())
            else:
                Bz_integral[i] = None

        diff_pd=np.diff(pd_list)    
        size=50
        where_pd_max=np.array(diff_pd[int(len(diff_pd)/2)-size:int(len(diff_pd)/2)+size])
        pd_jump_ind=(np.where(diff_pd==where_pd_max.max()))[0][0]

        size2=100
        new_symh=[]
        for ind,item in enumerate(SYM_H2):
            if ind<=int(len(SYM_H2)/2)-size2:
                new_symh.append(0)
            elif ind>=int(len(SYM_H2)/2)+size2:
                new_symh.append(0)
            else:
                new_symh.append(item)

        diff_symh=np.diff(new_symh)  
        ind_diff_symh=np.where((diff_symh >0) & (diff_symh==diff_symh.max()))[0][0]

        while ind_diff_symh < pd_jump_ind:
            #diff_symh=np.delete(diff_symh,diff_symh.max())
            diff_symh[ind_diff_symh]=0
            ind_diff_symh=np.where( diff_symh==diff_symh.max())[0][0]
            if ind_diff_symh-120 > pd_jump_ind:
                continue
            else:
                pass
        IP_index = (np.where(diff_symh==diff_symh.max()))[0][0] #symh_jump_ind

        hms_day = []
        DAYS = []
        MJD = []
        for i in date2:
            hms_day.append(hmsm_to_days(hour=i.hour, min=i.minute))
            DAYS.append(i.date())

        for i in range(len(DAYS)):
            MJD.append(date_to_mjd(
                DAYS[i].year, DAYS[i].month, DAYS[i].day + hms_day[i]))

        MJD = np.array(MJD)
        # xova osa korelacnych grafov
        dt_corc = ((MJD-MJD[IP_index])*24*60)

        cor_wind=420
        # integral
        Bz_vx_integral_=np.array(Bz_vx_integral)
        Bz_vx_integral_all=np.array(Bz_vx_integral)
        Bz_vx_integral_ = Bz_vx_integral_[IP_index - cor_wind: IP_index + cor_wind]
        Bz_vx_integral_ = Bz_vx_integral_.astype('float64') #is naan hadzal error kvoli datovemu type
        nan_int_indx = np.argwhere(np.isnan(Bz_vx_integral_))
        corrected_symh=np.array(corrected_symh)

        korelace = []
        for i in range(len(SYM_H2)):
            if i - cor_wind > 0 and i+cor_wind < len(SYM_H2):
                sym_h = SYM_H2[i-cor_wind: i + cor_wind]
                if nan_int_indx.any():
                    korelace.append(pearsonr(sym_h[nan_int_indx[-1][0]+1:], Bz_vx_integral_[nan_int_indx[-1][0]+1:])[0])
                else:
                    korelace.append(pearsonr(sym_h[1:], Bz_vx_integral_[1:])[0])
            else:
                #sym_h = None
                korelace.append(None)

        korelace_corrected=[]
        for i in range(len(corrected_symh)):
            if i - cor_wind > 0 and i+cor_wind < len(corrected_symh):
                sym_h_corrected=symh_corr_list[i-cor_wind: i + cor_wind]
                if nan_int_indx.any(): #and corrected_symh[i-cor_wind]== None or corrected_symh[i+cor_wind]== None:
                    #korelace_corrected.append(None)
                    korelace_corrected.append(pearsonr(sym_h_corrected[nan_int_indx[-1][0]+1:], Bz_vx_integral_[nan_int_indx[-1][0]+1:])[0])
                else:
                    korelace_corrected.append(pearsonr(sym_h_corrected[1:], Bz_vx_integral_[1:])[0])
            else:
                korelace_corrected.append(None)
        #plt.figure()
        #fig, ax = plt.subplots(3,figsize=(10,8))
        #ax[0].plot(SYM_H_[IP_index - 6*60 : IP_index + 6*60])
        #ax[0].set_title(' Date: ' + str(IP_date)+' | ' + ' Integrating time: '+str(specific_time)+' hours')
        #ax[0].legend(['SYM-H'], loc='best')
        # ax[1].plot(Bz_vx_integral_)  
        # ax[1].legend(['INTEGRAL'], loc='best')             
        # ax[2].plot(dt_corc, korelace)
        # ax[2].legend(['Pearson Correlation int(Bz*vx)'], loc='best')
        # ax[2].set_xlim(-1000, 1000)
        # ax[2].set_ylim(-1, 1)
        # plt.show()
        # plt.close()

        corr = []
        for i in korelace:
            if i is not None:
                corr.append(i)
            else:
                pass
        min_corr = min(corr)
        indices_for_minimum_lag=(korelace.index(min_corr))

        corr_corrected=[]
        for ind,item in enumerate(korelace_corrected):
            if item is not None:
                corr_corrected.append(item)
            else:
                pass
        min_corr_corrected = min(corr_corrected)
        indices_for_minimum_lag_corrected=(korelace_corrected.index(min_corr_corrected))

        if specific_time==7:
            corr_7.append(min_corr)
            lag_7.append(dt_corc[indices_for_minimum_lag])

            corr_7_corr.append(min_corr_corrected)
            lag_7_corr.append(dt_corc[indices_for_minimum_lag_corrected])      

        if specific_time==8:
            corr_8.append(min_corr)
            lag_8.append(dt_corc[indices_for_minimum_lag])

            corr_8_corr.append(min_corr_corrected)
            lag_8_corr.append(dt_corc[indices_for_minimum_lag_corrected])

        if specific_time==9:
            corr_9.append(min_corr)    
            lag_9.append(dt_corc[indices_for_minimum_lag])  

            corr_9_corr.append(min_corr_corrected)    
            lag_9_corr.append(dt_corc[indices_for_minimum_lag_corrected])             

        if specific_time==10:
            corr_10.append(min_corr)
            lag_10.append(dt_corc[indices_for_minimum_lag])

            corr_10_corr.append(min_corr_corrected)
            lag_10_corr.append(dt_corc[indices_for_minimum_lag_corrected])

        if specific_time==11:
            corr_11.append(min_corr)
            lag_11.append(dt_corc[indices_for_minimum_lag])

            corr_11_corr.append(min_corr_corrected)
            lag_11_corr.append(dt_corc[indices_for_minimum_lag_corrected])

        if specific_time==12:
            corr_12.append(min_corr)
            lag_12.append(dt_corc[indices_for_minimum_lag])

            corr_12_corr.append(min_corr_corrected)
            lag_12_corr.append(dt_corc[indices_for_minimum_lag_corrected])

        if specific_time==13:
            corr_13.append(min_corr)
            lag_13.append(dt_corc[indices_for_minimum_lag])

            corr_13_corr.append(min_corr_corrected)
            lag_13_corr.append(dt_corc[indices_for_minimum_lag_corrected])

        if specific_time==14:
            corr_14.append(min_corr)
            lag_14.append(dt_corc[indices_for_minimum_lag])

            corr_14_corr.append(min_corr_corrected)
            lag_14_corr.append(dt_corc[indices_for_minimum_lag_corrected])

        if specific_time==15:
            corr_15.append(min_corr)
            lag_15.append(dt_corc[indices_for_minimum_lag])
            INT_AFTER=Bz_vx_integral_all[int(len(Bz_vx_integral_all)/2):]
            max_int.append(max(INT_AFTER))

            corr_15_corr.append(min_corr_corrected)
            lag_15_corr.append(dt_corc[indices_for_minimum_lag_corrected])

        if specific_time==16:
            corr_16.append(min_corr)
            lag_16.append(dt_corc[indices_for_minimum_lag])

            corr_16_corr.append(min_corr_corrected)
            lag_16_corr.append(dt_corc[indices_for_minimum_lag_corrected])

        if specific_time==17:
           corr_17.append(min_corr)
           lag_17.append(dt_corc[indices_for_minimum_lag])

           corr_17_corr.append(min_corr_corrected)
           lag_17_corr.append(dt_corc[indices_for_minimum_lag_corrected])

        if specific_time==18:
           corr_18.append(min_corr)
           lag_18.append(dt_corc[indices_for_minimum_lag])

           corr_18_corr.append(min_corr_corrected)
           lag_18_corr.append(dt_corc[indices_for_minimum_lag_corrected])

        if specific_time==19:
           corr_19.append(min_corr)
           lag_19.append(dt_corc[indices_for_minimum_lag])

           corr_19_corr.append(min_corr_corrected)
           lag_19_corr.append(dt_corc[indices_for_minimum_lag_corrected])

minimum_korelace=list(zip(corr_7,corr_8,corr_9,corr_10,corr_11,corr_12,corr_13,corr_14,corr_15,corr_16,corr_17,corr_18,corr_19))
minimum_lag=list(zip(lag_7,lag_8,lag_9,lag_10,lag_11,lag_12,lag_13,lag_14,lag_15,lag_16,lag_17,lag_18,lag_19))

minimum_korelace_corr=list(zip(corr_7_corr,corr_8_corr,corr_9_corr,corr_10_corr,corr_11_corr,corr_12_corr,corr_13_corr,corr_14_corr,corr_15_corr,corr_16_corr,corr_17_corr,corr_18_corr,corr_19_corr))
minimum_lag_corr=list(zip(lag_7_corr,lag_8_corr,lag_9_corr,lag_10_corr,lag_11_corr,lag_12_corr,lag_13_corr,lag_14_corr,lag_15_corr,lag_16_corr,lag_17_corr,lag_18_corr,lag_19_corr))

corr_list=[corr_7,corr_8,corr_9,corr_10,corr_11,corr_12,corr_13,corr_14,corr_15,corr_16,corr_17,corr_18,corr_19]
lag_list=[lag_7,lag_8,lag_9,lag_10,lag_11,lag_12,lag_13,lag_14,lag_15,lag_16,lag_17,lag_18,lag_19]

corr_list_corr=[corr_7_corr,corr_8_corr,corr_9_corr,corr_10_corr,corr_11_corr,corr_12_corr,corr_13_corr,corr_14_corr,corr_15_corr,corr_16_corr,corr_17_corr,corr_18_corr,corr_19_corr]
lag_list_corr=[lag_7_corr,lag_8_corr,lag_9_corr,lag_10_corr,lag_11_corr,lag_12_corr,lag_13_corr,lag_14_corr,lag_15_corr,lag_16_corr,lag_17_corr,lag_18_corr,lag_19_corr]

minimum_korelace2=[]
for i in range(len(int_values)):
    minimum_korelace2.append(corr_list[i])

#CORR
minimum_korelace2_corr=[]
for i in range(len(int_values)):
    minimum_korelace2_corr.append(corr_list_corr[i])

median=[]
for i in minimum_korelace2:
    median.append(statistics.median(i))

#CORR
median_corr=[]
for i in minimum_korelace2_corr:
    median_corr.append(statistics.median(i))    

max_min=min(min(minimum_korelace2))
#CORR
max_min_corr=min(min(minimum_korelace2_corr))

condition = np.array(minimum_korelace) == max_min
np.where(condition)[0] 
minimum_korelace_arr=np.array(minimum_korelace)
minimum_lag_arr=np.array(minimum_lag)

#CORR
condition_corr = np.array(minimum_korelace_corr) == max_min_corr
np.where(condition_corr)[0] 
minimum_korelace_arr_corr=np.array(minimum_korelace_corr)
minimum_lag_arr_corr=np.array(minimum_lag_corr)


for i in range(len(minimum_lag)):
    minimum_lag[i]=np.array(minimum_lag[i])
    pass
for j in range(len(minimum_korelace)):
    minimum_korelace[j]=np.array(minimum_korelace[j])
    pass

#CORR
for i in range(len(minimum_lag_corr)):
    minimum_lag_corr[i]=np.array(minimum_lag_corr[i])
    pass
for j in range(len(minimum_korelace_corr)):
    minimum_korelace_corr[j]=np.array(minimum_korelace_corr[j])
    pass

minimum_korelace_15=list(zip(corr_15))
minimum_lag_15=list(zip(lag_15))
median_15=statistics.median(corr_15)
max_min_15=min(min(minimum_korelace_15))
condition_15 = np.array(minimum_korelace_15) == max_min_15
np.where(condition_15)[0] #[12,6] poloha minima v minimum_korelace
minimum_korelace_arr_15=np.array(minimum_korelace_15)
minimum_lag_arr_15=np.array(minimum_lag_15)

#CORR
minimum_korelace_15_corr=list(zip(corr_15_corr))
minimum_lag_15_corr=list(zip(lag_15_corr))
median_15_corr=statistics.median(corr_15_corr)
max_min_15_corr=min(min(minimum_korelace_15_corr))
condition_15_corr = np.array(minimum_korelace_15_corr) == max_min_15_corr
np.where(condition_15_corr)[0] #[12,6] poloha minima v minimum_korelace
minimum_korelace_arr_15_corr=np.array(minimum_korelace_15_corr)
minimum_lag_arr_15_corr=np.array(minimum_lag_15_corr)

for i in range(len(minimum_lag_15)):
    minimum_lag_15[i]=np.array(minimum_lag_15[i])
    pass
for j in range(len(minimum_korelace_15)):
    minimum_korelace_15[j]=np.array(minimum_korelace_15[j])
    pass

#CORR
for i in range(len(minimum_lag_15_corr)):
    minimum_lag_15_corr[i]=np.array(minimum_lag_15_corr[i])
    pass
for j in range(len(minimum_korelace_15_corr)):
    minimum_korelace_15_corr[j]=np.array(minimum_korelace_15_corr[j])
    pass

orig_vs_corr=0
if orig_vs_corr==1:
    #labels=['0','1','2','3','4','5','6','7','8','9','10','11','12']
    labels=[7,8,9,10,11,12,13,14,15,16,17,18,19]
    col=ListedColormap(['lightgrey','black','darkgrey','saddlebrown','darkred','darkslategrey', 'darkgreen','darkblue','darkmagenta','indigo','darkorange','darkviolet','crimson'])
    col_pal=sn.color_palette("dark:salmon_r", as_cmap=True)
    for i in range(len(minimum_lag)):
        scatter=plt.scatter(minimum_lag[i], minimum_korelace[i], c=labels, cmap=col_pal)
        #scatter=sn.scatterplot(x=minimum_lag[i], y=minimum_korelace[i],hue=labels,size=labels, palette='hot')
        plt.legend(*scatter.legend_elements(),loc='best')
    plt.rcParams["figure.figsize"] = [10,10]
    plt.xlabel('Time lags (minutes)',fontsize=14)
    plt.xticks(fontsize=14)
    plt.ylabel('Minimum of correlation',fontsize=14) 
    plt.yticks(fontsize=14)
    plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/special_graphs/time_lags_vs_min_corr_48h.pdf')
    #plt.show()
    plt.close()


    scatter=plt.scatter(minimum_lag_15, minimum_korelace_15,label='Integration time 15 hours',c='maroon')#, markersize=4)
    plt.legend(loc='best')
    plt.rcParams["figure.figsize"] = [10,10]
    plt.xlabel('Time lags (minutes)',fontsize=20)
    plt.xticks(fontsize=20)
    plt.ylabel('Minimum of correlation',fontsize=20) 
    plt.yticks(fontsize=20)
    plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/special_graphs/time_lags_vs_min_corr_48h_int_time_15.pdf')
    #plt.show()
    plt.close()

    canvas = plt.figure()
    rect = canvas.patch
    rect.set_facecolor('white')
    sp1 = canvas.add_subplot(1,1,1, facecolor='w')
    for j,i in enumerate(minimum_korelace):
        plt.plot(int_values, minimum_korelace[j], marker='o', markerfacecolor='blue', markersize=4, color='skyblue', linewidth=1)
        plt.plot(int_values,median,color='tomato',linewidth=1)
        plt.rcParams["figure.figsize"] = [8,8]
        plt.xlabel('Interval of integration (hours)',fontsize=14)
        plt.xticks(fontsize=14)
        plt.ylabel('Minimum of correlation',fontsize=14) 
        plt.yticks(fontsize=14)       
    plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/special_graphs/int_value_vs_min_corr_48h.pdf',dpi=100)
    #plt.show()
    plt.close()


    plt.figure()
    fig, ax = plt.subplots(3, figsize=(12,14))

    ax[0].plot(min_symh,corr_15, 'o' ,marker='o', markerfacecolor='blue')
    ax[0].set_title('15 hour integration interval')
    ax[0].set_xlabel('Minimum of SYM-H after IP shock [nT]',fontsize=12)
    ax[0].tick_params(axis='both',labelsize=12)
    ax[0].set_ylabel('Minimum of correlation',fontsize=12) 

    ax[1].plot(max_int,corr_15, 'o' ,marker='o', markerfacecolor='green')
    ax[1].set_xlabel('Maximum of integral after IP shock',fontsize=12)
    ax[1].tick_params(axis='both',labelsize=12)
    ax[1].set_ylabel('Minimum of correlation',fontsize=12) 
    ax[1].ticklabel_format(useOffset=False,style='sci')
    ax[1].xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))

    ax[2].plot(symh_at_ip ,corr_15, 'o' ,marker='o', markerfacecolor='red')
    ax[2].set_xlabel('SYM-H at the moment of shock [nT]',fontsize=12)
    ax[2].tick_params(axis='both',labelsize=12)
    ax[2].set_ylabel('Minimum of correlation',fontsize=12)

    plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/special_graphs/min_symh_vs_min_corr_48h.pdf',dpi=100)
    #plt.show()
    plt.close
    print(1)
else:
    #labels=['0','1','2','3','4','5','6','7','8','9','10','11','12']
    labels=[7,8,9,10,11,12,13,14,15,16,17,18,19]
    col=ListedColormap(['lightgrey','black','darkgrey','saddlebrown','darkred','darkslategrey', 'darkgreen','darkblue','darkmagenta','indigo','darkorange','darkviolet','crimson'])
    col_pal=sn.color_palette("dark:salmon_r", as_cmap=True)
    for i in range(len(minimum_lag_corr)):
        scatter=plt.scatter(minimum_lag_corr[i], minimum_korelace_corr[i], c=labels, cmap=col_pal)
        #scatter=sn.scatterplot(x=minimum_lag[i], y=minimum_korelace[i],hue=labels,size=labels, palette='hot')
        plt.legend(*scatter.legend_elements(),loc='best')
    plt.rcParams["figure.figsize"] = [10,10]
    plt.xlabel('Time lags (minutes)',fontsize=14)
    plt.xticks(fontsize=14)
    plt.ylabel('Minimum of corrected correlation',fontsize=14) 
    plt.yticks(fontsize=14)
    plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/special_graphs/time_lags_vs_min_corr_48h_corrected.pdf')
    #plt.show()
    plt.close()


    scatter=plt.scatter(minimum_lag_15_corr, minimum_korelace_15_corr,label='Integration time 15 hours',c='maroon')#, markersize=4)
    plt.legend(loc='best')
    plt.rcParams["figure.figsize"] = [10,10]
    plt.xlabel('Time lags (minutes)',fontsize=20)
    plt.xticks(fontsize=20)
    plt.ylabel('Minimum of corrected correlation',fontsize=20) 
    plt.yticks(fontsize=20)
    plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/special_graphs/time_lags_vs_min_corr_48h_int_time_15_corrected.pdf')
    #plt.show()
    plt.close()

    canvas = plt.figure()
    rect = canvas.patch
    rect.set_facecolor('white')
    sp1 = canvas.add_subplot(1,1,1, facecolor='w')
    for j,i in enumerate(minimum_korelace):
        plt.plot(int_values, minimum_korelace_corr[j], marker='o', markerfacecolor='blue', markersize=4, color='skyblue', linewidth=1)
        plt.plot(int_values,median_corr,color='tomato',linewidth=1)
        plt.rcParams["figure.figsize"] = [8,8]
        plt.xlabel('Interval of integration (hours)',fontsize=14)
        plt.xticks(fontsize=14)
        plt.ylabel('Minimum of corrected correlation',fontsize=14) 
        plt.yticks(fontsize=14)       
    plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/special_graphs/int_value_vs_min_corr_48h_corrected.pdf',dpi=100)
    #plt.show()
    plt.close()


    plt.figure()
    fig, ax = plt.subplots(3, figsize=(12,14))

    ax[0].plot(min_symh,corr_15_corr, 'o' ,marker='o', markerfacecolor='blue')
    ax[0].set_title('15 hour integration interval')
    ax[0].set_xlabel('Minimum of SYM-H after IP shock [nT]',fontsize=12)
    ax[0].tick_params(axis='both',labelsize=12)
    ax[0].set_ylabel('Minimum of corrected correlation',fontsize=12) 

    ax[1].plot(max_int,corr_15_corr, 'o' ,marker='o', markerfacecolor='green')
    ax[1].set_xlabel('Maximum of integral after IP shock',fontsize=12)
    ax[1].tick_params(axis='both',labelsize=12)
    ax[1].set_ylabel('Minimum of corrected correlation',fontsize=12) 
    ax[1].ticklabel_format(useOffset=False,style='sci')
    ax[1].xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))

    ax[2].plot(symh_at_ip ,corr_15_corr, 'o' ,marker='o', markerfacecolor='red')
    ax[2].set_xlabel('SYM-H at the moment of shock [nT]',fontsize=12)
    ax[2].tick_params(axis='both',labelsize=12)
    ax[2].set_ylabel('Minimum of corrected correlation',fontsize=12)

    plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/special_graphs/min_symh_vs_min_corr_48h_corrected.pdf',dpi=100)
    #plt.show()
    plt.close
    print(1)

