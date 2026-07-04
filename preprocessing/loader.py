import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn import tree

import sys
import __init__
import numpy as np
from numpy import var, arange
import pandas as pd
from datetime import datetime
import time
import scipy.stats as stats
import statsmodels.api as sm
from matplotlib import pyplot as plt
from scipy import linalg, signal
lowess = sm.nonparametric.lowess
#fp = open('C:\\Users\\91987\\Desktop\\results_stops\\.csv','a')

def lowess(x, y, f=2./3., iter=3):
    """lowess(x, y, f=2./3., iter=3) -> yest

    Lowess smoother: Robust locally weighted regression.
    The lowess function fits a nonparametric regression curve to a scatterplot.
    The arrays x and y contain an equal number of elements; each pair
    (x[i], y[i]) defines a data point in the scatterplot. The function returns
    the estimated (smooth) values of y.

    The smoothing span is given by f. A larger value for f will result in a
    smoother curve. The number of robustifying iterations is given by iter. The
    function will run faster with a smaller number of iterations."""
    n = len(x)
    r = int(np.ceil(f*n))
    h = [np.sort(np.abs(x - x[i]))[r] for i in range(n)]
    w = np.clip(np.abs((x[:,None] - x[None,:]) / h), 0.0, 1.0)
    w = (1 - w**3)**3
    yest = np.zeros(n)
    delta = np.ones(n)
    for iteration in range(iter):
        for i in range(n):
            weights = delta * w[:,i]
            b = np.array([np.sum(weights*y), np.sum(weights*y*x)])
            A = np.array([[np.sum(weights), np.sum(weights*x)],
                   [np.sum(weights*x), np.sum(weights*x*x)]])
            beta = linalg.solve(A, b)
            yest[i] = beta[0] + beta[1]*x[i]

        residuals = y - yest
        s = np.median(np.abs(residuals))
        delta = np.clip(residuals / (6.0 * s), -1, 1)
        delta = (1 - delta**2)**2

    return yest

def preprocessor(sensor):
    x = np.linspace(0,len(sensor),len(sensor))
    b,a = signal.butter(1,0.2)
    bs = signal.filtfilt(b,a,sensor)
    f = 0.2
    return lowess(x,bs,f,3)

def preprocessor1(sensor):
    x = np.linspace(0,len(sensor),len(sensor))
    b,a = signal.butter(1,0.1)
    bs = signal.filtfilt(b,a,sensor)
    f = 0.2
    return lowess(x,bs,f,3)

#################################### methods to convert UTM to GPS coordinates #######################

import utm
utm.from_latlon(50.78505, 6.1307)
# 297631.3187	5629917.34465
utm.to_latlon(297750.4242122149, 5629847.200807358, 32, 'U')


import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# Load the vehicle trajectory data from inD dataset
data = pd.read_csv('D:\\inD-dataset-v1.0\\data\\07_tracks.csv',header=0,sep=",")
df = pd.DataFrame(data, columns = data.columns)

meta_data = pd.read_csv('D:\\inD-dataset-v1.0\\data\\07_recordingMeta.csv',header=0,sep=",")
df1 = pd.DataFrame(meta_data, columns = meta_data.columns)
df.shape
df1.columns

df['xCenter'] += df1['xUtmOrigin'][0]
df['yCenter'] += df1['yUtmOrigin'][0]

utmx = df['xCenter'].tolist()
utmy = df['yCenter'].tolist()

lat = []
long = []

for i in range(len(utmx)):
    print(utm.to_latlon(utmx[i], utmy[i], 32, 'U')[0],utm.to_latlon(utmx[i], utmy[i], 32, 'U')[1])
    lat.append(utm.to_latlon(utmx[i], utmy[i], 32, 'U')[0])
    long.append(utm.to_latlon(utmx[i], utmy[i], 32, 'U')[1])

df['latitude'] = lat
df['longitude'] = long

df.to_csv("00_tracks_mod.csv")


