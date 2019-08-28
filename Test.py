import matplotlib.pyplot as plt
import pandas
df=pandas.read_csv('BigMartSalesData.csv',delimiter=',')
print(df)

plt.plot(df['Year'],df['Quantity'])
plt.show()
