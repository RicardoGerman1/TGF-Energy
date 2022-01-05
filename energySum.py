import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# get only the columns you want from the csv file
df = pd.read_csv('/Users/13125/Documents/Physics Research/xu_1e6/testFileDF.csv', 
                 usecols=['energy(MeV)', 'y(mm)','z(mm)'])

# y and z columns are conditioned to parameters, if true, sum energy values
df['total1'] = df.loc[(df['y(mm)'] >= 56000.0) & (df['z(mm)'] >= 189000.0)
                      & (df['y(mm)'] <= 57000.0) & (df['z(mm)'] <= 190000.0), 'energy(MeV)'].sum()

df['total2'] = df.loc[(df['y(mm)'] >= 85000.0) & (df['z(mm)'] >= 193000.0)
                      & (df['y(mm)'] <= 90000.0) & (df['z(mm)'] <= 194000.0), 'energy(MeV)'].sum()

df['total3'] = df.loc[(df['y(mm)'] >= 153000.0) & (df['z(mm)'] >= 158000.0)
                     & (df['y(mm)'] <= 154000.0) & (df['z(mm)'] <= 159000.0), 'energy(MeV)'].sum()

df['total4'] = df.loc[(df['y(mm)'] >= -71000.0) & (df['z(mm)'] >= -380000.0)
                     & (df['y(mm)'] <= -70000.0) & (df['z(mm)'] <= -360000.0), 'energy(MeV)'].sum()

df['total5'] = df.loc[(df['y(mm)'] >= -370000.0) & (df['z(mm)'] >= -322000.0)
                     & (df['y(mm)'] <= -369000.0) & (df['z(mm)'] <= -321000.0), 'energy(MeV)'].sum()

df['total6'] = df.loc[(df['y(mm)'] >= 777000.0) & (df['z(mm)'] >= -135000.0)
                     & (df['y(mm)'] <= 778000.0) & (df['z(mm)'] <= -134000.0), 'energy(MeV)'].sum()

df['total7'] = df.loc[(df['y(mm)'] >= 51000.0) & (df['z(mm)'] >= -99900.0)
                     & (df['y(mm)'] <= 52000.0) & (df['z(mm)'] <= -99600.0), 'energy(MeV)'].sum()

df['total8'] = df.loc[(df['y(mm)'] >= 325000.0) & (df['z(mm)'] >= 478000.0)
                     & (df['y(mm)'] <= 330000.0) & (df['z(mm)'] <= 480000.0), 'energy(MeV)'].sum()


# Get the average of position hits, divided by # lines
totalY = df['y(mm)'].sum()
totalZ = df['z(mm)'].sum()

avgY = totalY / 889 
avgZ = totalZ / 889


# Convert the sum totals to a numpy list (numpy has more tools and it's faster)
sum1 = df['total1'].to_numpy()
sum2 = df['total2'].to_numpy()
sum3 = df['total3'].to_numpy()
sum4 = df['total4'].to_numpy()
sum5 = df['total5'].to_numpy()
sum6 = df['total6'].to_numpy()
sum7 = df['total7'].to_numpy()
sum8 = df['total8'].to_numpy()
# Slice the numpy list so only 1 value returns
e1 = sum1[:1]
e2 = sum2[:1]
e3 = sum3[:1]
e4 = sum4[:1]
e5 = sum5[:1]
e6 = sum6[:1]
e7 = sum7[:1]
e8 = sum8[:1]
# Join the energy values into a list
eMeV = np.concatenate((e2, e1, e3, e4, e5, e8, e7, e6))

# set up our detectors with xaxis and yaxis along with the corresponding energy sum
yaxis = [2000, 4000,-2000, 0, -2000, 0, 2000, 4000]
zaxis = [2000, 2000, 2000, 2000, 0, 0, 0, 0]
# eMeV = [e1, e2]

# Plot/Create a second dataframe using x,y, and energy values.
min_=0.0
max_=3.0

#plt.scatter(avgY, avgZ, marker="x", c='red') #The red cross marks the mean as calculated from the hits in the detectors.
df2 = pd.DataFrame(dict(yaxis=yaxis, zaxis=zaxis, eMeV=eMeV))
df2.plot.scatter('yaxis', 'zaxis', s=400, c= 'eMeV', cmap ='viridis')
plt.xlim(-5000, 5000)
plt.ylim(-5000, 5000)
plt.clim(min_, max_)
plt.show()

#print(df['total1'])
#print(df['total2'])
#df.info()

