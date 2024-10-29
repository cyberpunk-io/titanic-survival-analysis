import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Basic data analysis
print(df.describe())
print(df['Survived'].value_counts())

# Visualize survival rates
plt.figure(figsize=(10, 6))
df['Survived'].value_counts().plot(kind='bar', color=['red', 'green'])
plt.title('Survival Counts on the Titanic')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.xticks(ticks=[0, 1], labels=['Did Not Survive', 'Survived'], rotation=0)
plt.show()