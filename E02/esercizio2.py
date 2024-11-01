import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pianeti = pd.read_csv('ExoplanetsPars_2024.csv',delimiter=',',comment='#', usecols=['pl_orbper', 'pl_bmassj', 'pl_orbsmax','st_mass','discoverymethod' ])
print(pianeti)
print(pianeti.columns)

print(pianeti.iloc[5:8])

plt.scatter(pianeti['pl_orbper'] , pianeti['pl_bmassj'], color='royalblue', s=32)
plt.xlabel('periodo', fontsize=16)
plt.ylabel('massa', fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.show()

aly=pianeti['pl_orbsmax']/pianeti['st_mass']

plt.scatter(pianeti['pl_orbper'] , aly, color='tomato')
plt.xlabel('periodo', fontsize=16)
plt.ylabel('Rmax/m*', fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.show()

transit=pianeti.loc[( pianeti['discoverymethod'] =='Transit')]
rad_vel=pianeti.loc[( pianeti['discoverymethod'] == 'Radial Velocity')]

plt.scatter(transit['pl_orbper'] , transit['pl_bmassj'], color='royalblue', s=68, label='transit', alpha=0.5)
plt.scatter(rad_vel['pl_orbper'] , rad_vel['pl_bmassj'], color='tomato',   s=68, label='radial velocity', alpha=0.5)
plt.xlabel('periodo', fontsize=16)
plt.ylabel('massa', fontsize=16)
plt.legend(fontsize=14)
plt.xscale('log')
plt.yscale('log')
plt.show()

trm=np.log(transit['pl_bmassj'])
rvm=np.log(rad_vel['pl_bmassj'])
n, bis, p = plt.hist(rvm, bins=200, range=(0, 8), color='gold', label='radial velocity',alpha=0.5 )
n, bis, p = plt.hist(trm, bins=200, range=(0, 8), color='green',label='transit',alpha=0.5 )
plt.ylabel('massa', fontsize=16)
plt.legend(fontsize=14)
plt.show()


