# Requests is library to send HTTP requests and fetch web page content
import requests 

# BeautifulSoup is a library to parse HTML content
from bs4 import BeautifulSoup 

# Pandas is a library to handle and organize data in DataFrame format
import pandas as pd


# Define the headers and the website link to scrape
# The 'user-agent' headers are specific to your system. This helps mimic a browser.
#HEADERS = {
#    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
#}

# Website link
url = "https://en.wikipedia.org/wiki/List_of_largest_French_companies"


def scrape_wikepedia_table():
    """ Methode that scrape the data from HTML tables"""

    # Sends the GET request to the URL with the 'user-agent' header set
    response = requests.get(url) #headers=HEADERS

    # Verfy if response if oK
    if response.status_code == 200:
        # Parses the HTML content of the response using BeautifulSoup with the 'html.parser' to create a BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find table with the class "wikitable sortable"
        table = soup.find("table", class_="wikitable sortable")
        table_rows = table.find_all("tr")
        
        # Use list comprehension to get the headers
        tables_headers = [header.text.strip() for header in table_rows[0].find_all("th")]
        
        # Using slicing to remove the header row from the list
        table_values = table_rows[1:]
        # list of rows values
        data_rows = [row.find_all("td") for row in table_values]

        # Define a list to store row values
        list_values = []
        # Loop to retrieve the row values
        for i in range(len(data_rows)):
            # Define a variable that contains the row for processing
            row = data_rows[i]
            row_values = [element.text.strip() for element in row]

            # Add cleaned values to the list
            list_values.append(row_values)

    # Put the data into a DataFrame
    data = pd.DataFrame(data=list_values, columns=tables_headers) 
    
    # Save data into csv file
    data.to_csv("largest-companies-in-french.csv", index=False, encoding="utf-8")   

    return data



if __name__ == "__main__":
    data = scrape_wikepedia_table()
    print(data)