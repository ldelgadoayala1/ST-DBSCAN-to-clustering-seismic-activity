
#Proyecto de Tesis - Luis Delgado Ayala
#Instalar librerias a utilizar



#Librerias
import pandas as pd
from pyproj import CRS
import geopandas
import matplotlib.pyplot as plt
import shapefile
import numpy as np

import shapely.geometry
import rtree

import datetime
import math
from mpl_toolkits.mplot3d import axes3d
import warnings

from math import exp, expm1
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, whiten
from sklearn.cluster import KMeans
from sklearn import metrics
import networkx as nx
from geopy.distance import lonlat, distance

from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
warnings.filterwarnings('ignore')

def K_means_clustering(serie,n_clusters):

  coords=serie[['lat','long']]


  
  kmeans = KMeans(n_clusters=n_clusters, random_state=0,algorithm="full").fit(coords)
  clusters_labels=kmeans.labels_

  clusters= kmeans.predict(np.radians(coords))
  num_clusters = len(set(clusters_labels))
  df_values=serie.values




  output=[]
  lat=df_values[:,7]
  lon=df_values[:,8]


  cl=clusters_labels
  time=serie[["time"]]
  time=time.astype(int)
  time=(list(time.time))
  dia=serie.day
  dia=dia.astype(int)
  dia=(list(dia))
  
  mes=serie.month
  mes=mes.astype(int)
  mes=(list(mes))
  anio=serie.year
  anio=anio.astype(int)
  anio=(list(anio))
  magn1=(list(serie.magn1))
  #time=pd.DataFrame(time)
  
 
  for i in range(len(clusters_labels)):
    aux=[]
    aux.append(lat[i])
    aux.append(lon[i])
    aux.append(dia[i])
    aux.append(mes[i])
    aux.append(anio[i])
    aux.append(time[i])
    aux.append(magn1[i])
    aux.append(cl[i])
    
    output.append(aux)
    
  df_out=pd.DataFrame(output,columns=["lon","lat","day","month","year","time","magn1","K-Means"])

  return df_out
  
#====================================================================================================================
def dbscan_clustering(serie,epsilon,mn):

  coords=serie[['lat','long']]



  kms_per_radian = epsilon/6371.0088

  dbscan = DBSCAN(eps=kms_per_radian,min_samples=mn,algorithm='ball_tree',metric='haversine').fit(coords)

                
  clusters= dbscan.fit(np.radians(coords))

  clusters_labels=dbscan.labels_
  clusters=dbscan.fit_predict(np.radians(coords))
  num_clusters = len(set(clusters_labels))
  df_values=serie.values




  output=[]
  lat=df_values[:,7]
  lon=df_values[:,8]


  cl=clusters_labels
  time=serie[["time"]]
  time=time.astype(int)
  time=(list(time.time))
  dia=serie.day
  dia=dia.astype(int)
  dia=(list(dia))

  mes=serie.month
  mes=mes.astype(int)
  mes=(list(mes))
  anio=serie.year
  anio=anio.astype(int)
  anio=(list(anio))
  magn1=(list(serie.magn1))
  #time=pd.DataFrame(time)


  for i in range(len(clusters_labels)):
    aux=[]
    aux.append(lat[i])
    aux.append(lon[i])
    aux.append(dia[i])
    aux.append(mes[i])
    aux.append(anio[i])
    aux.append(time[i])
    aux.append(magn1[i])
    aux.append(cl[i])
    aux.append(mn)
    aux.append(epsilon)
    output.append(aux)
    
  df_out=pd.DataFrame(output,columns=["lon","lat","day","month","year","time","magn1","DBSCAN","MN_DBSCAN","EPSILON_DBSCAN"])

  return df_out

name="Test_2007_2017_Buffer_4_10.0_3.0_45.0"
df=pd.read_csv(name+".csv")
df=pd.DataFrame(df)


DBSCAN=dbscan_clustering(df,20,4)

n_clusters=len(list(set(DBSCAN.DBSCAN.values)))
K_MEANS=K_means_clustering(df,n_clusters)

DBSCAN_column=DBSCAN["DBSCAN"].values
K_MEANS_column=K_MEANS["K-Means"].values
df_out=df
df_out["DBSCAN"]=DBSCAN_column
df_out["K-Means"]=K_MEANS_column
print(df[["date_time","cluster","DBSCAN","K-Means"]])
df_out.to_csv(name+"_result.csv")