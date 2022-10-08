import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdate
import time
import pandas as pd

csv=pd.read_csv(r'C:\Users\lenovo\Desktop\文件\程序设计基础\co2-mm-mlo.csv',engine='python')
for i in range(csv.shape[1]):
    csv['Date'].iloc[i]=pd.datetime.strptime(csv['Date'].iloc[i],'%Y-%m-%d')
