import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
df=pd.read_csv("Test_2007_2017_Buffer_4_10.0_2.0_35.0_result.csv")
df["date_time"]=pd.to_datetime(df.date_time.values,format='%Y-%m-%d')
indexes=df.sort_values(by="magn1",ascending=False)
indexes=indexes.iloc[0:3]
#Region de estudio Constitucion
ymin=-38.5
ymax=-34
xmin=-80
xmax=-67
month_min=1
month_max=6
year_min=2010
year_max=2010


#Region de estudio Iquique
ymin=-21
ymax=-19
xmin=-71.5
xmax=-69.8
month_min=3
month_max=6
year_min=2014
year_max=2014


#Region de estudio Coquimbo

ymin=-32
ymax=-30
xmin=-73
xmax=-71
month_min=9
month_max=12
year_min=2015
year_max=2015




print(len(df))
df=df[df["year"]>=year_min]
df=df[df["year"]<=year_max]
df=df[df["month"]>=month_min]
df=df[df["month"]<=month_max]

df=df[df["lat"]>=ymin]
df=df[df["lat"]<=ymax]
df=df[df["long"]>=xmin]
df=df[df["long"]<=ymax]
#df=df[df["cluster"]!=-1]

noise=df[df["cluster"]==-1]
print(len(noise))
clusters=list(set(df.cluster.values))

dates=list(set(df["date_time"].values))
plt.figure(figsize=(10,10), dpi=150)
plt.title("")
plt.xlabel("Time")
plt.ylabel("N° Seismic events per day")
distinc_by_day={}  
for date in dates:
    count=df[df["date_time"]==date]
    distinc_by_day[date]=len(count)
   
    

plt.bar(distinc_by_day.keys(),distinc_by_day.values(),color="black")
for cluster in clusters:
    aux=df[df["cluster"]==cluster]
    dates=list(set(aux["date_time"].values))
    dicc={}
    for date in dates:
        count=aux[aux["date_time"]==date]
        dicc[date]=len(count)
    c = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]

    plt.bar(dicc.keys(),dicc.values(),color=c)
    

list_days=distinc_by_day.keys()
list_days=sorted(list_days)






'''

ymin=-32
ymax=-30
xmin=-73
xmax=-71
  
df=df[df["year"]==2015]
df=df[df["month"]>=9]
df=df[df["month"]<=11]

df=df[df["lat"]>=ymin]
df=df[df["lat"]<=ymax]
df=df[df["long"]>=xmin]
df=df[df["long"]<=ymax]


distinc_by_day={}

dates=list(set(df["date_time"].values))

for date in dates:
    count=df[df["date_time"]==date]
    distinc_by_day[date]=len(count)




iquique={}
df_iquique=df[df["cluster"]==390]
dates=list(set(df_iquique["date_time"].values))

for date in dates:
    count=df_iquique[df_iquique["date_time"]==date]
    iquique[date]=len(count)


coquimbo={}
df_coquimbo=df[df["cluster"]==324]
rest=df[df["cluster"]!=324]
df_coquimbo=df_coquimbo[df_coquimbo["month"]>=9]
df_coquimbo=df_coquimbo[df_coquimbo["month"]>=11]

dates=list(set(df_coquimbo["date_time"].values))

for date in dates:
    count=df_coquimbo[df_coquimbo["date_time"]==date]
    coquimbo[date]=len(count)

plt.bar(distinc_by_day.keys(),distinc_by_day.values(),color="b")
plt.bar(iquique.keys(),iquique.values(),color="r")

#plt.bar(coquimbo.keys(),coquimbo.values(),color="g")
'''