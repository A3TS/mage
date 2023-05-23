import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read the CSV file
df = pd.read_csv('pipeline_job_summary.csv')

#Extract the relevant columns
stat = df['Reason']
statuses = df['Status']
occurrences = df['Occurrences']
Joint = df['Status'] + ' ' + df['Reason']

#Set color palette
colors = sns.color_palette('bright')

#Create a pie chart
plt.figure(figsize=(8, 6)) # Specify the figure size in inches
plt.pie(occurrences, labels=Joint, autopct='%1.1f%%', colors=colors)

#Add legend
legend_labels = df['Status'] + ' - ' + df['Reason']
plt.legend(legend_labels, loc='best')

#Add title
plt.title('Pipeline Job Summary')

#Save the pie chart as an image
plt.savefig('pipeline_job_summary.jpg', dpi=300)
plt.show()

