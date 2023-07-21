import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("C:\\Users\\91996\\webpage project\\project 4.1`\\dataset\\crude_oil_price.csv")
df
df.set_index('Date').plot()
plt.show()