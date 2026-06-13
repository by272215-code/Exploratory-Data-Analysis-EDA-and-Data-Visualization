import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "Age": [20, 22, 21, 23, 25, 24, 22, 26],
    "Study_Hours": [2, 3, 4, 5, 6, 5, 4, 7],
    "Marks": [55, 60, 65, 70, 80, 75, 68, 90]
}
df = pd.DataFrame(data)
print("First 5 Records:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
print("\nCorrelation Matrix:")
print(df.corr())

# Histogram
plt.figure(figsize=(6,4))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(5,4))
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()