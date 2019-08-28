import matplotlib.pyplot as plt
import pandas
df=pandas.read_csv('CityTemps.csv',delimiter=',')
plt.hist(df['Melbourne'],df['San Francisco'])
plt.show()
