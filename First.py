import matplotlib.pyplot as plt
import pandas
df=pandas.read_csv('Hurricanes.csv',delimiter=',')
print(df)
plt.bar(df['Year'],df['Hurricanes'])
plt.show()
