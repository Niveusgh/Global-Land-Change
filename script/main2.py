import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load and preprocess data
df = pd.read_csv('data/clean_combined.csv')

# skipped
df['Total Cereal Allocation'] = df[['Cereals allocated to other uses', 'Cereals allocated to animal feed', 'Cereals allocated to human food']].sum(axis=1)
df['Proportion Allocated to Human Food'] = df['Cereals allocated to human food'] / df['Total Cereal Allocation']

# Filter and reshape data for 'World'
df_world = df[df['Entity'] == 'World']
df_world = df_world.melt(id_vars=['Entity', 'Code', 'Year'], 
                         value_vars=['Cropland', 'Pasture', 'Permanent ice', 'Semi-natural land', 'Urban', 'Villages', 'Wild barren land', 'Wild woodlands'], 
                         var_name='Land_type', 
                         value_name='Area_Aggregated_Categories')


# Drop rows with NaN values
df_world = df_world.dropna(subset=['Area_Aggregated_Categories'])


df_world['Year'] = df_world['Year'].astype(int)

# Group and pivot data
df_world = df_world[df_world['Year'] >= 200]
df_world = df_world.groupby(['Year', 'Land_type'])['Area_Aggregated_Categories'].sum().reset_index()
df_world = df_world.pivot(index='Year', columns='Land_type', values='Area_Aggregated_Categories').fillna(0)

# Convert to percentages
df_world = df_world.divide(df_world.sum(axis=1), axis=0) * 100


# Plot chart 1
# Define a custom color palette using hex color codes
custom_palette = {
    'Cropland': '#FF8D85',  # Dark orange
    'Pasture': '#B22222',  # Firebrick
    'Wild barren land': '#FFD700',  # Gold
    'Permanent ice': '#4073FF',  # Light sky blue
    'Wild woodlands': '#064E40',  # Forest green
    'Semi-natural land':'#6ACCBC',        
    'Urban': '#808080', # Gray
    'Villages': '#804000'  # Gray
}
# Create a new figure
plt.figure(figsize=(16, 9))
plt.suptitle('Chart 1', fontsize=20, y=1.03)


# Initialize a variable to store the cumulative sum
cumulative_sum = np.zeros_like(df_world.iloc[:, 0])

# Plot a stacked area chart
for column in df_world.columns:
    plt.fill_between(df_world.index, cumulative_sum, cumulative_sum + df_world[column], color=custom_palette.get(column, 'lightgray'), alpha=0.4)
    cumulative_sum += df_world[column]
    
# Set labels and title
plt.xlabel('Year', fontsize=14)
plt.ylabel('Percentage of Total Land Mass (%)', fontsize=14)
plt.title('Change in Global Land Use Over Time (AD 200 to Present)', fontsize=16)

plt.grid(True)
plt.legend(df_world.columns, loc='upper left')

plt.show()