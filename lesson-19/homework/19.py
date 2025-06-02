#Homework 1
import pandas as pd

# 1. Ma'lumotlarni yuklash
sales_df = pd.read_csv("task\\sales_data.csv")

# 2. Kategoriya bo'yicha umumiy statistika
category_stats = sales_df.groupby('Category').agg(
    Total_Quantity_Sold=('Quantity', 'sum'),
    Average_Price_Per_Unit=('Price', 'mean'),
    Max_Quantity_Single_Transaction=('Quantity', 'max')
).reset_index()

print("Kategoriya bo‘yicha statistikalar:")
print(category_stats)
print("\n")

# 3. Har bir kategoriya uchun eng ko‘p sotilgan mahsulot
product_sales = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()

top_products = product_sales.sort_values(['Category', 'Quantity'], ascending=[True, False]).groupby('Category').first().reset_index()

print("Har bir kategoriya uchun eng ko‘p sotilgan mahsulot:")
print(top_products)
print("\n")

# 4. Eng yuqori umumiy savdo bo‘lgan sana (Quantity * Price)
sales_df['Total_Sale'] = sales_df['Quantity'] * sales_df['Price']

daily_sales = sales_df.groupby('Date')['Total_Sale'].sum().reset_index()

top_sales_date = daily_sales.loc[daily_sales['Total_Sale'].idxmax()]

print("Eng yuqori savdo bo‘lgan sana:")
print(top_sales_date)


#Homework 2
import pandas as pd

# 1. Ma'lumotlarni yuklash
sales_df = pd.read_csv("task\\sales_data.csv")

# 2. Kategoriya bo'yicha umumiy statistika
category_stats = sales_df.groupby('Category').agg(
    Total_Quantity_Sold=('Quantity', 'sum'),
    Average_Price_Per_Unit=('Price', 'mean'),
    Max_Quantity_Single_Transaction=('Quantity', 'max')
).reset_index()

print("Kategoriya bo‘yicha statistikalar:")
print(category_stats)
print("\n")

# 3. Har bir kategoriya uchun eng ko‘p sotilgan mahsulot
product_sales = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()

top_products = product_sales.sort_values(['Category', 'Quantity'], ascending=[True, False]) \
                            .groupby('Category').first().reset_index()

print("Har bir kategoriya uchun eng ko‘p sotilgan mahsulot:")
print(top_products)
print("\n")

# 4. Eng yuqori umumiy savdo bo‘lgan sana (Quantity * Price)
sales_df['Total_Sale'] = sales_df['Quantity'] * sales_df['Price']

daily_sales = sales_df.groupby('Date')['Total_Sale'].sum().reset_index()

top_sales_date = daily_sales.loc[daily_sales['Total_Sale'].idxmax()]

print("Eng yuqori savdo bo‘lgan sana:")
print(top_sales_date)


#Homework 3
import sqlite3
import pandas as pd
import numpy as np

# 1. Load population data from SQLite database
conn = sqlite3.connect('task/population.db')
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# 2. Load salary bands from Excel
salary_bands_df = pd.read_excel('task/population salary analysis.xlsx')

# Ensure columns: 'Band', 'MinSalary', 'MaxSalary'
# 3. Assign salary band to each person
def get_salary_band(salary):
    for _, row in salary_bands_df.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['Band']
    return 'Uncategorized'

population_df['SalaryBand'] = population_df['Salary'].apply(get_salary_band)

# 4. Overall Statistics by SalaryBand
total_population = len(population_df)

overall_stats = population_df.groupby('SalaryBand').agg(
    PopulationCount=('Salary', 'count'),
    AverageSalary=('Salary', 'mean'),
    MedianSalary=('Salary', 'median')
).reset_index()

overall_stats['PopulationPercentage'] = (overall_stats['PopulationCount'] / total_population) * 100

# 5. State-wise Statistics by SalaryBand
state_group = population_df.groupby(['State', 'SalaryBand']).agg(
    PopulationCount=('Salary', 'count'),
    AverageSalary=('Salary', 'mean'),
    MedianSalary=('Salary', 'median')
).reset_index()

# Add total population per state
state_totals = population_df.groupby('State').size().reset_index(name='StateTotal')
state_stats = pd.merge(state_group, state_totals, on='State')
state_stats['PopulationPercentage'] = (state_stats['PopulationCount'] / state_stats['StateTotal']) * 100
state_stats.drop(columns='StateTotal', inplace=True)

# 6. Output results
print("\n=== Overall Salary Band Statistics ===")
print(overall_stats)

print("\n=== State-wise Salary Band Statistics ===")
print(state_stats)

# Optional: Save to Excel
with pd.ExcelWriter('task/salary_analysis_results.xlsx', engine='openpyxl') as writer:
    overall_stats.to_excel(writer, sheet_name='Overall Stats', index=False)
    state_stats.to_excel(writer, sheet_name='State Stats', index=False)
