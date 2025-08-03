from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_article_links():
    """
    Function to extract article links
    """
    
    # Create an instance of ChromeOptions to customize browser options
    options = webdriver.ChromeOptions()

    # Add an option to suppress Chrome logging messages
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Initialize Chrome driver with the defined options
    navigateur = webdriver.Chrome(options=options)

    # The URL of the site to scrape
    lien = "https://fr.hespress.com/economie"

    # Access the page
    navigateur.get(lien)

    # Wait for the page to fully load
    time.sleep(10) 

    # Set the time limit 
    temps_limite = 1 * 60  # 3 minutes = 180 seconds
    # start time
    debut = time.time()  

    # Scroll the page and wait to load all content
    hauteur_derniere = navigateur.execute_script("return document.body.scrollHeight")  # Get the initial height of the page

    while True:
        # Check if 3 minutes have passed
        if time.time() - debut > temps_limite:
            print("Time's up, stopping the script.")
            break  # Stop execution after 3 minutes

        # Scroll to the bottom of the page
        navigateur.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for the page to fully load
        time.sleep(30)

    #contents = navigateur.find_element(By.TAG_NAME, "article")

    cards = navigateur.find_element(By.CLASS_NAME, "posts-categoy")
    all_cards  = cards.find_elements(By.CLASS_NAME, "overlay")

    liens_news = []

    # Retrieve the links of the downloaded articles
    for i in range(len(all_cards)):
        lien = all_cards[i].find_element(By.TAG_NAME, "a").get_attribute("href")
        liens_news.append(lien)
    return liens_news
# Call function
liens_news = scrape_article_links()
