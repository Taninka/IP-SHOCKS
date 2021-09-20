from datetime import datetime, timedelta, time
import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace, sum
import scipy
from scipy import integrate
from scipy import signal
import matplotlib.dates as mdates
import scipy.interpolate as interp
import matplotlib.ticker as plticker
import math
import pandas as pd
from itertools import combinations
import operator
from statistics import mode
from statistics import mean
from statistics import median
from scipy.stats import pearsonr, spearmanr, kendalltau
from stingray import Lightcurve
from stingray.crosscorrelation import CrossCorrelation

def square(list):
    return np.array([i ** 2 for i in list])

def date_to_mjd(year, month, day):
    """
    Convert a date to Julian Day.

    Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet',
        4th ed., Duffet-Smith and Zwart, 2011.

    Parameters
    ----------
    year : int
        Year as integer. Years preceding 1 A.D. should be 0 or negative.
        The year before 1 A.D. is 0, 10 B.C. is year -9.

    month : int
        Month as integer, Jan = 1, Feb. = 2, etc.

    day : float
        Day, may contain fractional part.

    Returns
    -------
    jd : float
        Julian Day

    Examples
    --------
    Convert 6 a.m., February 17, 1985 to Julian Day

    >>> date_to_jd(1985,2,17.25)
    2446113.75

    """
    if month == 1 or month == 2:
        yearp = year - 1
        monthp = month + 12
    else:
        yearp = year
        monthp = month

    # this checks where we are in relation to October 15, 1582, the beginning
    # of the Gregorian calendar.
    if ((year < 1582) or
        (year == 1582 and month < 10) or
            (year == 1582 and month == 10 and day < 15)):
        # before start of Gregorian calendar
        B = 0
    else:
        # after start of Gregorian calendar
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
    """
    Convert hours, minutes, seconds, and microseconds to fractional days.

    Parameters
    ----------
    hour : int, optional
        Hour number. Defaults to 0.

    min : int, optional
        Minute number. Defaults to 0.

    sec : int, optional
        Second number. Defaults to 0.

    micro : int, optional
        Microsecond number. Defaults to 0.

    Returns
    -------
    days : float
        Fractional days.

    Examples
    --------
    >>> hmsm_to_days(hour=6)
    0.25

    """
    days = sec + (micro / 1.e6)

    days = min + (days / 60.)

    days = hour + (days / 60.)

    return days / 24.

def datetime_to_float(d):
    return d.timestamp()

def float_to_datetime(fl):
    return datetime.fromtimestamp(fl)

ips_min_sec_to_date = hmsm_to_days(hour=18, min=22)

IPs_date = date_to_mjd(2014, 12, 23+ips_min_sec_to_date)
# print(IPs_date)

####################
# ###################################################################################################################################################################
# GEOMAGNETIC INDEX SYM-H
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
        # Dst.append(float(p[2]))
        SYM_H.append(float(p[2]))
        #year_dst.append(p[0])
        #sec_dst.append(p[1])
        #SYM_H.append(float(p[6]))
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

date2 = []
for i in range(len(sec_dst)):
    date2.append(
        datetime(int(year_dst[i]), 1, 1) + timedelta(seconds=sec_dst[i]))

df_S = pd.DataFrame({'date': date2, 'symh': SYM_H_}, columns=['date', 'symh'])
dfS=df_S.set_index('date').resample('3s').mean()
dfS=dfS.reset_index()
dfS['symh'] = dfS['symh'].interpolate()
date=dfS['date'].tolist()
SYM_H_=dfS['symh'].tolist()

SYM_H_der = np.diff(SYM_H, n=1)

# mvalue of SC
res = np.roll(SYM_H, -1)-SYM_H
res = res[int(len(SYM_H)/2)-100:int(len(SYM_H)/2)+100]
ind = int(len(SYM_H)/2)-100+(np.argmax(res))
symh_at_ip=[]

symh_at_ip.append(SYM_H[ind])

flog.write(str(IP_date)+' & '+str(max(res))+'\\\\\n')


#####################################################################################################################################################################
# K index

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

#####################################################################################################################################################################
# SOLAR WIND SPEED
year_v = []
sec_v = []
vx = []
vy = []
vz = []
P_d=[]
file = open('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/' +str(IP_date)+'/WI_PM_3DP_'+str(IP_date)+'.txt', 'r')
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
dtpd_=[]
for i in range(len(year_v)):
    dtpd.append(datetime.strptime(year_v[i], '%Y-%m-%d %H:%M:%S.%f'))
for i in dtpd:
    dtpd_.append(i.replace(microsecond=0))
st_ind=[]
for i,item in enumerate(dtpd_):
    if item ==date2[0]:
        st_ind.append(i)
if st_ind:    
    dtpd=dtpd[st_ind[0]:]
    p_d=p_d[st_ind[0]:]
    vx = vx[st_ind[0]:]
    vy = vy[st_ind[0]:]
    vz = vz[st_ind[0]:]
else:
    pass

p_d=np.array(p_d)
df = pd.DataFrame({'dtpd': dtpd, 'pd': p_d, 'vx': vx, 'vy': vy, 'vz': vz}, columns=['dtpd', 'pd', 'vx', 'vy', 'vz'])
df2=df.set_index('dtpd').resample('3s').mean()
df2=df2.reset_index()
df2 = pd.concat([dfS,df2], join="outer", axis=1)

df2.loc[np.where(df2['pd'] <= -1e31)[0],'pd'] = np.nan
df2.loc[np.where(df2['vx'] >=9999)[0],'vx'] = np.nan
df2.loc[np.where(df2['vy'] >=9999)[0],'vy'] = np.nan
df2.loc[np.where(df2['vz'] >=9999)[0],'vz'] = np.nan

df2=df2.reset_index()

df2['pd'] = df2['pd'].interpolate()
df2['vx'] = df2['vx'].interpolate()
df2['vy'] = df2['vy'].interpolate()
df2['vz'] = df2['vz'].interpolate()
df2['symh'] = df2['symh'].interpolate()
if df2['dtpd'].isnull().values.any():
    df2['dtpd'] = np.where(df2['dtpd'].notnull(),df2['dtpd'],df2['date'])
elif df2['date'].isnull().values.any():
    df2['date'] = np.where(df2['date'].notnull(),df2['date'],df2['dtpd'])


dtpd_list=df2['dtpd'].tolist()

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
# # MAGNETIC FIELD
# year = []
# sec_B = []
# B_mag = []
# Bx = []
# By = []
# Bz = []

# #fhandle = open(filein, 'r')
# fhandle=open('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/' +
#             str(IP_date)+'/WI_H0_MFI_API_'+str(IP_date)+'.txt', 'r')
# lines = (fhandle.readlines())
# for line in lines:
#     if line[:4].isdigit():
#         p = line.split(',')
#         year.append((p[0]))
#         #sec_B.append(float(p[1]))
#         B_mag.append(float(p[1]))
#         Bx.append(float(p[2]))
#         By.append(float(p[3]))
#         Bz.append(float(p[4]))
# fhandle.close()

# year = np.array(year)
# B_mag = np.array(B_mag)
# Bx = np.array(Bx)
# By = np.array(By)
# Bz = np.array(Bz)

# utc_time = []
# for i in range(len(year)):
#     utc_time.append(datetime.strptime(year[i], '%Y-%m-%d %H:%M:%S.%f'))



# dfb = pd.DataFrame({'dtB': utc_time, 'Bz': Bz}, columns=['dtB', 'Bz'])
# dfb2=dfb.set_index('dtB').resample('3s',origin='epoch').mean()
# dfb2=dfb2.reset_index()
# dfb2.loc[np.where(dfb2['Bz'] <= -1e31)[0],'Bz'] = np.nan
# dfb2=dfb2.reset_index()
# dfb2['Bz'] = dfb2['Bz'].interpolate()

# if df2['date'].isnull().values.any():
#     dfb2 = pd.concat([df2['dtpd'],dfb2], join="outer", axis=1)
#     if df2['dtpd'].isnull().values.any():
#         dtB_list=dfb2['dtB'].tolist()  
#     else:
#         dtB_list=dfb2['dtpd'].tolist() 

# else:
#     dfb2 = pd.concat([dfS['date'],dfb2], join="outer", axis=1)
#     if df2['date'].isnull().values.any():
#         dtB_list=dfb2['dtB'].tolist()  
#     else:
#         dtB_list=dfb2['date'].tolist()         
# #dfb2 = pd.concat([dfS['date'],dfb2], join="outer", axis=1)
# dfb2=dfb2.reset_index()
# dfb2['Bz'] = dfb2['Bz'].interpolate()

# Bz_list=dfb2['Bz'].tolist()
# Bz_list=np.array(Bz_list)

# ind_eq_B=[]
# for ind,item in enumerate(dtB_list):
#     if item==dtpd_list[-1]:
#         ind_eq_B.append(ind)
# Bz_list2=Bz_list[:ind_eq_B[0]+1]
# utc_time2=utc_time[:ind_eq_B[0]+1]
 
################################################################################################################################################################
#uprava pd a symh na rovnaku velkost, zistim kde s aim rovnaju posledne hodnoty
# print(date[0],dtpd_list[0],date[-1],dtpd_list[-1])

# if len(date) > len(dtpd_list):
#     for ind,item in enumerate(date):
#         if item==dtpd_list[-1]:
#             ind_eq=ind
#     SYM_H2=SYM_H_[:ind_eq+1]
#     date2=date[:ind_eq+1]
#     pd_list=pd_list
# else:
#     for ind,item in enumerate(dtpd_list):
#         if item==date[-1]:
#             ind_eq=ind   
#     pd_list=pd_list[:ind_eq+1]
#     date2=dtpd_list[:ind_eq+1]
#     SYM_H2=SYM_H_

# fig, ax = plt.subplots(4, figsize=(8,6),sharex=True)
# ax[0].plot(dtpd,p_d,'k',label='Pd')
# ax[0].legend(loc='best')
# ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
# ax[1].plot(date2,pd_list,'k',label='Pd interpolated')
# ax[1].legend(loc='best')
# ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
# ax[2].plot(date,SYM_H_,'r',label='SYM H')
# ax[2].legend(loc='best')
# ax[2].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
# ax[3].plot(date2,SYM_H2,'r',label='SYM H')
# ax[3].legend(loc='best')
# ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
# #plt.show()
# plt.close()

#SHOCK SPEED FOR DATAFRAME

diff_vx=np.diff(vx_list[28000:29500])
vx_jump_ind=(np.where(diff_vx==diff_vx.min()))[0][0] 

#plt.plot(vx_list)
#plt.show()

if IP_date =='CME_2010-02-15':
    st_ind= 28000 + vx_jump_ind
    end_ind=28000 + vx_jump_ind+1
    vx_jump_size.append(vx_list[end_ind] - vx_list[st_ind])
    vx_glob.append(vx_list[28000 + vx_jump_ind])

elif IP_date =='CME_2017-10-24':
    diff_vx=np.diff(vx_list[26000:29500])
    vx_jump_ind=(np.where(diff_vx==diff_vx.min()))[0][0] 
    st_ind= 26000 + vx_jump_ind -2
    end_ind=26000 + vx_jump_ind +1
    vx_jump_size.append(vx_list[end_ind] - vx_list[st_ind])
    vx_glob.append(vx_list[26000 + vx_jump_ind])

elif IP_date == 'CME_2016-01-18':
    vx_jump_size.append(-76.4)
    vx_glob.append(-360.3)   

elif IP_date == 'CME_2015-06-25':
    vx_jump_size.append(-42.5)
    vx_glob.append(-607.8)   

elif IP_date == 'CME_2014-12-23':
    vx_jump_size.append(-150.5)
    vx_glob.append(-419.4) 

elif IP_date == 'CME_2013-08-20':
    vx_jump_size.append(-20.2)
    vx_glob.append(-418.13) 

elif IP_date == 'CME_2013-07-12':
    vx_jump_size.append(-31.71)
    vx_glob.append(-410.42) 

elif IP_date == 'CME_2013-05-24':
    vx_jump_size.append(-78.9)
    vx_glob.append(-537.4) 

elif IP_date == 'CME_2013-03-17':
    vx_jump_size.append(-147.0)
    vx_glob.append(-527.5) 

elif IP_date == 'CME_2012-10-31':
    vx_jump_size.append(-52.1)
    vx_glob.append(-331.0) 

elif IP_date == 'CME_2011-11-12':
    vx_jump_size.append(-85.3)
    vx_glob.append(-411.4) 

elif IP_date == 'CME_2011-11-11':
    vx_jump_size.append(-23.3)
    vx_glob.append(-381.31) 

elif IP_date == 'CME_2014-02-20':
    vx_jump_size.append(-82.9)
    vx_glob.append(-606.8)     

else:
    st_ind=28000 + vx_jump_ind -2
    end_ind=28000 + vx_jump_ind +2
    vx_jump_size.append(vx_list[st_ind] - vx_list[end_ind])
    vx_glob.append(vx_list[28000 + vx_jump_ind])

    fig,ax1=plt.subplots(1,figsize=(7,5))
    ax1.plot(date[28000:29500],vx_list[28000:29500],'k')
    ax1.axvline(x=date[28000 + vx_jump_ind ], color='red', linestyle='--')
    ax1.axvline(x=date[st_ind], color='lime', linestyle='--')
    ax1.axvline(x=date[end_ind], color='lime', linestyle='--')
    ax1.text(0.9, 0.9, 'vx jump size: ' + str(np.round(vx_jump_size[ind_shock],5)) , horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='k')
    #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_vx/'+str(IP_date)+'_vx.pdf')
    #plt.show()


#SHOCK concentration FOR DATAFRAME
#plt.plot(pd_list)
#plt.show()

if IP_date =='CME_2010-02-15':
    n_glob.append(None)
    n_jump_size.append(None)

elif IP_date =='CME_2017-10-24':
    diff_n=np.diff(pd_list[26000:29200])     
    n_jump_ind=np.where(diff_n==diff_n.max())[0][0] 
    st_ind=26000 + n_jump_ind -2
    end_ind=26000 + n_jump_ind +2
    n_glob.append(pd_list[26000 + n_jump_ind])
    n_jump_size.append(pd_list[end_ind] - pd_list[st_ind])

elif IP_date == 'CME_2016-01-18':
    n_jump_size.append(9.68)
    n_glob.append(10.54)  

elif IP_date == 'CME_2014-12-23':
    n_jump_size.append(14.45)
    n_glob.append(16.23) 

elif IP_date == 'CME_2013-05-24':
    n_jump_size.append(5.56)
    n_glob.append(7.35) 

elif IP_date == 'CME_2013-03-17':
    n_jump_size.append(12.48)
    n_glob.append(7.82) 

elif IP_date == 'CME_2012-10-31':
    n_jump_size.append(10.52)
    n_glob.append(1.856) 

elif IP_date == 'CME_2011-11-12':
    n_jump_size.append(1.285)
    n_glob.append(1.778) 

elif IP_date == 'CME_2011-11-11':
    n_jump_size.append(2.296)
    n_glob.append(5.169) 

elif IP_date == 'CME_2014-02-20':
    n_jump_size.append(4.31)
    n_glob.append(4.105) 

elif IP_date == 'CME_2015-06-24':
    n_jump_size.append(1.771)
    n_glob.append(2.199) 

elif IP_date == 'CME_2014-02-20':
    n_jump_size.append(3.38)
    n_glob.append(5.11) 

elif IP_date == 'CME_2013-12-13':
    n_jump_size.append(8.68)
    n_glob.append(15.34) 

elif IP_date == 'CME_2012-09-04':
    n_jump_size.append(2.034)
    n_glob.append(3.286)

elif IP_date == 'CME_2011-07-11':
    n_jump_size.append(4.575)
    n_glob.append(6.844)

elif IP_date == 'CME_2011-06-04':
    n_jump_size.append(18.34)
    n_glob.append(18.56)

else:
    diff_n=np.diff(pd_list[28000:29200])     
    n_jump_ind=np.where(diff_n==diff_n.max())[0][0] 
    st_ind=28000 + n_jump_ind -2
    end_ind=28000 + n_jump_ind +2
    n_glob.append(pd_list[28000 + n_jump_ind])
    n_jump_size.append(pd_list[end_ind] - pd_list[st_ind])

    fig,ax1=plt.subplots(1,figsize=(7,5))
    ax1.plot(date[28000:29500],pd_list[28000:29500],'k')
    ax1.axvline(x=date[st_ind], color='lime', linestyle='--')
    ax1.axvline(x=date[28000 + n_jump_ind ], color='red', linestyle='--')
    ax1.axvline(x=date[end_ind], color='lime', linestyle='--')
    ax1.text(0.2, 0.9, 'n jump size: ' + str(np.round(n_jump_size[ind_shock],5)), horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='k')
    #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_n/'+str(IP_date)+'_n.pdf')
    #plt.show()

#dynamic pressure
dynamic_pressure=np.array(pd_list)*(square(vx_list) + square(vy_list) + square(vz_list) )

if IP_date =='CME_2010-02-15':
    pd_jump_size.append(None)

elif IP_date =='CME_2017-10-24':
    diff_pd=np.diff(dynamic_pressure[26000:29200])     
    pd_jump_ind=np.where(diff_pd==diff_pd.max())[0][0] 
    st_ind_pd=26000 + pd_jump_ind -2
    end_ind_pd=26000 + pd_jump_ind +2
    pd_jump_size.append(pd_list[end_ind] - pd_list[st_ind])

elif IP_date == 'CME_2011-11-12':
    pd_jump_size.append(279300)

elif IP_date == 'CME_2011-11-11':
    pd_jump_size.append(385100)

elif IP_date == 'CME_2011-07-11':
    pd_jump_size.append(1534000)

elif IP_date =='CME_2011-06-04':
    pd_jump_size.append(4300000)

elif IP_date =='CME_2012-10-31':
    pd_jump_size.append(None)

elif IP_date =='CME_2013-05-24':
    pd_jump_size.append(2951000)

elif IP_date =='CME_2013-12-13':
    pd_jump_size.append(1025000)

elif IP_date =='CME_2013-03-17':
    pd_jump_size.append(None)

elif IP_date =='CME_2014-12-23':
    pd_jump_size.append(3870000)

elif IP_date =='CME_2014-02-20':
    pd_jump_size.append(1684000)

else:
    diff_pd=np.diff(dynamic_pressure[28000:29200])     
    pd_jump_ind=np.where(diff_pd==diff_pd.max())[0][0] 
    st_ind_pd=28000 + pd_jump_ind -2
    end_ind_pd=28000 + pd_jump_ind +2
    pd_jump_size.append(dynamic_pressure[end_ind_pd] - dynamic_pressure[st_ind_pd])

    fig,ax1=plt.subplots(1,figsize=(7,5),sharex=True)
    ax1.set_title(str(IP_date),fontsize=10)
    ax1.plot(date[28000:29500],dynamic_pressure[28000:29500],'k', label='pd')
    ax1.axvline(x=date[st_ind_pd], color='lime', linestyle='--')
    ax1.axvline(x=date[28000 + pd_jump_ind ], color='red', linestyle='--')
    ax1.axvline(x=date[end_ind_pd], color='lime', linestyle='--')
    #ax1.text(0.2, 0.9, 'pd jump size: ' + str(np.round(pd_jump_size[ind_shock],2)), horizontalalignment='center', verticalalignment='center', transform=ax3.transAxes,color='k')
    ax1.legend(loc='best')
    ax1.set_xlabel('date')
    ax1.set_ylabel('pd')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_pd/'+str(IP_date)+'_v2_n_pd.pdf')
    #plt.show()
    plt.close()


#SYM-H SC 
diff_symh=np.diff(SYM_H_[24800:30800])
symh_jump_ind=(np.where(diff_symh==diff_symh.max()))[0][0] 

#print(len(date),len(dtpd_list))

if IP_date =='CME_2011-02-18':
    symh_jump_ind=symh_jump_ind-90
elif IP_date == 'CME_2010-02-15':
    symh_jump_ind=symh_jump_ind+30
elif IP_date == 'CME_2015-06-21':
    symh_jump_ind=symh_jump_ind+30
elif IP_date == 'CME_2011-09-26':
    symh_jump_ind=symh_jump_ind-30
elif IP_date == 'CME_2014-02-27':
    symh_jump_ind=symh_jump_ind+20
else:
    pass

#berem 110% zo spodu a 90% zvrchu preto po prepocitnai zo 160 bodov to je +- 16 bodov
perc_10=int(len(SYM_H_[24800 + symh_jump_ind - 70:24800 + symh_jump_ind + 75]) * 10 / 100)

#+-75 bodov odpoveda +- 4 minutam okolo SI
symh_before.append(SYM_H_[24800 + symh_jump_ind - 70 ])
symh_after.append(SYM_H_[24800 + symh_jump_ind + 75 ])
SI_size.append(symh_after[ind_shock] - symh_before[ind_shock])

symh_before_110.append(SYM_H_[24800 + symh_jump_ind - 70 + perc_10 ])
symh_after_90.append(SYM_H_[24800 + symh_jump_ind + 75 - perc_10 ])

len_=len(date[24800 + symh_jump_ind - 70 + perc_10 : 24800 + symh_jump_ind + 75 - perc_10 ])

data = pd.DataFrame({'x': date[24800 + symh_jump_ind - 70 + perc_10 : 24800 + symh_jump_ind + 75 - perc_10 ]},
                    index=pd.date_range(date[24800 + symh_jump_ind - 70 + perc_10], periods=len_, freq='3s'))
delta = (data.index - data.index[0])
seconds = delta.seconds

from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(seconds, SYM_H_[24800 + symh_jump_ind - 70 + perc_10 : 24800 + symh_jump_ind + 75 - perc_10 ])
SI_slope.append(slope)


fig, ((ax1))=plt.subplots(1, figsize=(7, 5), sharex=True, sharey=False)
ax1.plot(date[24800:32800],SYM_H_[24800:32800],color='chocolate')
ax1.set_title(str(IP_date) +' | time_lag: ' +str(time_shift/20)+' min',fontsize=10)
ax1.axvline(x=date[24800 + symh_jump_ind], color='lime', linestyle='--')
ax1.axvline(x=date[24800 + symh_jump_ind - 70 + perc_10], color='darkblue', linestyle='--')
ax1.text(0.45, 0.8, 'SYM-H before:' + str(symh_before[ind_shock]) +'nT', horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='darkblue')
ax1.axvline(x=date[24800 + symh_jump_ind + 75 - perc_10], color='darkblue', linestyle='--')
ax1.text(0.85, 0.8, 'SYM-H after:' + str(symh_after[ind_shock]) +'nT', horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='darkblue')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
ax1.legend(['ORIGINAL SYM-H'], loc='best')
ax1.set_ylabel('SYM-H [nT]',rotation=60, ha='right',fontsize=10)
ax1.tick_params(axis='both',labelsize=10,labelbottom=True)
ax1.text(0.2, 0.9, 'Slope of SI: ' +str(round(slope,5)), horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='chocolate')
#plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_symh/'+str(IP_date)+'_SYM_H_SI.pdf')
#plt.show()
plt.close()

######################################################################################################################################################
#GEOMAGETIC FIELD BUDKOV
year_B = []
sec_B = []
Bx = []
By = []
Bz = []

#fhandle = open(filein, 'r')
fhandle=open('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/' +
            str(IP_date)+'/magnetograms/m_'+str(IP_date)+'.txt', 'r')
lines = (fhandle.readlines())
for line in lines:
    if line[:4].isdigit():
        p = line.split(' ')
        year_B.append((p[0]))
        sec_B.append((p[1]))
        Bx.append(float(p[2]))
        By.append(float(p[3]))
        Bz.append(float(p[4]))
fhandle.close()

year_B = np.array(year_B)
sec_B = np.array(sec_B)
Bx = np.array(Bx)
By = np.array(By)
Bz = np.array(Bz)

utc_time = []
for i in range(len(year_B)):
    utc_time.append(datetime.strptime(year_B[i] + sec_B[i], '%Y-%m-%d%H:%M:%S.%f'))

df_geo = pd.DataFrame({'dtpd': utc_time, 'Bx': Bx, 'By': By, 'Bz': Bz}, columns=['dtpd', 'Bx', 'By', 'Bz'])
df_geo=df_geo.reset_index()

df_geo.loc[np.where(df_geo['Bx'] >=99999)[0],'Bx'] = np.nan
df_geo.loc[np.where(df_geo['By'] >=99999)[0],'By'] = np.nan
df_geo.loc[np.where(df_geo['Bz'] >=99999)[0],'Bz'] = np.nan
df_geo=df_geo.reset_index()

df_geo['Bx'] = df_geo['Bx'].interpolate()
df_geo['By'] = df_geo['By'].interpolate()
df_geo['Bz'] = df_geo['Bz'].interpolate()

Bx=df_geo['Bx'].tolist()
By=df_geo['By'].tolist()
Bz=df_geo['Bz'].tolist()

B_mag=[]
for i in range(len(Bx)):
    B_mag.append(math.sqrt(Bx[i]**2 +By[i]**2  +Bz[i]**2 ))

#DELTA BX, BY, BZ, B_mag
DBx= np.diff(Bx)
DBy= np.diff(By)
DBz= np.diff(Bz)
DB_mag=np.diff(B_mag)

sqrt_DB_mag=[]
for i in range(len(DBx)):
    sqrt_DB_mag.append(math.sqrt(DBx[i]**2 + DBy[i]**2 + DBz[i]**2))


symh_SI_time=date[24800 + symh_jump_ind]
diff_B=np.diff(B_mag)
B_jump_ind=(np.where(diff_B==diff_B.max()))[0][0] 
#B mag
fig, ((ax1))=plt.subplots(1, figsize=(7, 6), sharex=True, sharey=False)
ax1.plot(utc_time,B_mag,color='chocolate')
ax1.set_title(str(IP_date) ,fontsize=10)
ax1.axvline(x=symh_SI_time, color='dodgerblue', linestyle='--')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
ax1.tick_params(axis='both',labelsize=10,labelbottom=True, rotation=30)
ax1.set_ylabel('B magnitude',fontsize=10)
ax1.set_xlabel('Date&Time',fontsize=10)
ax1.text(0.43, 0.9, str(symh_SI_time) , horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='dodgerblue')
#plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_B_mag/'+str(IP_date)+'_B_mag.pdf')
#plt.show()

#DB mag
if IP_date == 'CME_2015-05-06':
    pass
else:
    #rounded_utc_time=utc_time.replace(second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S')
    rounded_utc_time=[i.strftime('%Y-%m-%d %H:%M:%S') for i  in utc_time]
    date_interval=[item.strftime('%Y-%m-%d %H:%M:%S') for i,item  in enumerate(date) if i==24800 or i ==32800]
    SI_ind_st=[i for i,item  in enumerate(rounded_utc_time) if item==date_interval[0]][0]
    SI_ind_end=[i for i,item  in enumerate(rounded_utc_time) if item==date_interval[1]][0]
    
    fig, ((ax1,ax2,ax3))=plt.subplots(3, figsize=(10, 9), sharex=True, sharey=False)
    ax1.plot(utc_time[SI_ind_st : SI_ind_end],DB_mag[SI_ind_st: SI_ind_end],color='chocolate')
    ax1.set_title(str(IP_date) ,fontsize=10)
    ax1.axvline(x=symh_SI_time, color='dodgerblue', linestyle='--')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax1.tick_params(axis='both',labelsize=10,labelbottom=True)
    ax1.set_ylabel('Delta B ',fontsize=10,rotation=60,)
    ax1.text(0.43, 0.9, str(symh_SI_time) , horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='dodgerblue')
    
    ax2.plot(date[24800:32800],SYM_H_[24800:32800],color='chocolate')
    ax2.axvline(x=date[24800 + symh_jump_ind], color='dodgerblue', linestyle='--')
    ax2.axvline(x=date[24800 + symh_jump_ind - 70 + perc_10], color='darkblue', linestyle='--')
    ax2.text(0.45, -0.4, 'SYM-H before:' + str(symh_before[ind_shock]) +'nT', horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='darkblue')
    ax2.axvline(x=date[24800 + symh_jump_ind + 75 - perc_10], color='darkblue', linestyle='--')
    ax2.text(0.85, -0.4, 'SYM-H after:' + str(symh_after[ind_shock]) +'nT', horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='darkblue')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax2.legend(['ORIGINAL SYM-H'], loc='best')
    ax2.set_ylabel('SYM-H [nT]',rotation=60, ha='right',fontsize=10)
    ax2.tick_params(axis='both',labelsize=10,labelbottom=True)

    ax3.plot(utc_time[SI_ind_st: SI_ind_end],sqrt_DB_mag[SI_ind_st : SI_ind_end],color='chocolate')
    ax3.axvline(x=symh_SI_time, color='dodgerblue', linestyle='--')
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax3.tick_params(axis='both',labelsize=10,labelbottom=True)
    ax3.set_ylabel('sqrt Delta B ',fontsize=10,rotation=60,)
    ax3.set_xlabel('Date&Time',fontsize=10)
    ax3.text(0.43, -1.5, str(symh_SI_time) , horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='dodgerblue')
    #print(datetime.combine(symh_SI_time.date(), time(23, 0, 0)), datetime.combine(symh_SI_time.date() + timedelta(days=1), time(1, 0, 0)),symh_SI_time )
  
    if datetime.combine(symh_SI_time.date(), time(11, 0, 0))< symh_SI_time < datetime.combine(symh_SI_time.date(), time(13, 0, 0)) :
        plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_DB_mag_before_12/'+str(IP_date)+'_B_mag.pdf')
    
    elif datetime.combine(symh_SI_time.date(), time(23, 0, 0))< symh_SI_time < datetime.combine(symh_SI_time.date() + timedelta(days=1), time(1, 0, 0)) :
        plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_DB_mag_after_12/'+str(IP_date)+'_B_mag.pdf')
    
    elif datetime.combine(symh_SI_time.date() - timedelta(days=1), time(23, 0, 0)) < symh_SI_time < datetime.combine(symh_SI_time.date() , time(1, 0, 0)) :
        plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_DB_mag_after_12/'+str(IP_date)+'_B_mag.pdf')
    
    else:
        plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_DB_mag/'+str(IP_date)+'_B_mag.pdf')
    #plt.show()

    #sqrt  DB mag
    # fig, ((ax1))=plt.subplots(1, figsize=(7, 6), sharex=True, sharey=False)
    # ax1.plot(utc_time[SI_ind_st: SI_ind_end],sqrt_DB_mag[SI_ind_st : SI_ind_end],color='chocolate')
    # ax1.set_title(str(IP_date) ,fontsize=10)
    # ax1.axvline(x=symh_SI_time, color='dodgerblue', linestyle='--')
    # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    # ax1.tick_params(axis='both',labelsize=10,labelbottom=True, rotation=30)
    # ax1.set_ylabel('SQRT Delta B ',fontsize=10)
    # ax1.set_xlabel('Date&Time',fontsize=10)
    # ax1.text(0.43, 0.9, str(symh_SI_time) , horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes,color='dodgerblue')
    # #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_sqrt_DB_mag/'+str(IP_date)+'_B_mag.pdf')
    # plt.show()

######################################################################################################################################################


print('File ' + str (IP_date)+ ' was processed')

######################################################################################################################################################
#t=48
#orezanie na hodinu okolo skokov
#pd_list=pd_list[int(len(pd_list)/2)-int(len(pd_list)/t*2):int(len(pd_list)/2)+int(len(pd_list)/t*2)]
#SYM_H=SYM_H[int(len(SYM_H)/2)-int(len(SYM_H)/t*2):int(len(SYM_H)/2)+int(len(SYM_H)/t*2)]
#date2=date2[int(len(date2)/2)-int(len(date2)/t*2):int(len(date2)/2)+int(len(date2)/t*2)]

#hladam kde nastal skutocny skok vo vx + neriesim absolutnu hodnotu diff aby som zabezpecila ze skok je do kladnych cisel
# diff_pd=np.diff(pd_list)    
#diff_pd_=[abs(x) for x in diff_pd]
#dotatocna podmienky aby sa bral skok v rozmezi hodiny od skoku pre SYM-H
# size=10
# where_pd_max=np.array(diff_pd[int(len(diff_pd)/2)-size:int(len(diff_pd)/2)+size])
# pd_jump_ind=(np.where(diff_pd==where_pd_max.max()))[0][0] 
# #pd_jump_ind=(np.where((diff_pd_==max(diff_pd_)))[0][0] 

# #hladam kde nastal skutocny skok v sym-h
# size2=70
# new_symh=[]
# for ind,item in enumerate(SYM_H2):
#     if ind<=int(len(SYM_H2)/2)-size2:
#         new_symh.append(0)
#     elif ind>=int(len(SYM_H2)/2)+size2:
#         new_symh.append(0)
#     else:
#         new_symh.append(item)

# diff_symh=np.diff(new_symh)  
# ind_diff_symh=np.where((diff_symh >0) & (diff_symh==diff_symh.max()))[0][0]

# while ind_diff_symh < pd_jump_ind:
#     #diff_symh=np.delete(diff_symh,diff_symh.max())
#     diff_symh[ind_diff_symh]=0
#     ind_diff_symh=np.where( diff_symh==diff_symh.max())[0][0]
#     if ind_diff_symh-120 > pd_jump_ind:
#         continue
#     else:
#         pass
    
# #diff_symh_=[abs(x) for x in diff_symh]
# #where_symh_max=np.array(diff_symh[int(len(diff_symh)/2)-size2:int(len(diff_symh)/2)+size2])
# symh_jump_ind=(np.where(diff_symh==diff_symh.max()))[0][0] 

# # #difference of jump time in vx and SC in SYM-H
# time_lags_pd_symh=[]
# time_lags_pd_symh.append(date2[symh_jump_ind]-date2[pd_jump_ind])

# #vykreslenie grafov
# fig, ((ax1),(ax2))=plt.subplots(2, figsize=(8, 6), sharex=True, sharey=False)
# ax1.plot(date2,pd_list,'r') # P_d
# ax1.set_title(str(IP_date) +' | time_lag: ' +str(time_lags_pd_symh[0]) ,fontsize=10)
# ax1.axvline(x=date2[pd_jump_ind], color='k', linestyle='--') # ciara kde je skok
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
# ax1.legend(['P_d'], loc='best')
# ax1.set_ylabel('P_d [nPa]',rotation=30, ha='right',fontsize=10)
# ax1.tick_params(axis='both',labelsize=10,labelbottom=True)
# ax1.annotate('jump time '+ str(date2[pd_jump_ind].time()), xy=(1,1), xycoords = 'axes fraction',xytext=(0.4, 0.5))

# ax2.plot(date2, SYM_H2,'r') #SYM-H
# ax2.axvline(x=date2[symh_jump_ind], color='k', linestyle='--') # ciara kde je skok
# ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
# ax2.legend(['SYM-H'], loc='best')
# ax2.set_ylabel('SYM-H [nT]',rotation=30, ha='right',fontsize=10)
# ax2.tick_params(axis='both',labelsize=10)
# ax2.annotate('jump time '+ str(date2[symh_jump_ind].time()), xy=(1,1), xycoords = 'axes fraction',xytext=(0.4, 0.5))
# plt.setp(ax1.get_xticklabels(), visible=True)
# #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/time_lag_pd_symh/'+str(IP_date)+'_time_lag_pd_symh.pdf')
# #plt.show()
# plt.close(fig)
# ######################################################################################################################################################
# #PREPOCET NA MAGNETOPAUZU 
# dynamic_pressure=pd_list

# dynamic_pressure=dynamic_pressure.tolist()
# delta_symh=[]
# for ind,item in enumerate(dynamic_pressure):
#     delta_symh.append(20 * math.sqrt(item/1.6) + 20)

# for i in range(0,time_shift):
#     delta_symh.insert(0,None) 
# delta_symh=delta_symh[:len(delta_symh)-time_shift]    

# corrected_symh=[]
# for ind,item in enumerate(delta_symh):
#     if item is not None and ind <len(SYM_H2):
#         corrected_symh.append(SYM_H2[ind] - delta_symh[ind]) 
#     elif item is None:
#         corrected_symh.append(None)
#     else: 
#         pass

# with open('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/'+str(IP_date)+'/CORRECTED_SYM_H_'+str(IP_date)+'.txt','w') as f:
#     lis=[np.array(date2),np.array(corrected_symh)]
#     for x in zip(*lis):
#         f.write("{0}\t{1}\n".format(*x))



# fig, ((ax1),(ax2)) = plt.subplots(2, figsize=(8,6),sharex=True, sharey=False)
# ax1.plot(date2[24800:32800] ,SYM_H2[24800:32800],'g')
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
# ax1.set_title(str(IP_date) +' | time_lag: ' +str(time_lags_pd_symh[0]) ,fontsize=10)
# ax1.legend(['SYM-H'], loc='best')
# ax1.set_ylabel('SYM-H [nT]',rotation=30, ha='right',fontsize=10)
# ax1.tick_params(axis='both',labelsize=10,labelbottom=True)

# ax2.plot(date2[24800:32800],delta_symh[24800:32800],'r')
# ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
# ax2.legend(['delta SYM-H'], loc='best')
# ax2.set_ylabel('p_d [nPa]',rotation=30, ha='right',fontsize=10)
# ax2.tick_params(axis='both',labelsize=10,labelbottom=True)
# #lt.show()
# plt.close()    

# fig, ((ax1),(ax2),(ax3))=plt.subplots(3, figsize=(8, 6), sharex=True, sharey=False)
# ax1.plot(date2[24800:32800],SYM_H2[24800:32800],'r')
# ax1.set_title(str(IP_date) +' | time_lag: ' +str(time_shift)+' min',fontsize=10)
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
# ax1.legend(['ORIGINAL SYM-H'], loc='best')
# ax1.set_ylabel('SYM-H [nT]',rotation=60, ha='right',fontsize=10)
# ax1.tick_params(axis='both',labelsize=10,labelbottom=True)

# ax2.plot(date2[24800:32800],delta_symh[24800:32800],'r',label='delta SYM-H')
# ax2.plot(date2[24800:32800],dynamic_pressure[24800:32800],'b',label='dynamic pressure')
# ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
# ax2.legend(loc='best')
# ax2.set_ylabel('DELTA SYM-H [nT]',rotation=60, ha='right',fontsize=10)
# ax2.tick_params(axis='both',labelsize=10,labelbottom=True)

# ax3.plot(date2[24800:32800],corrected_symh[24800:32800],'r')
# ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
# ax3.legend(['CORRECTED SYM-H'], loc='best')
# ax3.set_ylabel('SYM-H [nT]',rotation=60, ha='right',fontsize=10)
# ax3.tick_params(axis='both',labelsize=10,labelbottom=True)
# ax3.tick_params(axis='both',labelsize=10)
# plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs/'+str(IP_date)+'orig_correlat_symh.pdf')
# #plt.show()
# plt.close(fig)   
# ####################################################################################################################################################################################################################################
# Bz_vx = (Bz_list2*vx_list)

# for specific_time in range(7, 20):
#     Bz_vx_integral = [None]*len(Bz_vx)
#     for i in range(len(Bz_vx)):
#         if i-specific_time*60 > 0 and i < len(Bz_vx):
#             Bz_vx_integral[i] = ((Bz_vx[i-specific_time*60:i]).sum())
#         else:
#             Bz_vx_integral[i] = None

#     # INTEGRAL OF Bz.vx
#     Bz_integral = [None]*len(Bz_list2)

#     # integral BZ only, cele to dam to for cyklu a pre kazde i si vygenerujem grafy
#     for i in range(len(Bz_list2)):
#         if i-specific_time*60 > 0 and i < len(Bz_list2):
#             Bz_integral[i] = ((Bz_list2[i-specific_time*60:i]).sum())
#         else:
#             Bz_integral[i] = None

#     # PLOT DATA
#     Bz_vx_integral2=[]
#     for i in Bz_vx_integral:
#         if i is not None:
#             Bz_vx_integral2.append(i)
#         else:
#             pass  

#     corrected_symh2=[]
#     for i in corrected_symh:
#         if i is not None:
#             corrected_symh2.append(i)
#         else:
#             pass   

#     fig, ax = plt.subplots(5, figsize=(8,6), sharex=True)
#     ax[0].plot(date2, Bz_vx_integral, color='r', linewidth=0.5)
#     ax[0].legend(['Bz_vx_integral'], loc='best')
#     ax[0].set_title(str(IP_date)+' - '+str(specific_time)+' hour integration interval',fontsize=10.5)
#     ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
#     ax[0].set_ylabel('Bz_vx_integral',rotation=30, ha='right',fontsize=10.5)
#     ax[0].tick_params(axis='both',labelsize=10.5)

#     ax[1].plot(date2, Bz_list2, color='b', linewidth=0.5)
#     ax[1].legend(['Bz'], loc='best')
#     ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
#     ax[1].set_ylabel('Bz[nT]',rotation=30, ha='right',fontsize=10.5)
#     ax[1].tick_params(axis='both',labelsize=10.5)

#     ax[2].plot(date2, vx_list, color='purple', linewidth=0.5)
#     ax[2].legend(['vx'], loc='best')
#     ax[2].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
#     ax[2].set_ylabel('vx [km/s]',rotation=30, ha='right',fontsize=10.5)
#     ax[2].tick_params(axis='both',labelsize=10.5)

#     ax[3].plot(date, SYM_H, color='darkgreen', linewidth=0.5)
#     ax[3].set_xlabel('TIME',fontsize=10.5)
#     ax[3].legend(['SYM-H'], loc='best')
#     ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
#     ax[3].axvline(x=date[symh_jump_ind], color='k', linestyle='--',linewidth=0.5)
#     ax[3].set_ylabel('SYM-H [nT]',rotation=30, ha='right',fontsize=10.5)
#     ax[3].tick_params(axis='both',labelsize=10.5)

#     ax[4].plot(date2,corrected_symh,'k',linewidth=0.5)
#     ax[4].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:'))
#     ax[4].legend(['CORRECTED SYM-H'], loc='best')
#     ax[4].set_ylabel('SYM-H [nT]',rotation=30, ha='right',fontsize=10)
#     ax[4].set_xlabel('TIME',fontsize=10.5)
#     ax[4].tick_params(axis='both',labelsize=10.5,labelbottom=True)
#     ax[4].tick_params(axis='both',labelsize=10.5)   

#     fig.autofmt_xdate()
#     plt.setp(ax[0].get_xticklabels(), visible=True)
#     plt.setp(ax[1].get_xticklabels(), visible=True)
#     plt.setp(ax[2].get_xticklabels(), visible=True)
#     plt.setp(ax[3].get_xticklabels(), visible=True)

#     base_0 = abs(int((max(Bz_vx_integral2)-min(Bz_vx_integral2))/5))    
#     max_len_0 = (len(str(int(base_0))))
#     round_0 = round(base_0, -max_len_0+1)
#     # this locator puts ticks at regular intervals
#     loc0 = plticker.MultipleLocator(base=round_0)
#     ax[0].yaxis.set_major_locator(loc0)

#     max_len_1=(len(str(int(abs(max(Bz_list2))))))
#     base_1 = abs(int((max(Bz_list2)-min(Bz_list2))/5))
#     max_len_1 = (len(str(int(base_1))))
#     round_1 = round(base_1, -max_len_1+1)
#     loc1 = plticker.MultipleLocator(base=round_1)
#     ax[1].yaxis.set_major_locator(loc1)

#     base_2 = abs(int((max(vx_list)-min(vx_list))/5))
#     max_len_2 = (len(str(int(base_2))))
#     round_2 = round(base_2, -max_len_2+1)
#     loc2y = plticker.MultipleLocator(base=round_2)
#     ax[2].yaxis.set_major_locator(loc2y)

#     base_3 = abs(int((max(SYM_H)-min(SYM_H))/5))
#     max_len_3 = (len(str(int(base_3))))
#     round_3 = round(base_3, -max_len_3+1)
#     loc3 = plticker.MultipleLocator(base=round_3)
#     ax[3].yaxis.set_major_locator(loc3)

#     base_4 = abs(int((max(corrected_symh2)-min(corrected_symh2))/6))
#     max_len_4 = (len(str(int(base_4))))
#     round_4 = round(base_4, -max_len_4+1)
#     loc4 = plticker.MultipleLocator(base=round_4)
#     ax[4].yaxis.set_major_locator(loc4)

#     plt.tight_layout()
#     #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/'+str(IP_date)+'/graphs_png/'+str(IP_date)+':'+str(specific_time)+'.png')
#     #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/Mag_field_integrals_2/'+str(specific_time)+'/Mag_field_integral'+str(IP_date)+'.pdf')
#     #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_for_WDS/'+str(IP_date)+':'+str(specific_time)+'h.pdf')
#     plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_for_WDS/'+str(IP_date)+':'+str(specific_time)+'h.pdf')
#     plt.show()
#     plt.close(fig)

# ################################################################################################################################################################################################
#     # CORELATION
#     corrected_symh=np.array(corrected_symh)
#     if specific_time == 15:

#         #Bz_vx_integral_ = np.array(Bz_vx_integral)

#         #INTERPOL = interp.interp1d(np.arange(Bz_vx_integral_.size), Bz_vx_integral_)
#         #COMPRESS_integral = INTERPOL(np.linspace(0, Bz_vx_integral_.size-1, SYM_H_.size))
#         #COMPRESS_integral_corrected = INTERPOL(np.linspace(0, Bz_vx_integral_.size-1, corrected_symh.size))

#         #IP_index = int(len(COMPRESS_integral)/2)
#         IP_index=symh_jump_ind

#         korelace = []
#         korelace_corrected=[]
#         korelace_soucin = []
#         korelace_soucin_corrected = []
#         hms_day = []
#         DAYS = []
#         MJD = []

#         for i in date2:
#             hms_day.append(hmsm_to_days(hour=i.hour, min=i.minute))
#             DAYS.append(i.date())

#         for i in range(len(DAYS)):
#             MJD.append(date_to_mjd(
#                 DAYS[i].year, DAYS[i].month, DAYS[i].day + hms_day[i]))
#         MJD = np.array(MJD)

#         # xova osa korelacnych grafov
#         dt_corc = ((MJD-MJD[IP_index])*24*60)

#         cor_wind=900 #(15 hod)
#         # soucin
#         Bz_vx_ = np.array(Bz_vx)
#         Bz_vx2 = Bz_vx_[IP_index - cor_wind: IP_index + cor_wind]

#         # integral
#         Bz_vx_integral_=np.array(Bz_vx_integral)
#         Bz_vx_integral_ = Bz_vx_integral_[IP_index - cor_wind: IP_index + cor_wind]
#         Bz_vx_integral_ = Bz_vx_integral_.astype('float64') #is naan hadzal error kvoli datovemu type
#         nan_int_indx = np.argwhere(np.isnan(Bz_vx_integral_))


#         for i in range(len(SYM_H2)):
#             #if i - 6*cor_wind > 0 and i+6*cor_wind < len(SYM_H_):
#             if i - cor_wind > 0 and i+cor_wind < len(SYM_H2):
#                 #sym_h = SYM_H_[i-6*cor_wind: i + 6*cor_wind]
#                 sym_h = SYM_H2[i-cor_wind: i + cor_wind]
#                 if nan_int_indx.any():
#                     korelace.append(pearsonr(sym_h[nan_int_indx[-1][0]+1:], Bz_vx_integral_[nan_int_indx[-1][0]+1:])[0])
#                     korelace_soucin.append(pearsonr(sym_h, Bz_vx2)[0])
#                 else:
#                     korelace.append(pearsonr(sym_h[1:], Bz_vx_integral_[1:])[0])
#                     korelace_soucin.append(pearsonr(sym_h, Bz_vx2)[0])
#             else:
#                 sym_h = None
#                 korelace.append(None)
#                 korelace_soucin.append(None)

#         df_corr = pd.DataFrame({'symh_corr': corrected_symh}, columns=[ 'symh_corr'])
#         df_corr=df_corr.reset_index()
#         df_corr['symh_corr'] = df_corr['symh_corr'].interpolate(method='nearest').ffill().bfill()
#         symh_corr_list=df_corr['symh_corr'].tolist()


#         for i in range(len(corrected_symh)):
#             if i - cor_wind > 0 and i+cor_wind < len(corrected_symh):
#                 sym_h_corrected=symh_corr_list[i-cor_wind: i + cor_wind]
#                 if nan_int_indx.any(): #and corrected_symh[i-cor_wind]== None or corrected_symh[i+cor_wind]== None:
#                     #korelace_corrected.append(None)
#                     korelace_corrected.append(pearsonr(sym_h_corrected[nan_int_indx[-1][0]+1:], Bz_vx_integral_[nan_int_indx[-1][0]+1:])[0])
#                     korelace_soucin_corrected.append(pearsonr(sym_h_corrected, Bz_vx2)[0])
#                 else:
#                     korelace_corrected.append(pearsonr(sym_h_corrected[1:], Bz_vx_integral_[1:])[0])
#                     korelace_soucin_corrected.append(pearsonr(sym_h_corrected[1:], Bz_vx2[1:])[0])
#             else:
#                 korelace_corrected.append(None)
#                 korelace_soucin_corrected.append(None)


#         fig, ax = plt.subplots(3,figsize=(10,8),sharex=True)
#         ax[0].plot(SYM_H2,)
#         ax[0].legend(['SYM-H'], loc='best')
#         ax[1].plot(Bz_vx_integral)
#         ax[1].legend(['integral'], loc='best')
#         ax[2].plot(corrected_symh)
#         ax[2].legend(['corrected SYM-H'], loc='best')
#         #plt.show()
#         plt.close(fig)

#         fig, ax = plt.subplots(2,figsize=(10,8))
#         #ax[0].plot(korelace[IP_index - 6*cor_wind : IP_index + 6*cor_wind], 'r' )
#         ax[0].plot(korelace[IP_index - cor_wind : IP_index + cor_wind], 'r' )
#         ax[0].legend(['correlation'], loc='best')
#         ax[0].set_ylabel('correlation coeficient',rotation=30)
#         #ax[1].plot(korelace_corrected[IP_index - 6*cor_wind : IP_index + 6*cor_wind], 'k')
#         ax[1].plot(korelace_corrected[IP_index - cor_wind : IP_index + cor_wind], 'k')
#         ax[1].legend(['corrected correlation'], loc='best')
#         ax[1].set_ylabel('correlation coeficient',rotation=30)
#    #    plt.show()
#         plt.close(fig)
#         # korelace.append(np.correlate(Bz_vx_integral_,sym_h))

#         #####TIEM LAG FOR MINIMUM CORRELATION
#         corr = []
#         corr_corrected=[]
#         for ind,item in enumerate(korelace):
#             if item is not None:
#                 corr.append(item)
#             else:
#                 pass
#         min_corr = min(corr)
#         indices_for_minimum_lag=(korelace.index(min_corr))
#         min_lag=round(dt_corc[indices_for_minimum_lag])

#         corr_corrected=[]
#         for ind,item in enumerate(korelace_corrected):
#             if item is not None:
#                 corr_corrected.append(item)
#             else:
#                 pass
#         min_corr_corrected = min(corr_corrected)
#         indices_for_minimum_lag_corrected=(korelace_corrected.index(min_corr_corrected))
#         min_lag_corrected=round(dt_corc[indices_for_minimum_lag_corrected])

#         corr2 = []
#         for ind,item in enumerate(korelace_soucin):
#             if item is not None:
#                 corr2.append(item)
#             else:
#                 pass
#         min_corr2 = min(corr2)
#         indices_for_minimum_lag2=(korelace_soucin.index(min_corr2))
#         min_lag2=round(dt_corc[indices_for_minimum_lag2])  

#         corr2_corrected = []
#         for ind,item in enumerate(korelace_soucin_corrected):
#             if item is not None:
#                 corr2_corrected.append(item)
#             else:
#                 pass
#         min_corr2_corrected = min(corr2_corrected)
#         indices_for_minimum_lag2_corrected=(korelace_soucin_corrected.index(min_corr2_corrected))
#         min_lag2_corrected=round(dt_corc[indices_for_minimum_lag2_corrected]) 

#         fig, ax = plt.subplots(4, figsize=(8,8))
#         ax[0].plot(dt_corc, korelace)
#         ax[0].set_title(' Date: ' + str(IP_date)+' | ' + ' Integrating time: '+str(specific_time)+' hours')
#         ax[0].legend(['Pearson Correlation int(Bz*vx)'], loc='left')
#         ax[0].tick_params(axis='both',labelsize=10.5)
#         ax[0].set_xlim(-1500, 1500)
#         ax[0].set_ylim(-1, 1)
#         ax[0].set_ylabel('correlation coefficient',fontsize=10.5,rotation=30)
#         ax[0].annotate('min time lag '+ str(min_lag) +' min', xy=(min_lag, min_corr), xytext=(0, 0),arrowprops=dict(width=0.5,headwidth=5,facecolor='black', shrink=5))
#         ax[0].annotate('min corr '+str(round(min_corr,2)), xy=(min_lag, min_corr), xytext=(-0.8, -0.8)) 

#         ax[1].plot(dt_corc, korelace_corrected)
#         ax[1].legend(['Pearson Correlation int(Bz*vx) corrected'], loc='left')
#         ax[1].annotate('min time lag '+str(min_lag_corrected) +' min', xy=(min_lag_corrected, min_corr_corrected), xytext=(0, 0),arrowprops=dict(width=0.5,headwidth=5,facecolor='black', shrink=5))
#         ax[1].annotate('min corr ' + str(round(min_corr2,2)), xy=(min_lag_corrected, min_corr_corrected), xytext=(-0.8, -0.8))     
#         ax[1].set_xlim(-1500, 1500)
#         ax[1].set_ylim(-1, 1)
#         ax[1].set_ylabel('correlation coefficient',fontsize=10.5,rotation=30)
#         ax[1].tick_params(axis='both',labelsize=10.5)

#         ax[2].plot(dt_corc, korelace_soucin)
#         ax[2].legend(['Pearson Correlation Bz*vx'], loc='best')
#         ax[2].annotate('min time lag '+str(min_lag2) +' min', xy=(min_lag2, min_corr2), xytext=(0, 0),arrowprops=dict(width=0.5,headwidth=5,facecolor='black', shrink=5))
#         ax[2].annotate('min corr ' + str(round(min_corr2,2)), xy=(min_lag2, min_corr), xytext=(-0.8, -0.8))     
#         ax[2].set_xlim(-1500, 1000)
#         ax[2].set_ylim(-1, 1)
#         ax[2].set_ylabel('correlation coefficient',fontsize=10.5,rotation=30)
#         ax[2].tick_params(axis='both',labelsize=10.5)

#         ax[3].plot(dt_corc, korelace_soucin_corrected)
#         ax[3].legend(['Pearson Correlation Bz*vx corrected'], loc='best')
#         ax[3].annotate('min time lag '+str(min_lag2_corrected) +' min', xy=(min_lag2_corrected, min_corr2_corrected), xytext=(0, 0),arrowprops=dict(width=0.5,headwidth=5,facecolor='black', shrink=5))
#         ax[3].annotate('min corr ' + str(round(min_corr2_corrected,2)), xy=(min_lag2_corrected, min_corr_corrected), xytext=(-0.8, -0.8))     
#         ax[3].set_xlim(-1500, 1500)
#         ax[3].set_ylim(-1, 1)
#         ax[3].set_ylabel('correlation coefficient',fontsize=10.5,rotation=30)
#         ax[3].tick_params(axis='both',labelsize=10.5)

#         # ax[2].plot(dt_corc, kendall)
#         # ax[2].legend(['Kendall Correlation'], loc='best')
#         # ax[2].set_xlabel('Time lags')
#         # ax[3].plot(np_corr)
#         # ax[3].legend(['Numpy Correlation'],loc='best')
#         # ax[3].set_xlabel('Time lags')

#         #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/graphs_for_WDS/corr_graph'+str(IP_date)+':'+str(specific_time)+'h.pdf')
#         #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/' +
#         #            str(IP_date)+'/corr_graphs/'+str(IP_date)+':'+str(specific_time)+'.png')
#         plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/corr_graphs/'+str(IP_date)+':'+str(specific_time)+'.png')
#         #plt.savefig('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/corr_graphs2/corr_graphs_for_7hours/'+str(IP_date)+':'+str(specific_time)+'.pdf')  
#         #plt.show()
#         plt.close(fig)
#     else:
#         pass

#     #print('INTEGRATION TIME: ' + str(specific_time))

# print('FILE: ' + str(each_file))
