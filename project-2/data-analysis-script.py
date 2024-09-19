import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Load the data
df = pd.read_csv('sample_sales_data.csv')

# Data Cleaning
def clean_data(df):
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Remove any duplicate rows
    df = df.drop_duplicates()
    
    # Handle missing values
    df['sales'] = df['sales'].fillna(df.groupby('product')['sales'].transform('mean'))
    df['quantity'] = df['quantity'].fillna(df.groupby('product')['quantity'].transform('median'))
    
    # Create a new column for total revenue
    df['total_revenue'] = df['sales'] * df['quantity']
    
    # Normalize product names
    df['product'] = df['product'].str.lower().str.strip()
    
    # Create a categorical column for sales performance
    df['sales_performance'] = pd.cut(df['total_revenue'], 
                                     bins=[0, 100, 200, 500, np.inf], 
                                     labels=['Poor', 'Average', 'Good', 'Excellent'])
    
    return df

# Group and Aggregate Data
def analyze_data(df):
    # Group by date and category, calculate total revenue and average quantity
    daily_category_stats = df.groupby([df['date'].dt.date, 'category']).agg({
        'total_revenue': 'sum',
        'quantity': 'mean'
    }).reset_index()
    
    # Calculate 7-day rolling average of total revenue by product
    product_revenue_ma = df.groupby(['product', df['date'].dt.date])['total_revenue'].sum().reset_index()
    product_revenue_ma['7day_ma'] = product_revenue_ma.groupby('product')['total_revenue'].rolling(window=7, min_periods=1).mean().reset_index(0, drop=True)
    
    # Find top 3 products by total revenue for each region
    top_products_by_region = df.groupby(['region', 'product'])['total_revenue'].sum().reset_index()
    top_products_by_region = top_products_by_region.sort_values(['region', 'total_revenue'], ascending=[True, False]).groupby('region').head(3)
    
    # Calculate customer lifetime value
    customer_ltv = df.groupby('customer_id')['total_revenue'].sum().reset_index()
    customer_ltv['ltv_segment'] = pd.qcut(customer_ltv['total_revenue'], q=4, labels=['Bronze', 'Silver', 'Gold', 'Platinum'])
    
    return daily_category_stats, product_revenue_ma, top_products_by_region, customer_ltv

# Main execution
if __name__ == "__main__":
    # Clean the data
    cleaned_df = clean_data(df)
    
    # Analyze the data
    daily_category_stats, product_revenue_ma, top_products_by_region, customer_ltv = analyze_data(cleaned_df)
    
    # Print some results
    print("Daily Category Stats:")
    print(daily_category_stats.head())
    
    print("\nProduct Revenue 7-Day Moving Average:")
    print(product_revenue_ma.head(10))
    
    print("\nTop 3 Products by Region:")
    print(top_products_by_region)
    
    print("\nCustomer Lifetime Value Segments:")
    print(customer_ltv.head(10))
    
    # Export results to CSV
    daily_category_stats.to_csv('daily_category_stats.csv', index=False)
    product_revenue_ma.to_csv('product_revenue_ma.csv', index=False)
    top_products_by_region.to_csv('top_products_by_region.csv', index=False)
    customer_ltv.to_csv('customer_ltv.csv', index=False)
