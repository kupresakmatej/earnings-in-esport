import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('ESport_Earnings.csv', encoding='ISO-8859-1')  # Replace '/path/to/your/data.csv' with the actual file path

# Convert 'Releaseyear' to datetime if needed
data['Releaseyear'] = pd.to_datetime(data['Releaseyear'], format='%Y')

# Count the occurrences of each genre
genre_counts = data['Genre'].value_counts()

# Plotting
plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar')
plt.title('Distribution of Games by Genre')
plt.xlabel('Genre')
plt.ylabel('Number of Games')
plt.xticks(rotation=45)
plt.show()

# Plotting
plt.figure(figsize=(10, 6))
sns.histplot(data['TotalMoney'], bins=30, kde=False)
plt.title('Distribution of Total Money Across Games')
plt.xlabel('Total Money')
plt.ylabel('Frequency')
plt.show()

# Count the number of games released each year
yearly_counts = data['Releaseyear'].dt.year.value_counts().sort_index()

# Plotting
plt.figure(figsize=(12, 6))
yearly_counts.plot(kind='line', marker='o')
plt.title('Trends in Game Releases Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Games Released')
plt.grid(True)
plt.show()

# Consider 'most popular' as top 20 games by 'TotalMoney'
top_countries = data.nlargest(20, 'TotalMoney')['Top_Country'].value_counts()

# Plotting
plt.figure(figsize=(8, 8))
top_countries.plot(kind='pie', autopct='%1.1f%%')
plt.title('Country Representation for the Most Popular Games')
plt.ylabel('')  # Hide the y-label
plt.show()

# Plotting
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TournamentNo', y='TotalMoney', data=data)
plt.title('Tournaments vs Earnings')
plt.xlabel('Number of Tournaments')
plt.ylabel('Total Earnings')
plt.show()

import plotly.express as px

# Scale the size for visualization purposes
data['Scaled_PlayerNo'] = data['PlayerNo'] * 10  # Adjust multiplier as needed

# Create the bubble chart
fig = px.scatter_geo(data, locations='Top_Country', locationmode='country names',
                     size='Scaled_PlayerNo',  # Use the scaled number
                     color='TournamentNo',  # Or any other variable of interest
                     hover_name='GameName', hover_data=['TotalMoney'],
                     projection='natural earth', title='Impact of Tournaments, Players, and Earnings Globally',
                     size_max=100)  # Adjust the maximum size to make bubbles larger

fig.show()

# Extract unique country names
unique_countries = data['Top_Country'].unique()

# Pretty-print the list of unique countries
print(unique_countries)
