![Rainforest Deforestation](image/Rainforest-deforestation.jpg)

# Global Land Use Data Analyst
### *Project by Thea Francis*

---
## Introduction
Half of the habitable land on our planet (areas free of ice and desert) is used for agriculture. The expanding agricultural landscape is the leading cause of deforestation.

## About the Project
This project aims to show that the majority of agricultural lands are allocated for raising livestock. The project also examines the dynamics of global land use over time, historical land use data, and the habitable land requirements associated with different national diets. The program produces visual representations, revealing trends across various countries and regions over time.


## Running the Program
1. Python 3 is required. This project is written using version 3.10.4.
2. Clone the repo from github.
3. Setup a virtual environment and activate it.
4. To make sure you have all the necessary packages, run
```
"pip install -r requirements.txt". 
```
 The following packages will be required to run the program: 
- pandas, 
- numpy, 
- matplotlib.pyplot, 
- scipy,
- seaborn </br>

To run the "main.ipynb" file, Jupyter Notebook needs to be installed. </br>

5. The program can be run directly by running "main.py" from the script folder. You can also run the "main.ipynb" file from script folder using Jupyter Notebook.



## Project Requirements

The following requirements have been met with this project:

1. **Read and analyze data from Two CSV files.**
- "global-land-use-since-10000bc.csv"
- "cereal_and_land_use_all_years_country.csv". 
- *All data are from ourworldindata.org* 

2. **Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.** </br>
The project involves the merging of the two CSV files. The datasets are cleaned and preprocessed to ensure data usability in "clean.py". The merged file then used to calculate the proportion of total cereals allocated to human food for each country.

3. **Make 3 matplotlib or seaborn visualizations to display your data.** </br>
Three Seaborn Plots are generated as output. The first visualization shows global trends in different land categories. The second visualization illustrates land use patterns by region, and the third presents a time-series analysis of cereal distribution to different uses.

4. **Utilize a virtual environment and include instructions in your README on how the user should set one up.** </br>
This project uses a traditional VENV, it can be used with the included "requirements.txt" file.

5. **Annotate your .py files with well-written comments and a clear README.md (only applicable if you’re not using a jupyter notebook).** </br>
This README file serves the purpose of providing comprehensive guidance to users. 

---
## Data Analysis Conclusions 
Indonedia and Malaysia are the biggest contributors. Combined, they produce 87% of global palm oil. And the deforestation data showin that the tropical forest in Indonesia has been declining over the past 3 decades. 
- The graph 'Top 10 Palm Production Country' shows the golbal trend of top palm producers. 
- The graph 'All other countries in the world combined' shows the percentage Indonesia and Malaysia compare with the all other countries. 
- The graph 'Forest Change in Acres' shows the changes of forest in 30 years of a few different countries. 
- The graph 'Palm oil production trend world wide' shows the world wide trend of palm oil production.
