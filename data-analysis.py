import pandas as pd
df = pd.read_csv(r"C:\Users\nitis\Downloads\diabetes-data.csv")
print(df.head())

print(df.describe())
print(df['Age'].value_counts())

print(df.dtypes)
df['BMI'] = pd.to_numeric(df['BMI'])

print(df.isnull().sum())
df.dropna(inplace=True)

import matplotlib.pyplot as plt


# Histogram

plt.hist(df['BloodPressure'], bins=5)
plt.xlabel('BloodPressure')
plt.ylabel('Frequency')
plt.show()


# Scatter plot

plt.scatter(df['Age'], df['Glucose'])
plt.xlabel('Age')
plt.ylabel('Glucose')
plt.show()


# correlation matrix

import seaborn as sns
correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()


# Box plot
plt.boxplot(df['Pregnancies'])
plt.xlabel('Pregnancies')
plt.show()


# Group by a categorical column (outcome)(Age) and calculate mean

grouped = df.groupby('Outcome')['Age'].mean()
print(grouped)

# Random sampling

sampled_df = df.sample(n=100, random_state=42)
print(sampled_df)


# Binning numeric data(outcome column) into categories

bins = [-1,0,1]
labels = ['negative','positive']
df['report_outcome'] = pd.cut(df['Outcome'], bins=bins, labels=labels)
print(df.head())


# Export

df.to_csv(r"C:\Users\nitis\Downloads\updated-diabetes-data.csv", index=False)









