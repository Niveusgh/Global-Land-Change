import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from country_name import *

# Load data
agriculture_data = pd.read_csv('data/habitable-land-needed.csv')
world_map = gpd.read_file('image/ne_10m_admin_0_countries.shp')

# Correct country names
# country_name_corrections = {
#     'United States of America': 'United States',
#     'Republic of the Congo': 'Congo',
#     'United Republic of Tanzania': 'Tanzania',
#     'The Bahamas': 'Bahamas',
#     'Republic of Serbia': 'Serbia',
#     'Tazania': 'Tanzania',
#     'Ivory Coast': "Cote d'Ivoire",
# }

world_map['SOVEREIGNT'] = world_map['SOVEREIGNT'].replace(country_name_corrections)

# Remove leading/trailing spaces
world_map['SOVEREIGNT'] = world_map['SOVEREIGNT'].str.strip()
agriculture_data['Entity'] = agriculture_data['Entity'].str.strip()

# Separate 'World' data
world_data = agriculture_data[agriculture_data['Entity'] == 'World']
country_data = agriculture_data[agriculture_data['Entity'] != 'World']

# Add missing countries

# missing_countries = ['South Sudan', 'Somalia', 'Syria', 'Somaliland', 'Western Sahara',
#                      'Democratic Republic of the Congo', 'Bhutan', 'Kosovo', 'Libya', 
#                      'Sudan', 'Eritrea', 'Liechtenstein', 'Qatar', 'San Marino', 
#                      'Monaco', 'eSwatini', 'Burundi', 'Andorra', 'Brazilian Island', 
#                      'Papua New Guinea', 'Equatorial Guinea', 'Vatican', 'Northern Cyprus', 
#                      'Cyprus No Mans Area', 'Kashmir', 'Southern Patagonian Ice Field', 
#                      'Bir Tawil', 'Antarctica', 'Taiwan', 'Seychelles', 'Marshall Islands', 
#                      'Comoros', 'São Tomé and Principe', 'Singapore', 'Tonga', 'Tuvalu', 
#                      'Nauru', 'Federated States of Micronesia', 'Palau', 'Bahrain', 
#                      'Spratly Islands', 'Bajo Nuevo Bank (Petrel Is.)', 'Serranilla Bank', 
#                      'Scarborough Reef']

missing_countries_df = pd.DataFrame(missing_countries, columns=['Entity'])
missing_countries_df['HALF Index (habitable land area) (Alexander et al. (2016))'] = np.nan
agriculture_data = pd.concat([agriculture_data, missing_countries_df], ignore_index=True)

# Merge dataframes
merged_data = world_map.merge(agriculture_data, how='left', left_on='SOVEREIGNT', right_on='Entity')

# Include 'World' data
world = pd.concat([merged_data, world_data])

# Calculate world average
world_average = world_data['HALF Index (habitable land area) (Alexander et al. (2016))'].values[0]

# Add the title and the description
plt.suptitle("Share of global habitable land needed if everyone had the diet of...", fontsize=14, fontweight='bold')


# Assign color categories
world['color_category'] = np.where(
    world['HALF Index (habitable land area) (Alexander et al. (2016))'].isnull(), 'no_data',
    np.where(world['HALF Index (habitable land area) (Alexander et al. (2016))'] < world_average, 'blue',
    np.where(world['HALF Index (habitable land area) (Alexander et al. (2016))'] <= 99, 'yellow', 'red')))

# Map color categories to actual colors
color_mappings = {'blue': '#96ceb4', 'yellow': '#ff9966', 'red': '#d9534f', 'no_data': '#7f7f7f'}
world['color'] = world['color_category'].map(color_mappings)

# Plot
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
world[world['color_category'] != 'no_data'].geometry.plot(facecolor=world[world['color_category'] != 'no_data']['color'], ax=ax)
world[world['color_category'] == 'no_data'].geometry.plot(facecolor='none', edgecolor='grey', hatch='////', ax=ax)

# Legend
legend_labels = {
    '#96ceb4': 'Less than currently used',
    '#ff9966': 'Greater than currently used',
    '#d9534f': 'Not possible with global land',
    'grey': 'No data'
}
legend_handles = [mpatches.Patch(color=color, label=label, hatch='////' if color == 'grey' else None) for color, label in legend_labels.items()]
plt.legend(legend_handles, legend_labels.values(), title='HALF Index (habitable land area)', loc='lower right')

# Remove x and y axis marks
ax.set_xticks([])
ax.set_yticks([])



plt.show()