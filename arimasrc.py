from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import warnings
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
df=pd.read_csv("C:\\Users\\91996\\webpage project\\project 4.1`\\dataset\\crude_oil_price.csv",index_col=['Date'])
train=df.iloc[-200:-100]
test=df.iloc[-100:]
model=ARIMA(train['Price'],order=(2,1,1))
model=model.fit()
start=len(train)
end=len(train)+len(test)-1
pred=model.predict(start=start,end=end,typ='levels')
pred.index=df.index[start:end+1]
pred.plot(legend=True)
test['Price'].plot(legend=True)
plt.show()




