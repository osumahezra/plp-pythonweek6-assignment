import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"PYTHON CLASS\plp-pythonweek7-assignment\Iris.csv")
df=pd.DataFrame(df)
print(df.head())
print(df.info())
# There are no null data in the dataset
print(df.describe())
dfsummary = df.groupby('Species').mean()
print(dfsummary)
# The average length in centmeters of the sepal for each species is specified in the column "SepalLengthCm"
# The average width in centmeters of the sepal for each species is specified in the column "SepalWidthCm"
# The average length in centmeters of the petal for each species is specified in the column "PetalLengthCm"
# The average width in centmeters of the petal for each species is specified in the column "PetalWidthCm"
dfsummary['PetalLengthCm'].plot(kind='bar')
plt.title('Petal Length Distribution')
plt.xlabel('Petal Length (cm)')
plt.show()


df['PetalWidthCm'].plot(kind='hist', bins=10)
plt.title('Species Distribution')
plt.xlabel('Species')
plt.show()

df.plot(x='SepalLengthCm', y='PetalLengthCm', kind='scatter')
plt.title('Petal Lenght vs Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='SepalLengthCm',
    y='PetalLengthCm',
    hue='Species',
    palette='Set1'
)
plt.title('Petal Length vs Sepal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

