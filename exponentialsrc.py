
import pandas as pd

from matplotlib import pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.seasonal import seasonal_decompose 

from statsmodels.tsa.holtwinters import SimpleExpSmoothing   

from statsmodels.tsa.holtwinters import ExponentialSmoothing
df=pd.read_csv("C:\\Users\\91996\\webpage project\\project 4.1`\\dataset\\crude_oil_price.csv",index_col='Date')
print(df.shape)

print(df.head())



df.index = pd.DatetimeIndex(df.index).to_period('M')
train_airline = df[:350]
test_airline = df[350:]
fitted_model = ExponentialSmoothing(train_airline['Price'],trend='mul',seasonal='add',seasonal_periods=12).fit()
test_predictions = fitted_model.forecast()

test_airline['Price'].plot(legend=True,label='TEST',figsize=(6,4))
test_predictions.plot(legend=True,label='PREDICTION')
plt.show()