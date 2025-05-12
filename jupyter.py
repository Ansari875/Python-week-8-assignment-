# covid_tracker.py (or use this in a Jupyter Notebook)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Display plots in Jupyter
# %matplotlib inline  

# Load the dataset
try:
    df = pd.read_csv('covid_global_data.csv')  # Replace with your dataset filename
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Dataset file not found.")

# View first few rows
print(df.head())

# Basic structure and missing values
print("\nData Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# Clean data: Drop rows with missing values (or fill them)
df = df.dropna()

# Convert 'date' to datetime format
df['date'] = pd.to_datetime(df['date'])

# Describe statistics
print("\nBasic Statistics:")
print(df.describe())

# Group by country and get total confirmed cases
confirmed_by_country = df.groupby('country')['confirmed'].sum().sort_values(ascending=False)

# Group by date for global trend
daily_global = df.groupby('date')[['confirmed', 'deaths', 'recovered']].sum().reset_index()

# Top 5 countries by confirmed cases
top5_countries = confirmed_by_country.head(5)
print("\nTop 5 Countries by Confirmed Cases:")
print(top5_countries)

# ================== VISUALIZATIONS ==================

# 1. Line Chart: Global trend of confirmed cases
plt.figure(figsize=(10, 5))
plt.plot(daily_global['date'], daily_global['confirmed'], label='Confirmed', color='blue')
plt.plot(daily_global['date'], daily_global['deaths'], label='Deaths', color='red')
plt.plot(daily_global['date'], daily_global['recovered'], label='Recovered', color='green')
plt.title('Global COVID-19 Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Chart: Top 5 countries by confirmed cases
plt.figure(figsize=(8, 5))
top5_countries.plot(kind='bar', color='orange')
plt.title('Top 5 Countries by Confirmed Cases')
plt.ylabel('Total Confirmed Cases')
plt.xlabel('Country')
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of daily confirmed cases
plt.figure(figsize=(8, 5))
sns.histplot(df['confirmed'], bins=30, kde=True)
plt.title('Distribution of Daily Confirmed Cases')
plt.xlabel('Confirmed Cases')
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Deaths vs Confirmed cases
plt.figure(figsize=(8, 5))
sns.scatterplot(x='confirmed', y='deaths', data=df, alpha=0.5)
plt.title('Deaths vs Confirmed Cases')
plt.xlabel('Confirmed Cases')
plt.ylabel('Deaths')
plt.tight_layout()
plt.show()
