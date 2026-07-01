import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('daten/datalog_29.06.txt', sep=r'\s+')
#data1 = pd.read_csv('daten/thres20_24.6..txt', sep=r'\s+')

# Set custom column names for the DataFrame.
# These names are used to access the respective columns easily (e.g., 'x', 'y', 'xerr', 'yerr').
# Adjust the column names according to the actual data structure of your file.
data.columns = ['evNum', 'timeMs', 'adc', 'rateAverage']
evNum=data["evNum"]
timeMs=data["timeMs"]
adc=data["adc"]
rateAverage=data["rateAverage"]
#time = timeMs/1000
#rate = []
#for i in range(len(time)-1):
 #   t = time[i+1]-time[i]
  #  r = 1/t
   # rate.append(r)
#rate.append(0)
time_s = data["timeMs"] / 1000
dt = time_s.diff()
rate = 1 / dt
rate.iloc[0] = 0

data["bin"] = (time_s // 60).astype(int)
data["rate"] = rate
mittel_rate = data.groupby("bin")["rate"].mean()
print(data["rate"].max())
print(mittel_rate)
fig, ax = plt.subplots(figsize=(8, 6))
#ax.set_ylim(0,2)
counts = data["adc"].value_counts().reset_index()
counts.columns = ["adcSorted", "anzahl"]
adcSorted = counts["adcSorted"]
anzahl = counts["anzahl"]
#print(adcSorted)
#ax.scatter(anzahl, adcSorted)
#ax.hist(data["adc"], bins=100, color="royalblue", edgecolor="black", log=True)
# Filtert alle Werte unter 100 einfach heraus
nur_hohe_signale = data[data["adc"] > 30]

# Neues Histogramm nur mit den hohen Signalen plottem

#ax.hist(nur_hohe_signale["adc"], bins=100, color="blue", edgecolor="black", log=False, density=True)
ax.hist(data["adc"], bins=100, color="crimson", edgecolor="black", log=False, density=True)
#plt.savefig("ohne")
plt.show()

