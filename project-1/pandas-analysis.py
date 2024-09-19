import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('sales_data.csv')

# Display basic information about the dataset
print(df.info())
print("\nFirst few rows:")
print(df.head())

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Calculate some basic statistics
print("\nBasic statistics:")
print(df.describe())

# Detect outliers using Interquartile Range (IQR) method
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

# Detect outliers in Quantity and Price columns
quantity_outliers = detect_outliers(df, 'Quantity')
price_outliers = detect_outliers(df, 'Price')

print("\nQuantity outliers:")
print(quantity_outliers[['Date', 'Product', 'Quantity']])

print("\nPrice outliers:")
print(price_outliers[['Date', 'Product', 'Price']])

# Analyze sales by category
category_sales = df.groupby('Category')['Total'].sum().sort_values(descending=True)
print("\nSales by category:")
print(category_sales)

# Visualize sales by category
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('sales_by_category.png')

# Analyze daily sales trend
daily_sales = df.groupby('Date')['Total'].sum()
plt.figure(figsize=(12, 6))
daily_sales.plot()
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('daily_sales_trend.png')

print("\nAnalysis complete. Check the generated plots for visualizations.")
