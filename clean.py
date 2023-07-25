import pandas as pd
import numpy as np

## clean data in Olympic_Data.csv and Population.csv (from Kaggle)
#
# Usage: 
# $ python clean.py data/Olympic_Data.csv and data/Population.csv results/clean.csv

# where:
# Olympic_Data.csv    = C:\Users\ahaas.SDDOMAIN\Desktop\Olympic_Data.csv\data
# data/Population     = C:\Users\ahaas.SDDOMAIN\Desktop\Population.csv\data

import pandas as pd
import numpy as np
import select as sql   

# Read in Data files
P1_df = pd.read_csv('data/Olympic_Data.csv')
P2_df = pd.read_csv('data/Population.csv')

# drop unneeded columns
P2_df=P2_df.drop(['Rank', 'Country/Territory', 'Capital', 'Continent'], axis =1)
P1_df=P1_df.drop(['ID', 'Games','Height', 'Weight', 'Team'], axis =1)

# drop olympians that didnt medal
P1_df.dropna(subset = ['Medal'], inplace=True)
#P1_df.head()

# rename columns
P2_df.rename(columns = {'CCA3':'NOC'}, inplace = True)

# converting to number
#year=1960
#while year!=2022:
    #year=str(year)
    #P2_df[year]=P2_df[year].fillna(0)
    #for row in P2_df[year]:
        #row=int(row)
        #new_row=("{:,}".format(row))
        #P2_df[year]=P2_df[year].replace([row],new_row)
    #year=int(year)+1
#P2_df.head()

#P1_df.head()

#num_of_rows = P1_df.shape
#print(num_of_rows)

#identify NOC that is not the same
#P1_df[P1_df['df1']['NOC'].isin(P2_df['df2']['NOC'])]


# merge data sets

output4 = pd.merge(P1_df, P2_df,
                   on= 'NOC',
                   how='outer')

# drop countries that have never won a medal
output4.dropna(subset = ['Medal'], inplace=True)

output4.tail(10)

output4.to_csv('results/clean.csv')