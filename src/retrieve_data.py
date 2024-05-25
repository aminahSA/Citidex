import requests
from bs4 import BeautifulSoup 
import pandas as pd


# Base URL for the API
base_url = "https://api.census.gov/data/2022/acs/acs1/subject"

# Define the parameters for the API request
params = {
    'get': 'NAME,S1901_C01_012E',  # 'NAME' for county name, 'S1901_C01_012E' for median household income estimate
    'for': 'county:*',              # Get data for all counties
    'in': 'state:*',                # Get data for all states
    'key': 'ad02a17e076b923ee25e0d3d7a8cb8fa32e7ead7' # Census API key
}

# Make the API request
response = requests.get(base_url, params=params)
response.raise_for_status()  # Check for request errors

# Parse the JSON response
data = response.json()

# Convert the response to a DataFrame
columns = data[0]
rows = data[1:]
df = pd.DataFrame(rows, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('median_income_by_county.csv', index=False)

print("Data retrieved and saved to median_income_by_county.csv")



''' First approach

#URL of Iowa median income page
url = "https://data.census.gov/table/ACSST1Y2022.S1903?g=050XX00US19061"

# Send a request to the webpage
response = requests.get(url)
response.raise_for_status()  # Ensure we notice bad responses

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the rows containing the data
rows = soup.find_all('div', {'class': 'ag-row-odd ag-row-no-focus ag-row ag-row-level-1 ag-row-group ag-row-group-expanded ag-row-position-absolute ag-after-created'})

# Initialize list to hold the extracted data
income_data = []

# Loop through each row and extract the relevant data
for row in rows:
    # Extract the county name and median income
    county_name = row.find('div', {'col-id': lambda x: x and '!!BOXHEAD2!!COLUMN1' in x}).text.strip()
    median_income = row.find('div', {'col-id': lambda x: x and '!!BOXHEAD1!!COLUMN2' in x}).text.strip()
    
    # Append the extracted data to the list
    income_data.append([county_name, median_income])

# Create a DataFrame
df = pd.DataFrame(income_data, columns=['County', 'Median Income'])

# Save the DataFrame to a CSV file
df.to_csv('median_income_by_county.csv', index=False)

print("Data scraped and saved to median_income_by_county.csv")
'''
