### Module 10: Final Project: Data Cleaning Exercise

In this module, you will apply all the techniques learned throughout the course to a real-world dataset. This hands-on project will give you practical experience in data cleaning, allowing you to document your process and results.

#### Sample Dataset

For this project, we’ll use a sample dataset containing sales data for a fictional retail store. You can download the dataset from the following link:

[Download Sales Data CSV](https://raw.githubusercontent.com/yourusername/yourrepository/main/sales_data.csv)

**Sample Data Structure:**
```plaintext
| Order_ID | Customer_Name | Order_Date  | Product    | Quantity | Price   | Shipping_Cost | Rating | Comments            |
|----------|---------------|-------------|------------|----------|---------|----------------|--------|---------------------|
| 1        | Alice         | 2023-01-01  | Widget A   | 2        | 25.50   | 5.00           | 4.5    | Fast delivery       |
| 2        | Bob           | 2023-01-02  | Widget B   | 1        | 15.00   | 3.00           | NaN    |                     |
| 3        | Charlie       | 2023-02-03  | Widget A   | 5        | 127.50  | 8.00           | 5.0    | Great product!      |
| 4        | David         | 2023-03-04  | Widget C   | 0        | 30.00   | 2.00           | 2.5    | Late delivery       |
| 5        | Eva           | 2023-03-05  | Widget A   | 3        | NaN     | 5.00           | 3.0    |                     |
| 6        | Frank         | 2023-04-06  | Widget B   | 2        | 15.00   | NaN            | 4.0    | Good value          |
| 7        | Grace         | 2023-04-07  | Widget C   | 1        | 30.00   | 4.00           | 4.5    |                     |
| 8        | Heidi         | 2023-05-08  | Widget A   | 1        | 25.50   | 5.00           | 5.0    | Perfect!            |
```

### Project Guidelines

1. **Import Libraries and Load the Dataset**
   - Start by importing necessary libraries like Pandas and NumPy. Load the dataset using `pd.read_csv()`.

   ```python
   import pandas as pd

   # Load the dataset
   df = pd.read_csv('sales_data.csv')
   print(df.head())
   ```

2. **Explore the Data**
   - Use `info()`, `describe()`, and `head()` to understand the dataset's structure, data types, and any initial observations regarding missing values or anomalies.

   ```python
   df.info()
   df.describe()
   ```

3. **Handle Missing Data**
   - Identify missing values in the dataset and apply appropriate strategies:
     - Use `fillna()` to fill missing ratings with the mean rating.
     - Use `dropna()` to remove any rows with critical missing values like `Price` or `Quantity`.

   ```python
   df['Rating'].fillna(df['Rating'].mean(), inplace=True)
   df.dropna(subset=['Price', 'Quantity'], inplace=True)
   ```

4. **Standardize Data Formats**
   - Ensure the `Order_Date` is in a consistent datetime format using `pd.to_datetime()`.
   - Standardize categorical variables (e.g., ensuring product names are consistently formatted).

   ```python
   df['Order_Date'] = pd.to_datetime(df['Order_Date'])
   df['Product'] = df['Product'].str.strip().str.title()  # Standardize product names
   ```

5. **Identify and Handle Outliers**
   - Use the Z-score or IQR method to identify and either remove or cap outliers in the `Price` and `Quantity` columns.

   ```python
   Q1 = df['Price'].quantile(0.25)
   Q3 = df['Price'].quantile(0.75)
   IQR = Q3 - Q1

   df = df[~((df['Price'] < (Q1 - 1.5 * IQR)) | (df['Price'] > (Q3 + 1.5 * IQR)))]
   ```

6. **Document Your Cleaning Process**
   - Create a Markdown file (or use comments in your code) to document the steps taken during the cleaning process. Include observations, decisions made, and any challenges faced.

7. **Analyze and Visualize the Cleaned Data**
   - After cleaning the data, perform basic analyses such as total sales per product, average rating, etc. Use libraries like Matplotlib or Seaborn for visualizations.

   ```python
   import matplotlib.pyplot as plt

   # Total sales per product
   total_sales = df.groupby('Product')['Price'].sum()
   total_sales.plot(kind='bar')
   plt.title('Total Sales per Product')
   plt.xlabel('Product')
   plt.ylabel('Total Sales')
   plt.show()
   ```

8. **Present Your Results**
   - Summarize your findings and results in a report or presentation. Include key insights gained from the data and how cleaning improved the dataset's usability.

### Conclusion

By completing this project, you'll gain hands-on experience with the entire data cleaning process. You'll learn how to apply various techniques in a real-world context, enhancing your skills and preparing you for future data analysis projects.