from pmdarima import auto_arima
import warnings
import pandas as pd
warnings.filterwarnings("ignore")

df=pd.read_csv("C:\\Users\\91996\\webpage project\\project 4.1`\\dataset\\crude_oil_price.csv")
stepwise_fit= auto_arima(df['Price'],trace=True,suppress_warnings=True)
stepwise_fit.summary()
