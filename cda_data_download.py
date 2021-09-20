from ai import cdas
import json
from datetime import datetime
from matplotlib import pyplot as plt
import requests
import numpy as np

# variables = cdas.get_variables('istp_public', 'WI_K0_3DP')
#print(json.dumps(variables, indent=4))

# datasets = cdas.get_datasets(
#     'istp_public',
#     idPattern='WI_K0_3DP.*',
#     labelPattern='.*W.*'
# )
#print(json.dumps(datasets, indent=4))

# variables = cdas.get_variables('istp_public', 'WI_PM_3DP')
# print(json.dumps(variables, indent=4))

# datasets = cdas.get_datasets(
#     'istp_public',
#     idPattern='WI_K0_3DP.*',
#     labelPattern='.*W.*'
# )
#print(json.dumps(datasets, indent=4))

# data = cdas.get_data(
#     'sp_phys',
#     'WI_PM_3DP',
#     datetime(2019, 10, 10),
#     datetime(2019, 10, 11, 0, 59, 59),
#     ['P_DENS', 'P_VELS'] 
# )
# print(data)
# plt.plot(data['EPOCH'], data['DENS_PROTN_S/C']) #VXGSE_PROTN_S/C, VYGSE_PROTN_S/C,VZGSE_PROTN_S/C
# plt.show()

#76 IP SHOCKs
file_name=[ 'CME_2010-02-15/WI_PM_3DP_CME_2010-02-15.txt'

    # ,'CME_2011-08-04/WI_PM_3DP_CME_2011-08-04.txt', 
    # 'CME_2011-08-05/WI_PM_3DP_CME_2011-08-05.txt', 
    # 'CME_2011-11-12/WI_PM_3DP_CME_2011-11-12.txt', 
    # 'CME_2011-11-11/WI_PM_3DP_CME_2011-11-11.txt', 
    # 'CME_2011-09-26/WI_PM_3DP_CME_2011-09-26.txt', 
    # 'CME_2011-09-25/WI_PM_3DP_CME_2011-09-25.txt', 
    # 'CME_2011-07-11/WI_PM_3DP_CME_2011-07-11.txt', 
    # 'CME_2011-06-04/WI_PM_3DP_CME_2011-06-04.txt', 
    # 'CME_2011-04-18/WI_PM_3DP_CME_2011-04-18.txt', 
    # 'CME_2011-02-18/WI_PM_3DP_CME_2011-02-18.txt', 
    # 'CME_2011-02-14/WI_PM_3DP_CME_2011-02-14.txt',

    # 'CME_2012-11-26/WI_PM_3DP_CME_2012-11-26.txt', 
    # 'CME_2012-11-23/WI_PM_3DP_CME_2012-11-23.txt', 
    # 'CME_2012-11-12/WI_PM_3DP_CME_2012-11-12.txt', 
    # 'CME_2012-10-31/WI_PM_3DP_CME_2012-10-31.txt', 
    # 'CME_2012-10-08/WI_PM_3DP_CME_2012-10-08.txt', 
    # 'CME_2012-09-30/WI_PM_3DP_CME_2012-09-30.txt', 
    # 'CME_2012-09-04/WI_PM_3DP_CME_2012-09-04.txt', 
    # 'CME_2012-09-03/WI_PM_3DP_CME_2012-09-03.txt', 
    # 'CME_2012-07-14/WI_PM_3DP_CME_2012-07-14.txt', 
    # 'CME_2012-06-16/WI_PM_3DP_CME_2012-06-16.txt', 
    # 'CME_2012-05-21/WI_PM_3DP_CME_2012-05-21.txt', 
    # 'CME_2012-04-23/WI_PM_3DP_CME_2012-04-23.txt', 
    # 'CME_2012-03-07/WI_PM_3DP_CME_2012-03-07.txt', 
    # 'CME_2012-01-22/WI_PM_3DP_CME_2012-01-22.txt', 

    # 'CME_2013-08-20/WI_PM_3DP_CME_2013-08-20.txt', 
    # 'CME_2013-05-24/WI_PM_3DP_CME_2013-05-24.txt', 
    # 'CME_2013-05-25/WI_PM_3DP_CME_2013-05-25.txt', 
    # 'CME_2013-05-31/WI_PM_3DP_CME_2013-05-31.txt', 
    # 'CME_2013-12-13/WI_PM_3DP_CME_2013-12-13.txt', 
    # 'CME_2013-10-02/WI_PM_3DP_CME_2013-10-02.txt', 
    # 'CME_2013-07-18/WI_PM_3DP_CME_2013-07-18.txt', 
    # 'CME_2013-07-12/WI_PM_3DP_CME_2013-07-12.txt', 
    # 'CME_2013-07-09/WI_PM_3DP_CME_2013-07-09.txt',
    # 'CME_2013-06-27/WI_PM_3DP_CME_2013-06-27.txt', 
    # 'CME_2013-04-13/WI_PM_3DP_CME_2013-04-13.txt', 
    # 'CME_2013-03-17/WI_PM_3DP_CME_2013-03-17.txt', 
    # 'CME_2013-02-16/WI_PM_3DP_CME_2013-02-16.txt', 

    # 'CME_2014-12-21/WI_PM_3DP_CME_2014-12-21.txt', 
    # 'CME_2014-12-23/WI_PM_3DP_CME_2014-12-23.txt', 
    # 'CME_2014-09-11/WI_PM_3DP_CME_2014-09-11.txt', 
    # 'CME_2014-09-12/WI_PM_3DP_CME_2014-09-12.txt',
    # 'CME_2014-07-02/WI_PM_3DP_CME_2014-07-02.txt', 
    # 'CME_2014-07-06/WI_PM_3DP_CME_2014-07-06.txt', 
    # 'CME_2014-02-20/WI_PM_3DP_CME_2014-02-20.txt', 
    # 'CME_2014-02-27/WI_PM_3DP_CME_2014-02-27.txt', 
    # 'CME_2014-01-07/WI_PM_3DP_CME_2014-01-07.txt', 
    # 'CME_2014-01-09/WI_PM_3DP_CME_2014-01-09.txt', 
    # 'CME_2014-06-23/WI_PM_3DP_CME_2014-06-23.txt', 
    # 'CME_2014-06-07/WI_PM_3DP_CME_2014-06-07.txt', 
    # 'CME_2014-03-25/WI_PM_3DP_CME_2014-03-25.txt', 
    # 'CME_2014-02-18/WI_PM_3DP_CME_2014-02-18.txt', 

    # 'CME1_2015-06-22/WI_PM_3DP_CME1_2015-06-22.txt', 
    # 'CME2_2015-06-22/WI_PM_3DP_CME2_2015-06-22.txt', 
    # 'CME_2015-03-17/WI_PM_3DP_CME_2015-03-17.txt', 
    # 'CME_2015-12-19/WI_PM_3DP_CME_2015-12-19.txt', 
    # 'CME_2015-11-04/WI_PM_3DP_CME_2015-11-04.txt', 
    # 'CME_2015-09-20/WI_PM_3DP_CME_2015-09-20.txt', 
    # 'CME_2015-08-15/WI_PM_3DP_CME_2015-08-15.txt', 
    # 'CME_2015-06-25/WI_PM_3DP_CME_2015-06-25.txt', 
    # 'CME_2015-06-24/WI_PM_3DP_CME_2015-06-24.txt', 
    # 'CME_2015-06-21/WI_PM_3DP_CME_2015-06-21.txt', 
    # 'CME_2015-05-06/WI_PM_3DP_CME_2015-05-06.txt', 

    # 'CME_2016-03-14/WI_PM_3DP_CME_2016-03-14.txt', 
    # 'CME_2016-01-18/WI_PM_3DP_CME_2016-01-18.txt', 
    # 'CME_2016-11-09/WI_PM_3DP_CME_2016-11-09.txt', 
    # 'CME_2016-10-12/WI_PM_3DP_CME_2016-10-12.txt', 
    # 'CME_2016-07-19/WI_PM_3DP_CME_2016-07-19.txt', 

    # 'CME_2017-10-24/WI_PM_3DP_CME_2017-10-24.txt', 
    # 'CME_2017-05-27/WI_PM_3DP_CME_2017-05-27.txt', 
    # 'CME_2017-07-08/WI_PM_3DP_CME_2017-07-08.txt'
    ]

st_ed_dt=[[datetime(2010, 2, 14, 17, 30 ),datetime(2010, 2, 16, 17, 30 )]

    # ,[datetime(2011, 8, 3, 21, 10 ),datetime(2011, 8, 5, 21, 10 )],
    # [datetime(2011, 8, 4, 17, 32 ),datetime(2011, 8, 6, 17, 32 )],
    # [datetime(2011, 11, 11, 5, 11, 45 ),datetime(2011, 11, 13, 5, 11, 45 )],
    # [datetime(2011, 11, 10, 3, 1, 27 ),datetime(2011, 11, 12, 3, 1, 27 )],
    # [datetime(2011, 9, 25, 11, 44, 18 ),datetime(2011, 9, 27, 11, 44, 18 )],
    # [datetime(2011, 9, 24, 10, 46, 33 ),datetime(2011, 9, 26, 10, 46, 33 )],
    # [datetime(2011, 7, 10, 8, 5 ),datetime(2011, 7, 12, 8, 5 )],
    # [datetime(2011, 6, 3, 19, 45 ),datetime(2011, 6, 5, 19, 45 )],
    # [datetime(2011, 4, 17, 5, 46, 11 ),datetime(2011, 4, 19, 5, 46, 11 )],
    # [datetime(2011, 2, 17, 0, 49, 3 ),datetime(2011, 2, 19, 0, 49, 3 )],
    # [datetime(2011, 2, 13, 15, 6, 45 ),datetime(2011, 2, 15, 15, 6, 45 )],

    # [datetime(2012, 11, 25, 4, 32, 51 ),datetime(2012, 11, 27, 4, 32, 51 )],
    # [datetime(2012, 11, 22, 20, 51, 21 ),datetime(2012, 11, 24, 20, 51, 21 )],
    # [datetime(2012, 11, 11, 22, 12, 42 ),datetime(2012, 11, 13, 22, 12, 42 )],
    # [datetime(2012, 10, 30, 16, 9, 15 ),datetime(2012, 11, 1, 16, 9, 15 )],
    # [datetime(2012, 10, 7, 4, 12, 15 ),datetime(2012, 10, 9, 4, 12, 15 )],
    # [datetime(2012, 9, 29, 22, 18, 36 ),datetime(2012, 10, 1, 22, 18, 36 )],
    # [datetime(2012, 9, 3, 22, 2, 36 ),datetime(2012, 9, 5, 22, 2, 36 )],
    # [datetime(2012, 9, 2, 11, 21, 51 ),datetime(2012, 9, 4, 11, 21, 51 )],
    # [datetime(2012, 7, 13, 17, 46, 39 ),datetime(2012, 7, 15, 17, 46, 39 )],
    # [datetime(2012, 6, 15, 19, 34, 39 ),datetime(2012, 6, 17, 19, 34, 39 )],
    # [datetime(2012, 5, 20, 18, 53 ),datetime(2012, 5, 22, 18, 53 )],
    # [datetime(2012, 4, 22, 2, 30 ),datetime(2012, 4, 24, 2, 30 )],
    # [datetime(2012, 3, 6, 3, 28, 42 ),datetime(2012, 3, 8, 3, 28, 42 )],
    # [datetime(2012, 1, 21, 5, 32, 54 ),datetime(2012, 1, 23, 5, 32, 54 )],

    # [datetime(2013, 8, 19, 21, 43 ),datetime(2013, 8, 21, 21, 43 )],
    # [datetime(2013, 5, 23, 17, 40 ),datetime(2013, 5, 25, 17, 40 )],
    # [datetime(2013, 5, 24, 9, 6 ),datetime(2013, 5, 26, 9, 6 )],
    # [datetime(2013, 5, 30, 15, 32 ),datetime(2013, 6, 1, 15, 32 )],
    # [datetime(2013, 12, 12, 12, 1 ),datetime(2013, 12, 14, 12, 1 )],
    # [datetime(2013, 10, 1, 1, 15, 51 ),datetime(2013, 10, 3, 1, 15, 51 )],
    # [datetime(2013, 7, 17, 12, 55, 42 ),datetime(2013, 7, 19, 12, 55, 42 )],
    # [datetime(2013, 7, 11, 16, 43, 27 ),datetime(2013, 7, 13, 16, 43, 27 )],
    # [datetime(2013, 7, 8, 20, 11, 39 ),datetime(2013, 7, 10, 20, 11, 39 )],
    # [datetime(2013, 6, 26, 13, 51, 18 ),datetime(2013, 6, 28, 13, 51, 18 )],
    # [datetime(2013, 4, 12, 22, 24 ),datetime(2013, 4, 14, 22, 24 )],
    # [datetime(2013, 3, 16, 5, 22 ),datetime(2013, 3, 18, 5, 22 )],
    # [datetime(2013, 2, 15, 11, 13 ),datetime(2013, 2, 17, 11, 13 )],

    # [datetime(2014, 12, 20, 18, 22 ),datetime(2014, 12, 22, 18, 22 )],
    # [datetime(2014, 12, 22, 10, 30 ),datetime(2014, 12, 24, 10, 30 )],
    # [datetime(2014, 9, 10, 23, 2 ),datetime(2014, 9, 12, 23, 2 )],
    # [datetime(2014, 9, 11, 15, 27 ),datetime(2014, 9, 13, 15, 27 )],
    # [datetime(2014, 7, 1, 23, 33 ),datetime(2014, 7, 3, 23, 33 )],
    # [datetime(2014, 7, 5, 9, 51 ),datetime(2014, 7, 7, 9, 51 )],
    # [datetime(2014, 2, 19, 2, 58 ),datetime(2014, 2, 21, 2, 58 )],
    # [datetime(2014, 2, 26, 16, 17 ),datetime(2014, 2, 28, 16, 17 )],
    # [datetime(2014, 1, 6, 14, 24 ),datetime(2014, 1, 8, 14, 24 )],
    # [datetime(2014, 1, 8, 19, 33 ),datetime(2014, 1, 10, 19, 33 )],
    # [datetime(2014, 6, 22, 22, 15, 57 ),datetime(2014, 6, 24, 22, 15, 57 )],
    # [datetime(2014, 6, 6, 15, 57 ),datetime(2014, 6, 8, 15, 57 )],
    # [datetime(2014, 3, 24, 19, 24 ),datetime(2014, 3, 26, 19, 24 )],
    # [datetime(2014, 2, 17, 6, 6, 21 ),datetime(2014, 2, 19, 6, 6, 21 )],

    # [datetime(2015, 6, 21, 4, 52 ),datetime(2015, 6, 23, 4, 52 )],
    # [datetime(2015, 6, 21, 18, 1 ),datetime(2015, 6, 23, 18, 1 )],
    # [datetime(2015, 3, 16, 4, 11 ),datetime(2015, 3, 18, 4, 11 )],
    # [datetime(2015, 12, 18, 15, 38, 24 ),datetime(2015, 12, 20, 15, 38, 24 )],
    # [datetime(2015, 11, 3, 3, 26, 6 ),datetime(2015, 11, 5, 3, 26, 6 )],
    # [datetime(2015, 9, 19, 5, 33 ),datetime(2015, 9, 21, 5, 33 )],
    # [datetime(2015, 8, 14, 7, 50 ),datetime(2015, 8, 16, 7, 50 )],
    # [datetime(2015, 6, 24, 5, 2, 39 ),datetime(2015, 6, 26, 5, 2, 39 )],
    # [datetime(2015, 6, 23, 13, 7, 15 ),datetime(2015, 6, 25, 13, 7, 15 )],
    # [datetime(2015, 6, 20, 15, 50 ),datetime(2015, 6, 22, 15, 50 )],
    # [datetime(2015, 5, 5, 0, 50 ),datetime(2015, 5, 7, 0, 50 )],

    # [datetime(2016, 3, 13, 16, 16, 33 ),datetime(2016, 3, 15, 16, 16, 33 )],
    # [datetime(2016, 1, 17, 21, 20, 48 ),datetime(2016, 1, 19, 21, 20, 48 )],
    # [datetime(2016, 11, 8, 5, 28 ),datetime(2016, 11, 10, 5, 28 )],
    # [datetime(2016, 10, 11, 21, 26 ),datetime(2016, 10, 13, 21, 26 )],
    # [datetime(2016, 7, 18, 23, 9 ),datetime(2016, 7, 20, 23, 9 )],

    # [datetime(2017, 10, 23, 8, 57, 30 ),datetime(2017, 10, 25, 8, 57, 30 )],
    # [datetime(2017, 5, 26, 14, 27 ),datetime(2017, 5, 28, 14, 27 )],
    # [datetime(2017, 7, 7, 23, 27 ),datetime(2017, 7, 9, 23, 27 )]
]

print(len(st_ed_dt),len(file_name))
def formatdt(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S.')+("%0.3f"%(dt.microsecond/10**6))[2:]

for ind, item in enumerate(file_name):
    # data = cdas.get_data(
    # 'sp_phys',
    # 'WI_H0_MFI',
    # st_ed_dt[ind][0],
    # st_ed_dt[ind][1],
    # ['B3F1','B3GSE']) #B, BX_(GSE), BY_(GSE), BZ_(GSE)
    data = cdas.get_data(
        'sp_phys',
        'WI_PM_3DP',
        st_ed_dt[ind][0],
        st_ed_dt[ind][1],
        ['P_DENS', 'P_VELS']) #DENS_PROTN_S/C VXGSE_PROTN_S/C, VYGSE_PROTN_S/C,VZGSE_PROTN_S/C
        #['Proton_Np_moment', 'Proton_VX_moment', 'Proton_VY_moment', 'Proton_VZ_moment'])
    dt=[]
    for i in data['EPOCH']:
        dt.append(formatdt(i))
    np.savetxt('/Users/Taninka/Documents/skola_PhD/CASE_STUDY/48hours_IP_shocks/'+str(item), np.transpose([dt,data['DENS_PROTN_S/C'],data['VXGSE_PROTN_S/C'],data['VYGSE_PROTN_S/C'],data['VZGSE_PROTN_S/C']]),fmt='%s, %s, %s, %s, %s')

#plt.plot(data['EPOCH'], data['P+_VX_MOMENT'])
#plt.show()
print('FINISHED')


