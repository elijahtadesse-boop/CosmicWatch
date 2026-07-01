import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('daten/SDS00008.CSV', sep=',')


# Set custom column names for the DataFrame.
# These names are used to access the respective columns easily (e.g., 'x', 'y', 'xerr', 'yerr').
# Adjust the column names according to the actual data structure of your file.
data.columns = ['timems', 'CH1', 'CH2']
timems=data["timems"]
CH1=data["CH1"]
CH2=data["CH2"]
time_s = data["timems"] / 1000
print(max(CH1))
print(min(CH1))
print(max(CH2))
print(min(CH2))
fig, ax = plt.subplots(figsize=(8, 6))
#ax.set_ylim(0,2)
#ax.scatter(, adcSorted)

ax.scatter(timems,CH1, label="CH1", s=5)
ax.scatter(timems, CH2, label="CH2", s=5)
#plt.hlines(0.707, xmin=0, xmax=9000, colors='black', linestyles='--')
#plt.hlines(4.24, xmin=-0.000015, xmax=0.000015, colors='black', linestyles='--')
#plt.hlines(6.16, xmin=-0.000015, xmax=0.000015, colors='black', linestyles='--')
#plt.hlines(2.32, xmin=-0.000015, xmax=0.000015, colors='black', linestyles='--')

#ax.set_ylim(-8,8)
ax.set_xlabel("Zeit t/ms")
ax.set_ylabel("Spannung U/V")
ax.legend()
plt.grid(True)
#plt.savefig("verstärker.png") #zuerst save dann show
plt.show()

