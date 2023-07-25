# Global Land Use Data Analyst

This program is designed to provide insights into global land use patterns, covering diverse categories such as agriculture, urbanization, forested areas, and more, for any specific year dating back to 1960. It delivers visual representations showing comparisons and trends in different land use categories across various countries and regions over time. 

## Project Goals

This project was created as a comprehensive resource for exploring the dynamics of land use globally and meets the following project requirements: 

1. **Read TWO data sets in with an API (or use two different APIs that have data you can combine to answer new questions).**
The data sources are the World Bank Open Data API and a second dataset from the Global Forest Watch platform. These datasets were chosen to ensure the comprehensive coverage of different aspects of land use worldwide.

2. **Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.**
The project involves the merging of the World Bank Open Data API dataset and the Global Forest Watch CSV files. The datasets are cleaned and preprocessed to ensure data quality and usability.

3. **Make 3 matplotlib or seaborn (or another plotting library) visualizations to display your data.**
Three Seaborn Plots are generated as output. The first visualization shows global trends in different land use categories. The second visualization illustrates land use patterns by region, and the third presents a time-series analysis of deforestation rates.

4. **Utilize a virtual environment and include instructions in your README on how the user should set one up.**.
This project uses Poetry for environment management. However, a traditional VENV can also be used with the included requirements.txt file.

5. **Annotate your .py files with well-written comments and a clear README.md (only applicable if you’re not using a jupyter notebook).**
This README file serves the purpose of providing comprehensive guidance to users. 

## Setup

This program requires two primary steps for setup: setting up a virtual environment and obtaining an API Key from the World Bank Data API.

### Virtual Environment 

#### Via Poetry
1. Clone the Repository to your local device.
2. Install Poetry to your device. (For more information about poetry check out https://python-poetry.org/ )
3. Open the project folder in terminal and type 
`Poetry Shell`
4. Next, install the required packages from the pyproject.toml file by typing 
`Poetry Install`

#### Via Requirements.txt
1. Clone the Repository to your local device. 
2. Navigate to the project folder with terminal and create a virtual environment.
- Windows
`python -m venv venv`
- Mac/Linux
`python3 -m venv venv`
3. Activate your virtual environment 
- Windows 
`venv\Scripts\activate.bat`
- Mac/Linux
`source venv/bin/activate`
4. Install the requirements.txt file using the following command 
`pip install -r requirements.txt`

### API Key and addition

To utilize this program, you'll need an API key from the World Bank Data API. 

After acquiring the API key, add it to a .env file. In the repository, locate a file named **.env.example**. Paste your API key, without spaces or quotation marks, to the right of the "=" sign, then rename the file to .env.

## Running The Program

1. Activate your virtual environment (as described above)
- For Windows: 
`python program.py`
- For Mac/Linux:
`python3 program.py`

2. You'll be asked to input the year you want to analyze.

3. Upon completion, you'll be presented with three data visualizations reflecting various aspects of global land use."
