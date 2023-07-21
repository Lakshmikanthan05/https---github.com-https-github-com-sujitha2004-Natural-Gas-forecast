print(df.shape)

print(df.head())

df[['Price']].plot(title='crude oil price')
plt.show()