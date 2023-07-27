from bokeh.plotting import  figure, output_notebook, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, HoverTool, CustomJS
from bokeh.models.widgets import Select
from bokeh.transform import factor_cmap
from bokeh.layouts import column as bokeh_column
from bokeh.models import TabPanel
from bokeh.models import Legend
from country_name import *
import pandas as pd


# Ensure output_notebook() is called in the same cell
output_notebook()

# Load the dataset
df = pd.read_csv('data/clean1.csv')

# Create 'Proportion Allocated to Animal Feed' and 'Proportion Allocated to Other Uses' columns
df['Total Cereal Allocation'] = df[['Cereals allocated to other uses', 'Cereals allocated to animal feed', 'Cereals allocated to human food']].sum(axis=1)
df['Proportion Allocated to Human Food'] = df['Cereals allocated to human food'] / df['Total Cereal Allocation']
df['Proportion Allocated to Animal Feed'] = df['Cereals allocated to animal feed'] / df['Total Cereal Allocation']
df['Proportion Allocated to Other Uses'] = df['Cereals allocated to other uses'] / df['Total Cereal Allocation']

# Convert proportions to percentages
for column in ['Proportion Allocated to Human Food', 'Proportion Allocated to Animal Feed', 'Proportion Allocated to Other Uses']:
    df[column] *= 100
    


# Filter the DataFrame
df_large_population = df[~df['Entity'].isin(small_population_countries)]

# Get column names
column_names = df_large_population.columns.tolist()

# Remove rows with missing values in relevant columns
df_remove_na = df_large_population.dropna(subset=['Cereals allocated to other uses', 
                             'Cereals allocated to animal feed', 
                             'Cereals allocated to human food', 'Year', 'Entity'])

df_clean = df_remove_na.drop(['Cropland',
 'Pasture',
 'Permanent ice',
 'Semi-natural land',
 'Urban',
 'Villages',
 'Wild barren land',
 'Wild woodlands'], axis=1)

# Convert 'Year' to int
df_clean['Year'] = df_clean['Year'].astype(int)


# Create a list of unique countries
countries = df_clean['Entity'].unique()



# Create a ColumnDataSource for each country
sources = {country: ColumnDataSource(df_clean[df_clean['Entity'] == country]) for country in countries}

# Create the initial figure
p = figure(width=800, height=250, x_axis_type="linear", title=countries[0])
p.xaxis.axis_label = 'Year'
p.yaxis.axis_label = 'Cereal Allocation (%)'

# Define the stack order and colors
stacks = ['Proportion Allocated to Human Food', 'Proportion Allocated to Animal Feed', 'Proportion Allocated to Other Uses']
# Define a custom color palette
colors = ["#FFB6C1", "#9370DB", "#ADD8E6"]
legend_labels = ['Human Food', 'Animal Feed', 'Other Uses']


# Add varea_stack to the plot
renderers = p.varea_stack(stacks, x='Year', color=colors, alpha=0.6, source=sources[countries[0]])

# Create a Legend
legend = Legend(items=[(label, [r]) for label, r in zip(legend_labels, renderers)], location="top_left", click_policy="hide")

# Add the legend to the plot
p.add_layout(legend)


hover = HoverTool(
    tooltips=[
        ("Year", "@Year"),
        ("Human Food (%)", "@{Proportion Allocated to Human Food}"),
        ("Animal Feed (%)", "@{Proportion Allocated to Animal Feed}"),
        ("Other Uses (%)", "@{Proportion Allocated to Other Uses}")
    ]
)
p.add_tools(hover)

# Create a Select widget for country selection
country_select = Select(value=countries[0], options=list(countries))

# Define a CustomJS callback for the Select widget
callback = CustomJS(args=dict(sources=sources, plot=p), code="""
    var country = cb_obj.value;
    plot.title.text = country;
    plot.renderers[0].data_source.data = sources[country].data;
    plot.change.emit();
""")
country_select.js_on_change('value', callback)

# Show the plot and the Select widget
show(bokeh_column(country_select, p))

