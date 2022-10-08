import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdate
import pandas as pd

#绘制y = （x+1）²的图像
f=lambda x:x**2+2*x+1
x=np.linspace(-5,5,1000)
plt.plot(x,f(x),'b-',)
plt.ylim(0,40)
plt.xticks(range(-5,6))
plt.title('Y=(x+1)²')
plt.show()

#用pandas处理并绘图
csv=pd.read_csv(r'C:\Users\lenovo\Desktop\文件\程序设计基础\实验二\co2-mm-mlo.csv',engine='python')
csv['Date']=pd.to_datetime(csv.Date,format="%Y/%m/%d")
csv.plot(x='Date',y=['Trend','Interpolated'])
plt.show()

#用pandas处理并绘图
json=pd.read_json(r'C:\Users\lenovo\Desktop\文件\程序设计基础\实验二\co2-mm-gl.json')
json.plot(x='Date',y=['Trend','Average'])
plt.show()





