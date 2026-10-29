import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv('matplotlib\data.csv')
type_count = df['Type1'].value_counts(ascending=True)
# print(type_count)

plt.barh(type_count.index, type_count.values, color='blue',
         edgecolor='black')

plt.title('Pokemon Type Distribution')
plt.xlabel('Count')
plt.ylabel('Type of pokemon')
plt.tight_layout()
plt.show()