from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np

def ad_test(dataset):
    dftest=adfuller(dataset,autolag='AIC')
    print("1. ADF : ",dftest[0])
    print("2. P-Value : ",dftest[1])
    print("3. num of lags :",dftest[2])
    print("4. num of observation used for ADF regression and critical values calculation :",dftest[3])
    print("5. critical values :")
    for key, val in dftest[4].items():
        print("\t",key,": ",val)

df=pd.read_csv("C:\\Users\\91996\\webpage project\\project 4.1`\\dataset\\crude_oil_price.csv")
ad_test(df['Price'])