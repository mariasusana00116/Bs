# -*- coding: utf-8 -*-
"""

@author: HP
"""
##############################################
#################EXAMEN FINAL#################
##############################################


pip install yfinance

import yfinance as yf
import pandas as pd
import numpy as np


##################################################################################
##################################################################################
##################################################################################

####WFC####
WFC_df=yf.download('WFC', start='2019-01-01',end='2019-12-31')
rend_WFC=pd.DataFrame(WFC_df['Adj Close'].pct_change())
rend_WFC.columns=['WFC']
rend_WFC.describe()
WFC_df.describe()


####JPM####
JPM_df=yf.download('JPM', start='2019-01-01',end='2019-12-31')
rend_JPM=pd.DataFrame(JPM_df['Adj Close'].pct_change())
rend_JPM.columns=['JPM']
rend_JPM.describe()
JPM_df.describe()


####GS####
GS_df=yf.download('GS', start='2019-01-01',end='2019-12-31')
rend_GS=pd.DataFrame(GS_df['Adj Close'].pct_change())
rend_GS.columns=['GS']
rend_GS.describe()
GS_df.describe()


data=pd.concat([rend_WFC,rend_JPM,rend_GS],axis=1)
data.corr()
data.describe()

import matplotlib.pyplot as plt
ticker=yf.Ticker('WFC')
WFC_df=ticker.history(period='max')
WFC_df['Close'].plot(title='Evolución del precio de WFC')
plt.show()

import matplotlib.pyplot as plt
ticker=yf.Ticker('JPM')
JPM_df=ticker.history(period='max')
JPM_df['Close'].plot(title='Evolución del precio de JPM')
plt.show()

import matplotlib.pyplot as plt
ticker=yf.Ticker('GS')
GS_df=ticker.history(period='max')
GS_df['Close'].plot(title='Evolución del precio de GS')
plt.show()


pip install pandas-datareader
import pandas_datareader.data as web
import pandas as pd
import datetime


pd.core.common.is_list_like=pd.api.types.is_list_like
start=datetime.datetime(2019,1,1)
end=datetime.datetime(2019,12,31)
rend_sp=web.DataReader(['sp500'],'fred',start,end).pct_change()
rend_sp.describe()
data2=pd.concat([data,rend_sp],axis=1)

#Sharpe ratio
np.mean(data2.WFC)/np.std(data2.WFC)
np.mean(data2.JPM)/np.std(data2.JPM)
np.mean(data2.GS)/np.std(data2.GS)

# VaR ==> Value at Risk ---- 99%
np.nanpercentile(data2.WFC,1)
np.nanpercentile(data2.JPM,1)
np.nanpercentile(data2.GS,1)

# cVaR ==> Pérdida promedio del VaR
data2[data2.WFC<=np.nanpercentile(data2.WFC,1)]['WFC'].mean()
data2[data2.JPM<=np.nanpercentile(data2.JPM,1)]['JPM'].mean()
data2[data2.GS<=np.nanpercentile(data2.GS,1)]['GS'].mean()

##################################################################################
##################################################################################
##################################################################################

import pandas_datareader as pdr
import numpy as np
import pandas as pd
import yfinance as yf
from statsmodels.formula.api import ols

f3=pdr.DataReader('F-F_Research_Data_Factors','famafrench')
data_f3=pd.DataFrame(f3[0])

####WFC####
df=yf.download('WFC',start='2019-01-01',end='2019-12-28')
wfc=df[['Adj Close']]
wfc.rename(columns={'Adj Close':'precio'},inplace=True)
wfc['rend']=wfc.precio.pct_change()
wfc2=wfc.resample('M').last()


wfc2.reset_index(drop=False,inplace=True)
data_f3.reset_index(drop=False,inplace=True)

data_multi=pd.concat([wfc2,data_f3],axis=1)
data_multi.columns=['date1','precio','rend','date2','prima','smb','hml','rf']


from statsmodels.formula.api import ols
modelo=ols(formula='rend~rf+prima',data=data_multi)
resultados=modelo.fit()
resultados.summary()

modelo=ols(formula='rend~rf+prima+smb+hml',data=data_multi)
resultados=modelo.fit()
resultados.summary()

