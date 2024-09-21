import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import graph_annotator

# read sample data
df = pd.read_csv('sample_data.csv')

# box plot
plt.figure()
sns.boxplot(x='condition', y='score', data=df)

# set y-axis limit
plt.ylim(0, 14)

# draw line and text of significant difference
graph_annotator.significance('**', df, 0, 1, column_name='condition')
graph_annotator.significance('***', df, 2, 3, column_name='condition')

plt.show()
