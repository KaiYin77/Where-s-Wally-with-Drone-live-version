import csv
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('error_6.csv', header=None)

#print(df.columns)
error_1 = []
error_2 = []
error_3 = []
error_4 = []
#print(df)
for column in df.iterrows():
    
    error_1.append(column[1][0])
    error_2.append(column[1][1])
    error_3.append(column[1][2])
    error_4.append(column[1][3])

fig, axs = plt.subplots(2,2)
axs[0, 0].plot(error_1)
axs[0, 0].set_title('error_1')
axs[0, 1].plot(error_2)
axs[0, 1].set_title('error_2')
axs[1, 0].plot(error_3)
axs[1, 0].set_title('error_3')
axs[1, 1].plot(error_4)
axs[1, 1].set_title('error_4')

plt.show()
