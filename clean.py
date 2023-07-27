import pandas as pd
import numpy as np
from pandasql import sqldf

# Read in Data files
country_land = pd.read_csv('data/country_land.csv')
land_use_df = pd.read_csv('data/global-land-use-since-10000bc.csv')

# Pivot the dataframe to turn the 'Entity' values into columns
pivoted_df = land_use_df.pivot(index='Year', columns='Entity', values='area_aggregated_categories')

# Reset the index
pivoted_df.reset_index(inplace=True)

# Filter out the rows where 'Year' is before -2000
filtered_df = pivoted_df[pivoted_df['Year'] >= -2000].copy()

# Add 'Entity' and 'Code' columns
filtered_df.loc[:, 'Entity'] = 'World'
filtered_df.loc[:, 'Code'] = 'OWID_WRL'

# Reorder the columns
filtered_df = filtered_df[['Entity', 'Code', 'Year', 'Cropland', 'Pasture', 'Permanent ice', 'Semi-natural land', 'Urban', 'Villages', 'Wild barren land', 'Wild woodlands']]


# Display the first few rows of the filtered dataframe
filtered_df.head()

# Perform an outer join to include all data from both dataframes
clean_combined = pd.merge(country_land, filtered_df, how='outer', on=['Entity', 'Code', 'Year'])

# Display the first few rows of the final dataframe
clean_combined.head()

#output
clean_combined.to_csv('data/clean_combined.csv')