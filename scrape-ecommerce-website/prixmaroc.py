"""
This project is about scraping data from ecommerce web site
"""

# Import libraries
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd  


# Headers: 'User-Agent' simulates a real browser to avoid restrictions on automated requests.
HEADERS = {
    # Example for Windows: "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

def scrape_product_links(num_pages): 
    """ 
    Extracts product links from multiple pages of the PrixMaroc website.
    
    Args:
        num_pages (int): Number of pages to scrape.
    
    Returns:
        list: A list of extracted product URLs.
    """
    page_links = []  # List to store category page URLs
    
    for i in range(1, num_pages + 1):  
        url = f"http://www.prixmaroc.ma/index.php?route=product/category&path=60_75&page={i}"
        page_links.append(url)

    product_links = []  # List to store individual product URLs

    for page_url in page_links:
        response = requests.get(page_url, headers=HEADERS)
        time.sleep(3)  # Short delay to avoid hammering the server

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            products = soup.find_all("div", class_="product-layout")
            
            for product in products:
                product_tag = product.find("h4").find("a")
                if product_tag:
                    product_links.append(product_tag["href"])

    return product_links


def scrape_prixmaroc(product_links):
    """ 
    Extract product details from the prixmaroc website.

    Args:
        product_links (list): List of product page URLs.
    
    Returns:
        DataFrame: A pandas DataFrame containing product information.
    """
    product_details = []  # List to store product data
    
    for link in product_links:
        response = requests.get(link, headers=HEADERS)
        time.sleep(5)  # Wait to avoid overwhelming the server
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            product_section = soup.find("div", id="content")

            if product_section:  # Make sure the content exists
                # Extract product data
                name = product_section.find("h1").text.strip()
                description = product_section.find("div", class_="tab-content").text.strip()
                
                product_items = product_section.find_all("li")
                if len(product_items) >= 7:  # Ensure list has enough items
                    model = product_items[3].text.strip()
                    availability = product_items[4].text.strip()
                    price_excl_tax = product_items[5].text.strip()
                    price_incl_tax = product_items[6].text.strip()

                    # Add product info to the list
                    product_info = [name, description, model, availability, price_excl_tax, price_incl_tax]
                    product_details.append(product_info)

    # Define column names for the DataFrame
    column_names = ["name", "description", "model", "availability", "price_excl_tax", "price_incl_tax"]
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame(data=product_details, columns=column_names)
    df.to_csv("prix-maroc-laptops.csv", index=False)
    
    return df
