"""
country_gpt.py
--------------
Author: Thea Francis
Date: 07/26/2023

This module contains lists of countries categorized by various geographical and demographic criteria. 
These lists can be imported into other Python scripts for use in data analysis, visualization, or other operations 
that require lists of countries. 

The lists are as follows:

1.small_population_countries: List of countries with small populations (Bottom 20).
2.large_population_countries: List of countries with large populations (Top 20).
3.na_countries: List of countries in North America.
4.europe_countries: List of countries in Europe.
5.africa_countries: List of countries in Africa.
6.oceania_countries: List of countries in Oceania.
7.not_countries: List of entities that are not recognized as independent countries.
8.all_countries: List of all countries in the world.

Usage:
- Get the length of a list: `length = len(list_name)`
- Import lists from another module: `from countries import small_population_countries`
- Check if an element is in a list: `element in list_name`


Note: Country names are kept uniform across the lists for consistency. Some country names have been omitted or 
modified to ensure this uniformity. For example: 
"Vatican City (Holy See)" is referred to as "Vatican City", 
and "Micronesia (Federated States of)" is referred to as "Micronesia". 
Countries with ambiguous or multiple names, such as 
"DR Congo", "Congo (Brazzaville)", "Congo (Kinshasa)", "Ivory Coast", and "Taiwan" 
have been removed from the lists.
"""

# List of countries with small populations
small_population_countries = [
    "Vatican City", "Antigua and Barbuda", "Monaco", "Gibraltar", "Tokelau",
    "Nauru", "Saint Barthelemy", "Tuvalu", "Macau", "Sint Maarten",
    "Saint Martin", "Bermuda", "San Marino", "Guernsey", "Anguilla",
    "Montserrat", "Jersey", "British Virgin Islands", "Liechtenstein",
    "Aruba", "Marshall Islands", "American Samoa", "Cook Islands",
    "Saint Pierre and Miquelon", "Saint Kitts and Nevis", "Niue",
    "Cayman Islands", "Wallis and Futuna", "Maldives", "Malta",
    "Grenada", "United States Virgin Islands", "Mayotte",
    "Saint Vincent and the Grenadines", "Barbados",
    "Curacao", "Seychelles", "Palau", "Northern Mariana Islands",
    "Andorra", "Guam", "Isle Of Man", "Saint Lucia",
    "Micronesia", "Singapore", "Tonga", "Dominica",
    "Bahrain", "Kiribati", "Turks and Caicos Islands", "Sao Tome and Principe",
    "Hong Kong", "Martinique", "Faroe Islands", "Guadeloupe", "Comoros",
    "Mauritius", "Reunion", "Luxembourg", "Samoa", "Cape Verde",
    "French Polynesia", "Trinidad and Tobago", "Brunei", "Palestine",
    "Puerto Rico", "Cyprus", "Lebanon", "Gambia", "Jamaica", "Qatar",
    "Falkland Islands", "Vanuatu", "Montenegro", "Bahamas", "Timor Leste",
    "Eswatini", "Kuwait", "Fiji", "New Caledonia", "Slovenia",
    "El Salvador", "Belize", "Djibouti", "North Macedonia", "Rwanda",
    "Burundi", "Equatorial Guinea", "Albania", "Solomon Islands",
    "Armenia", "Lesotho", "Belgium", "Moldova", "Guinea Bissau"
]
# 96 countries in total
# removed "Africa (FAO)", "Asia (FAO)", "Europe (FAO)", "Northern America (FAO)"
# removed "Oceania (FAO)", "South America (FAO)", "World"
# includes "Hong Kong", "Macau", "Singapore"
# 'Vatican City' for 'Vatican City (Holy See)'

# List of countries with large populations (Top 20)
large_population_countries = [
    "China", "India", "United States", "Indonesia", "Pakistan", 
    "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico", 
    "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam", 
    "Turkey", "Iran", "Germany", "Thailand"
]  # Note: "DR Congo" has been removed from the list

# List of countries in North America
na_countries = [
    "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada",
    "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador",
    "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", 
    "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", 
    "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago",
    "United States of America"
]

# List of countries in Europe
europe_countries = [
    "Albania", "Andorra", "Austria", "Belarus", "Belgium", 
    "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", 
    "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", 
    "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", 
    "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", 
    "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", 
    "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", 
    "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", 
    "Ukraine", "United Kingdom", "Vatican City"
]  # Note: "Vatican City (Holy See)" is referred to as "Vatican City"

# List of countries in Oceania
oceania_countries = [
    "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", 
    "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", 
    "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"
]  # Note: "Micronesia (Federated States of)" is referred to as "Micronesia"

# List of non-country entities
not_countries= [
    'Africa', 'Africa (FAO)', 'Americas (FAO)', 'Asia', 'Asia (FAO)', 'Caribbean (FAO)', 'Central America (FAO)', 
    'Central Asia (FAO)', 'Czechoslovakia', 'Democratic Republic of Congo', 'East Timor', 'Eastern Africa (FAO)', 
    'Eastern Asia (FAO)', 'Eastern Europe (FAO)', 'Europe', 'Europe (FAO)', 'European Union (27)', 
    'European Union (27) (FAO)', 'French Polynesia', 'High-income countries', 'Land Locked Developing Countries (FAO)', 
    'Least Developed Countries (FAO)', 'Low Income Food Deficit Countries (FAO)', 'Low-income countries', 
    'Lower-middle-income countries', 'Melanesia', 'Micronesia (FAO)', 'Micronesia (country)', 'Middle Africa (FAO)', 
    'Net Food Importing Developing Countries (FAO)', 'Netherlands Antilles', 'North America', 'Northern Africa (FAO)', 
    'Northern America (FAO)', 'Northern Europe (FAO)', 'Oceania', 'Oceania (FAO)', 'Polynesia', 
    'Small Island Developing States (FAO)', 'South America', 'South America (FAO)', 'South-eastern Asia (FAO)', 
    'Southern Africa (FAO)', 'Southern Asia (FAO)', 'Southern Europe (FAO)', 'Upper-middle-income countries', 
    'Western Africa (FAO)', 'Western Asia (FAO)', 'Western Europe (FAO)', 'World'
]  
# Note: The following entities have been removed - 'Congo', 'Macao', 'USSR', 'Taiwan', 'Sudan (former)', 'Yugoslavia', 
# 'South Korea', 'Serbia and Montenegro', 'Belgium-Luxembourg (FAO)', 'Bermuda', 'Cape Verde', 'Hong Kong', 'North Korea', 
# 'China (FAO)', 'Ethiopia (former)', 'New Caledonia'


all_countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 
    'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
    'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 
    'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
    'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 
    'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 
    'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
    'Comoros', 'Congo',
    'Costa Rica', 'Ivory Coast',
    'Croatia', 'Cuba', 'Cyprus',
    'Czechia', 'Denmark', 'Djibouti', 'Dominica', 
    'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
    'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 
    'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany',
    'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 
    'Guinea-Bissau', 'Guyana', 'Haiti', 'Vatican City',
    'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 
    'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
    'Kazakhstan', 'Kenya', 'Kiribati', 'South Korea', 
    'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho',
    'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 
    'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali',
    'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 
    'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
    'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 
    'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger',
    'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 
    'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay',
    'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 
    'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 
    'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
    'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 
    'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan',
    'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 
    'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand',
    'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 
    'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
    'United Arab Emirates', 'United Kingdom', 'United States', 
    'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',
    'Palestine', 'Yemen', 'Zambia', 'Zimbabwe'
]
# Updated "Congo (Brazzaville)" and "Congo (Kinshasa)" to "Congo" for uniformity.
# Replaced "Cote d'Ivoire" with "Ivory Coast".
# Changed "Holy See" to "Vatican City".
# Removed "Taiwan*" from the list. Note: Taiwan is not included.
# Replaced "Korea, South" with "South Korea".
# Updated "West Bank and Gaza" to "Palestine" for consistency.