import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('/Users/jessicasamir/Desktop/spie2024/DCS_submissionfor8models.csv')

# Create separate figures for pmodel and SpleenModel11 comparisons
fig, axes = plt.subplots(2, 3, figsize=(18, 8))

# pmodel15 vs pmodel30
ax = axes[0, 0]
sns.scatterplot(x=(df['pmodel15'] + df['pmodel30']) / 2, y=df['pmodel15'] - df['pmodel30'], ax=ax, color='orange')
ax.axhline(0, color='k', linestyle='--')
#ax.set_title('PancreasModel15 vs PancreasModel30', fontname='Times New Roman')
ax.set_xlabel('Avg. of PancreasModel15 & PancreasModel30', fontname='Times New Roman')
ax.set_ylabel('Diff. b/w PancreasModel15 & PancreasModel30', fontname='Times New Roman')
ax.set_ylim([-1, 0.5])

# pmodel15 vs pmodel50
ax = axes[0, 1]
sns.scatterplot(x=(df['pmodel15'] + df['pmodel50']) / 2, y=df['pmodel15'] - df['pmodel50'], ax=ax, color='orange')
ax.axhline(0, color='k', linestyle='--')
#ax.set_title('PancreasModel15 vs PancreasModel50', fontname='Times New Roman')
ax.set_xlabel('Avg. of PancreasModel15 & PancreasModel50', fontname='Times New Roman')
ax.set_ylabel('Diff. b/w PancreasModel15 & PancreasModel50', fontname='Times New Roman')
ax.set_ylim([-1, 0.5])

# pmodel15 vs pmodel70
ax = axes[0, 2]
sns.scatterplot(x=(df['pmodel15'] + df['pmodel70']) / 2, y=df['pmodel15'] - df['pmodel70'], ax=ax, color='orange')
ax.axhline(0, color='k', linestyle='--')
#ax.set_title('PancreasModel15 vs PancreasModel70', fontname='Times New Roman')
ax.set_xlabel('Avg. of PancreasModel15 & PancreasModel70', fontname='Times New Roman')
ax.set_ylabel('Diff. b/w PancreasModel15 & PancreasModel70', fontname='Times New Roman')
ax.set_ylim([-1, 0.5])

# SpleenModel11 vs SpleenModel23
ax = axes[1, 0]
sns.scatterplot(x=(df['smodel11'] + df['smodel23']) / 2, y=df['smodel11'] - df['smodel23'], ax=ax, color='purple')
ax.axhline(0, color='k', linestyle='--')
#ax.set_title('SpleenModel11 vs SpleenModel23', fontname='Times New Roman')
ax.set_xlabel('Avg. of SpleenModel11 & SpleenModel23', fontname='Times New Roman')
ax.set_ylabel('Diff. b/w SpleenModel11 & SpleenModel23', fontname='Times New Roman')
ax.set_ylim([-1, 0.5])

# SpleenModel11 vs SpleenModel28
ax = axes[1, 1]
sns.scatterplot(x=(df['smodel11'] + df['smodel28']) / 2, y=df['smodel11'] - df['smodel28'], ax=ax, color='purple')
ax.axhline(0, color='k', linestyle='--')
#ax.set_title('SpleenModel11 vs SpleenModel28', fontname='Times New Roman')
ax.set_xlabel('Avg. of SpleenModel11 & SpleenModel28', fontname='Times New Roman')
ax.set_ylabel('Diff. b/w SpleenModel11 & SpleenModel28', fontname='Times New Roman')
ax.set_ylim([-1, 0.5])

# SpleenModel11 vs SpleenModel34
ax = axes[1, 2]
sns.scatterplot(x=(df['smodel11'] + df['smodel34']) / 2, y=df['smodel11'] - df['smodel34'], ax=ax, color='purple')
ax.axhline(0, color='k', linestyle='--')
#ax.set_title('SpleenModel11 vs SpleenModel34', fontname='Times New Roman')
ax.set_xlabel('Avg. of SpleenModel11 & SpleenModel34', fontname='Times New Roman')
ax.set_ylabel('Diff. b/w SpleenModel11 & SpleenModel34', fontname='Times New Roman')
ax.set_ylim([-1, 0.5])

# Set the same x and y axis limits for all plots
min_val = min(df['pmodel15'].min(), df['pmodel30'].min(), df['pmodel50'].min(), df['pmodel70'].min(), df['smodel11'].min(), df['smodel23'].min(), df['smodel28'].min(), df['smodel34'].min())
max_val = max(df['pmodel15'].max(), df['pmodel30'].max(), df['pmodel50'].max(), df['pmodel70'].max(), df['smodel11'].max(), df['smodel23'].max(), df['smodel28'].max(), df['smodel34'].max())
for ax in axes.flat:
    ax.set_xlim([min_val, max_val])

plt.savefig('blandaltmanfigure.tiff', dpi=360, format='tiff')
plt.tight_layout()
plt.show()












'''
# Create separate figures for pmodel comparisons
fig, axes = plt.subplots(1, 3, figsize=(16, 4.25))

# pmodel15 vs pmodel30
ax = axes[0]
sns.scatterplot(x=(df['pmodel15'] + df['pmodel30']) / 2, y=df['pmodel15'] - df['pmodel30'], ax=ax, color='orange')
ax.axhline(0, color='k', linestyle='--')
ax.set_title('PancreasModel15 vs PancreasModel30', fontname='Times New Roman')
ax.set_xlabel('Avg. of PancreasModel15 & PancreasModel30', fontname='Times New Roman')
ax.set_ylabel('Diff. between PancreasModel15 & PancreasModel30', fontname='Times New Roman')
min_val = min(df['pmodel15'].min(), df['pmodel30'].min(), df['pmodel50'].min(), df['pmodel70'].min(), df['smodel11'].min(), df['smodel23'].min(), df['smodel28'].min(), df['smodel34'].min())
max_val = max(df['pmodel15'].max(), df['pmodel30'].max(), df['pmodel50'].max(), df['pmodel70'].max(), df['smodel11'].max(), df['smodel23'].max(), df['smodel28'].max(), df['smodel34'].max())
ax.set_xlim([min_val, max_val])
ax.set_ylim([min_val, max_val])

# pmodel15 vs pmodel50
ax = axes[1]
sns.scatterplot(x=(df['pmodel15'] + df['pmodel50']) / 2, y=df['pmodel15'] - df['pmodel50'], ax=ax, color='orange')
ax.axhline(0, color='k', linestyle='--')
ax.set_title('PancreasModel15 vs PancreasModel50', fontname='Times New Roman')
ax.set_xlabel('Avg. of PancreasModel15 & PancreasModel50', fontname='Times New Roman')
ax.set_ylabel('Diff. between PancreasModel15 & PancreasModel50', fontname='Times New Roman')
min_val = min(df['pmodel15'].min(), df['pmodel30'].min(), df['pmodel50'].min(), df['pmodel70'].min(), df['smodel11'].min(), df['smodel23'].min(), df['smodel28'].min(), df['smodel34'].min())
max_val = max(df['pmodel15'].max(), df['pmodel30'].max(), df['pmodel50'].max(), df['pmodel70'].max(), df['smodel11'].max(), df['smodel23'].max(), df['smodel28'].max(), df['smodel34'].max())
ax.set_xlim([min_val, max_val])
ax.set_ylim([min_val, max_val])

# pmodel15 vs pmodel70
ax = axes[2]
sns.scatterplot(x=(df['pmodel15'] + df['pmodel70']) / 2, y=df['pmodel15'] - df['pmodel70'], ax=ax, color='orange')
ax.axhline(0, color='k', linestyle='--')
ax.set_title('PancreasModel15 vs PancreasModel70', fontname='Times New Roman')
ax.set_xlabel('Avg. of PancreasModel15 & PancreasModel70', fontname='Times New Roman')
ax.set_ylabel('Diff. between PancreasModel15 & PancreasModel70', fontname='Times New Roman')
min_val = min(df['pmodel15'].min(), df['pmodel30'].min(), df['pmodel50'].min(), df['pmodel70'].min(), df['smodel11'].min(), df['smodel23'].min(), df['smodel28'].min(), df['smodel34'].min())
max_val = max(df['pmodel15'].max(), df['pmodel30'].max(), df['pmodel50'].max(), df['pmodel70'].max(), df['smodel11'].max(), df['smodel23'].max(), df['smodel28'].max(), df['smodel34'].max())
ax.set_xlim([min_val, max_val])
ax.set_ylim([min_val, max_val])


plt.savefig('pancreas.tiff', dpi=360, format='tiff')
plt.tight_layout()
plt.show()


#spleenmodelfigure
# Create separate figures for SpleenModel11 comparisons
fig, axes = plt.subplots(1, 3, figsize=(16, 4))

# SpleenModel11 vs SpleenModel23
ax = axes[0]
sns.scatterplot(x=(df['smodel11'] + df['smodel23']) / 2, y=df['smodel11'] - df['smodel23'], ax=ax, color='purple')
ax.axhline(0, color='k', linestyle='--')
ax.set_title('SpleenModel11 vs SpleenModel23', fontname='Times New Roman')
ax.set_xlabel('Avg. of SpleenModel11 & SpleenModel23', fontname='Times New Roman')
ax.set_ylabel('Diff. between SpleenModel11 & SpleenModel23', fontname='Times New Roman')

# SpleenModel11 vs SpleenModel28
ax = axes[1]
sns.scatterplot(x=(df['smodel11'] + df['smodel28']) / 2, y=df['smodel11'] - df['smodel28'], ax=ax, color='purple')
ax.axhline(0, color='k', linestyle='--')
ax.set_title('SpleenModel11 vs SpleenModel28', fontname='Times New Roman')
ax.set_xlabel('Avg. of SpleenModel11 & SpleenModel28', fontname='Times New Roman')
ax.set_ylabel('Diff. between SpleenModel11 & SpleenModel28', fontname='Times New Roman')

# SpleenModel11 vs SpleenModel34
ax = axes[2]
sns.scatterplot(x=(df['smodel11'] + df['smodel34']) / 2, y=df['smodel11'] - df['smodel34'], ax=ax, color='purple')
ax.axhline(0, color='k', linestyle='--')
ax.set_title('SpleenModel11 vs SpleenModel34', fontname='Times New Roman')
ax.set_xlabel('Avg. of SpleenModel11 & SpleenModel34', fontname='Times New Roman')
ax.set_ylabel('Diff. between SpleenModel11 & SpleenModel34', fontname='Times New Roman')


plt.savefig('spleen.tiff', dpi=360, format='tiff')
plt.tight_layout()
plt.show()
'''