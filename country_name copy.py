"""
Author: Thea Francis 
Date: 07/26/2023

This file, country_name.py, contains lists of countries categorized by various criteria:

1. small_population_countries.
2. large_population_countries.
4. na_countries: List of countries in North America.
5. europe_countries: List of countries in Europe.
6. africa_countries: List of countries in Africa.

# use len(small_population_countries)) for list length

These lists can be imported into other Python scripts for use in data analysis, 
visualization, or other operations that require lists of countries.
"""



# List of countries with small populations
small_population_countries = [
    "Vatican City", "Antigua and Barbuda", "Monaco", "Gibraltar", "Tokelau", 
    "Nauru", "Saint Barthelemy", "Tuvalu", "Macau", "Sint Maarten", 
    "Saint Martin", "Bermuda", "San Marino", "Guernsey", "Anguilla", 
    "Montserrat", "Jersey", "British Virgin Islands", "Liechtenstein", 
    "Aruba", "Marshall Islands", "American Samoa", "Cook Islands", 
    "Saint Pierre And Miquelon", "Saint Kitts And Nevis", "Niue",
    "Cayman Islands", "Wallis And Futuna", "Maldives", "Malta", 
    "Grenada", "United States Virgin Islands", "Mayotte", 
    "Saint Vincent And The Grenadines", "Barbados", "Antigua And Barbuda", 
    "Curacao", "Seychelles", "Palau", "Northern Mariana Islands",
    "Andorra", "Guam", "Isle Of Man", "Saint Lucia", 
    "Micronesia", "Singapore", "Tonga", "Dominica", 
    "Bahrain", "Kiribati", "Turks And Caicos Islands", "Sao Tome And Principe", 
    "Hong Kong", "Martinique", "Faroe Islands", "Guadeloupe", "Comoros", 
    "Mauritius", "Reunion", "Luxembourg", "Samoa", "Cape Verde", 
    "French Polynesia", "Trinidad And Tobago", "Brunei", "Palestine", 
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
# used 'Vatican City' for 'Holy See'

# List of countries with large populations (Top 20)
large_population_countries = [
    "China", "India", "United States", "Indonesia", "Pakistan", 
    "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico", 
    "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam", 
    "Turkey", "Iran", "Germany", "Thailand"
]
# removed "DR Congo" from the list



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
]
# "Vatican City (Holy See)" is used as Vantican City in the dataset


# List of countries in Africa
africa_countries = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", 
    "Burundi", "Cape Verde", "Cameroon", "Central African Republic", 
    "Chad", "Comoros", "Djibouti", "Egypt", "Equatorial Guinea", 
    "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", 
    "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", 
    "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", 
    "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", 
    "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", 
    "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", 
    "Zambia", "Zimbabwe"
]
# removed 'Congo (Brazzaville)', 'Congo (Kinshasa)' from the list
# removed "Ivory Coast" from the list

# List of countries in Oceania
oceania_countries = [
    "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", 
    "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", 
    "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"
]
# Used name "Micronesia" for "Micronesia (Federated States of)"

# list of non-country
not_countries= [
    'Africa',
    'Africa (FAO)',
    'Americas (FAO)',
    'Asia',
    'Asia (FAO)',
    'Caribbean (FAO)',
    'Central America (FAO)',
    'Central Asia (FAO)',
    'Czechoslovakia',
    'Democratic Republic of Congo',
    'East Timor',
    'Eastern Africa (FAO)',
    'Eastern Asia (FAO)',
    'Eastern Europe (FAO)',
    'Europe',
    'Europe (FAO)',
    'European Union (27)',
    'European Union (27) (FAO)',
    'French Polynesia',
    'High-income countries',
    'Land Locked Developing Countries (FAO)',
    'Least Developed Countries (FAO)',
    'Low Income Food Deficit Countries (FAO)',
    'Low-income countries',
    'Lower-middle-income countries',
    'Melanesia',
    'Micronesia (FAO)',
    'Micronesia (country)',
    'Middle Africa (FAO)',
    'Net Food Importing Developing Countries (FAO)',
    'Netherlands Antilles',
    'North America',
    'Northern Africa (FAO)',
    'Northern America (FAO)',
    'Northern Europe (FAO)',
    'Oceania',
    'Oceania (FAO)',
    'Polynesia',
    'Small Island Developing States (FAO)',
    'South America',
    'South America (FAO)',
    'South-eastern Asia (FAO)',
    'Southern Africa (FAO)',
    'Southern Asia (FAO)',
    'Southern Europe (FAO)',   
    'Upper-middle-income countries',
    'Western Africa (FAO)',
    'Western Asia (FAO)',
    'Western Europe (FAO)',
    'World',
    ]
# removed 'Congo','Macao', 'USSR', 'Taiwan', 'Sudan (former)', 'Yugoslavia',     'South Korea',
# removed 'Serbia and Montenegro', 'Belgium-Luxembourg (FAO)','Bermuda','Cape Verde',
# removed 'Hong Kong',   'North Korea',    'China (FAO)',    'Ethiopia (former)',     'New Caledonia',