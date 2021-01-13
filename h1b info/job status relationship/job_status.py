import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
https://stackoverflow.com/questions/42770379/pandas-change-order-of-crosstab-result
https://stackoverflow.com/questions/38337918/plot-pie-chart-and-table-of-pandas-dataframe
https://stackoverflow.com/questions/29219055/plot-top-10-verse-all-other-values

'''
df = pd.read_csv("h1b_kaggle.csv")
# concat job title and status to a new dataframe for analysis purpose
sta = pd.crosstab(df['JOB_TITLE'], df['CASE_STATUS'])
#fig, axs = plt.subplots(2, 2)
f, axs = plt.subplots(2,2,figsize=(20,20))

# see percentage of each status to help further analysis
plt.subplot(2,2,1)
df['CASE_STATUS'].value_counts().head(3).plot.pie(autopct='%1.1f%%')
plt.legend()
# and get the top 3 freq of status are
#   CERTIFIED, CERTIFIED-WITHDRAWN, AND DENIED

#------------------certified---------------------#
certify = sta.groupby(['JOB_TITLE'])['CERTIFIED'].sum().nlargest(15)
certify = certify.to_frame().reset_index()

plt.subplot(2,2,2)
sns.barplot(certify['CERTIFIED'], certify['JOB_TITLE'], alpha=0.8)
plt.title('Job title top 15 applying h1b certified')
plt.ylabel('num of certified', fontsize=12)

# put value in bar graph
for index, value in enumerate(certify['CERTIFIED']):
    plt.text(value, index, s=round(value, 0))


#------------------certified-withdrawn---------------------#
cerw = sta.groupby(['JOB_TITLE'])['CERTIFIED-WITHDRAWN'].sum().nlargest(15)
cerw = cerw.to_frame().reset_index()

plt.subplot(2,2,3)
sns.barplot(cerw['CERTIFIED-WITHDRAWN'], cerw['JOB_TITLE'], alpha=0.8)
plt.title('Job title top 15 applying h1b certified but withdrawned')
plt.ylabel('CERTIFIED but WITHDRAWN', fontsize=12)

# put value in bar graph
for index, value in enumerate(cerw['CERTIFIED-WITHDRAWN']):
    plt.text(value, index, s=round(value, 0))


#------------------denied---------------------#
deny = sta.groupby(['JOB_TITLE'])['DENIED'].sum().nlargest(15)
deny = deny.to_frame().reset_index()

plt.subplot(2,2,4)
sns.barplot(deny['DENIED'], deny['JOB_TITLE'], alpha=0.8)
plt.title('Job title top 15 applying h1b denied')
plt.ylabel('CERTIFIED but WITHDRAWN', fontsize=12)

# put value in bar graph
for index, value in enumerate(deny['DENIED']):
    plt.text(value, index, s=round(value, 0))

plt.tight_layout()
plt.savefig("top 15 h1b application job status info.png")
plt.show()
plt.close()