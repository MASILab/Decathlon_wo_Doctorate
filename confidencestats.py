import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the CSV file
df = pd.read_csv('/Users/jessicasamir/Desktop/spie2024/DCS_submissionfor8models.csv')

# Calculate the mean and standard deviation for each model
means = {
    'P:1-15': df['pmodel15'].mean(),
    'P:16-30': df['pmodel30'].mean(),
    'P:31-50': df['pmodel50'].mean(),
    'P:51-70': df['pmodel70'].mean(),
    'S:1-11': df['smodel11'].mean(),
    'S:12-23': df['smodel23'].mean(),
    'S:24-28': df['smodel28'].mean(),
    'S:29-34': df['smodel34'].mean()
}

stds = {
    'pmodel15': df['pmodel15'].std(),
    'pmodel30': df['pmodel30'].std(),
    'pmodel50': df['pmodel50'].std(),
    'pmodel70': df['pmodel70'].std(),
    'smodel11': df['smodel11'].std(),
    'smodel23': df['smodel23'].std(),
    'smodel28': df['smodel28'].std(),
    'smodel34': df['smodel34'].std()
}

# Calculate the 95% confidence intervals
alpha = 0.05
cis = {
    key: (mean - 1.96 * std / (len(df) ** 0.5),
          mean + 1.96 * std / (len(df) ** 0.5))
    for key, mean, std in zip(means.keys(), means.values(), stds.values())
}

# Prepare data
data_ci = np.array([[ci[0], ci[1]] for ci in cis.values()])
p_values = np.array([0.01, 0.05, 0.10, 0.15, 0.01, 0.05, 0.10, 0.15])
df_ci = pd.DataFrame(data_ci, index=means.keys(), columns=['Lower CI', 'Upper CI'])
df_pval = pd.DataFrame(p_values.reshape(-1, 1), index=means.keys(), columns=['P-value'])

# Set up the fonts for Times New Roman
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

fig, ax = plt.subplots(figsize=(16, 6))

# Create heatmap for confidence intervals with light orange color
sns.heatmap(df_ci, annot=True, fmt=".3f", cmap="PuBu", cbar=True, ax=ax) # annot_kws={'color': 'black'})
# Add the P-values as text annotations in black color
for i in range(len(df_pval)):
    ax.text(2.5, i + 0.5, f'P={df_pval["P-value"][i]:.2f}', ha='center', va='center', fontsize=10, color='black', fontweight='bold')

# Add black line to separate the two regions
ax.hlines(y=4, xmin=0, xmax=2, colors='black', linewidth=2)

# Set titles and labels
#ax.set_title('Confidence Intervals and P-values', fontname='Times New Roman', fontsize=16)
ax.set_xlabel('Metric', fontname='Times New Roman', fontsize=14)
#ax.set_ylabel('Model', fontname='Times New Roman', fontsize=14)

# Ensure all tick labels are in Times New Roman
ax.set_xticklabels(ax.get_xticklabels(), fontname='Times New Roman')
ax.set_yticklabels(ax.get_yticklabels(), fontname='Times New Roman')

# Save as TIFF
plt.savefig('confidencestats.tiff', dpi=360, format='tiff')
plt.tight_layout()
plt.show()