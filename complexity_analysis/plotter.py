import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('CRIMEgamma_plots.csv')


sns.axes_style("white")


PREF = 'CRIME'
'''
df=pd.read_csv(PREF + 'allmodels.csv')
df1=df.groupby('src').count()
df2=df.groupby('src').mean()
df2['ct']=df1.tgt
ax=df2.plot(x='gamma',y='ct',style='k.')
ax=sns.jointplot(x='gamma',y='ct',data=df2,kind='kde',xlim=[0,0.03])

plt.show()
'''


ax = sns.jointplot(y="numSrc", x="srcmean_gamma", data=df,kind='hex')
plt.title(PREF)

plt.savefig(PREF + 'mean_gammahex.png')
plt.figure()

ax = sns.jointplot(y="numSrc", x="srcmed_gamma", data=df,kind='hex')
plt.title(PREF)

plt.savefig(PREF +'med_gammahex.png')
plt.figure()

ax = sns.jointplot(y="numTgt", x="tgtmean_gamma", data=df,kind='hex')
plt.title(PREF)

plt.savefig(PREF +'mean_gammahex2.png')
plt.figure()

ax = sns.jointplot(y="numTgt", x="tgtmed_gamma", data=df,kind='hex')
plt.title(PREF)

plt.savefig(PREF +'med_gammahex2.png')
plt.figure()


PREF = 'CRIME'
ax = sns.scatterplot(y="numSrc", x="srcmean_gamma", data=df)
plt.title(PREF)

plt.savefig(PREF + 'mean_gammascatter.png')
plt.figure()

ax = sns.scatterplot(y="numSrc", x="srcmed_gamma", data=df)
plt.title(PREF)

plt.savefig(PREF +'med_gammascatter.png')
plt.figure()

ax = sns.scatterplot(y="numTgt", x="tgtmean_gamma", data=df)
plt.title(PREF)

plt.savefig(PREF +'mean_gammascatter2.png')
plt.figure()

ax = sns.scatterplot(y="numTgt", x="tgtmed_gamma", data=df)
plt.title(PREF)

plt.savefig(PREF +'med_gammascatter2.png')
plt.figure()
