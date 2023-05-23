import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the CSV file
df = pd.read_csv('pipeline_job_summary.csv')

# Extract the relevant columns
statuses = df['Status']
occurrences = df['Occurrences']
Joint = df['Status'] + ' ' + df['Reason']

# Replace NaN labels with values from df['Status']
Joint = np.where(pd.isnull(Joint), statuses, Joint)

# Set color palette
colors = sns.color_palette('bright')

# Create a pie chart
plt.figure(figsize=(8, 6))  # Specify the figure size in inches
plt.pie(occurrences, labels=Joint, autopct='%1.1f%%', colors=colors)

# Add legend
legend_labels = [f'{s} - {r}' for s, r in zip(df['Status'], df['Reason'])]
plt.legend(legend_labels, loc='lower left')

# Add title
plt.title('Pipeline Job Summary')

# Add color indicators and labels
patches, _ = plt.pie(occurrences, colors=colors)
plt.legend(patches, legend_labels, loc='best')

# Save the pie chart as an image
plt.savefig('pipeline_job_summary.jpg', dpi=300)
plt.show()

