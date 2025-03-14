#task 1
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Error handling for file loading
try:
    # Load Iris dataset using sklearn for demonstration, but you would load from CSV for other datasets
    iris = pd.DataFrame(pd.DataFrame(iris.data, columns=iris.feature_names),
                        index=iris.target_names)
    # If loading from CSV:
    # df = pd.read_csv('path_to_your_dataset.csv')
except FileNotFoundError:
    print("Error: The dataset file was not found.")

# Display the first few rows
print(iris.head())

# Explore the structure of the dataset
print(iris.info())

# Check for missing values
print(iris.isnull().sum())

# Clean the dataset: Let's assume there are missing values and we decide to drop them
iris = iris.dropna()

#**Task 2: Basic Data Analysis**

# Compute basic statistics
print(iris.describe())

# Groupby analysis (assuming 'species' as a categorical column and 'petal length (cm)' as numerical)
grouped = iris.groupby('species')['petal length (cm)'].mean()
print(grouped)

#**Task 3: Data Visualization**

# Create visualizations

# Line chart (Note: For Iris dataset, a time-series doesn't make sense. For other datasets like sales, you would use timestamps.)
# Let's move to a suitable visualization - Bar chart
plt.figure(figsize=(10,6))
sns.barplot(x='species', y='petal length (cm)', data=iris)
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# Histogram for understanding distribution of 'petal width (cm)'
plt.figure(figsize=(10,6))
sns.histplot(data=iris, x='petal width (cm)', bins=30, kde=True)
plt.title('Distribution of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.show()

# Scatter plot to visualize the relationship between 'sepal length (cm)' and 'petal length (cm)'
plt.figure(figsize=(10,8))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
