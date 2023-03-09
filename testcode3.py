#


from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the web page containing the HTML table to scrape
url = 'https://hfr.health.gov.ng/facilities/hospitals-search?_token=bKwt6zu4Xch5Bwwp4Py4ZLm5izdLBnHron2Odcij&state_id=1&lga_id=1&ward_id=0&facility_level_id=0&ownership_id=0&operational_status_id=1&registration_status_id=0&license_status_id=0&geo_codes=0&service_type=0&service_category_id=0&facility_name=&entries_per_page=20'

# Fetch the web page content using requests library
page = requests.get(url).text

# Create BeautifulSoup object from HTML
soup = BeautifulSoup(page, 'html.parser')

# Find the table element in the HTML
table = soup.find('table')

# Get the column names from the table header
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# Loop over each row in the table body and store the data in a list of dictionaries
data = []
for tr in table.find_all('tr'):
    row = {}
    for i, td in enumerate(tr.find_all('td')):
        row[headers[i]] = td.text.strip()
    if row:
        data.append(row)

# Create pandas DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Print the resulting DataFrame
print(df)