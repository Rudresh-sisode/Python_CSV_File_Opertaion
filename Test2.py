import matplotlib.pyplot as plt
import pandas
df=pandas.read_csv('BigMartSalesData.csv',delimiter=',')

print(df.iloc[3:345,4])
