# Import necessary libraries for scraping with Selenium

# Allows simulating user actions (clicks, mouse movements, etc.)
from selenium.webdriver import ActionChains 

# Allows using the WebDriver to control a web browser
from selenium import webdriver

# Allows managing the ChromeDriver service (not used here, but may be necessary in some cases)
from selenium.webdriver.chrome.service import Service

# Allows interacting with the operating system, e.g., for managing file paths
import os

# Allows locating elements on the web page
from selenium.webdriver.common.by import By
import time
import pandas as pd


def retrieve_url_page(url):
    """ 
    Method returns the URLs of all pages
    Args:
        url: website link
    Returns: a list of URLs of all pages
    """

    # initialization of the webdriver
    driver = webdriver.Chrome() 
    # open the URL
    driver.get(url)
    # pause for 5 seconds
    time.sleep(5)

    urls_pages = []  # List to store the URLs

    while True:
        time.sleep(10)
        
        # Find the "next page" button
        page_suivante = driver.find_element(By.CLASS_NAME, "p1j2gy66") 
        # Find all elements on the page with the class "l1ovpqvx" 
        next_button = page_suivante.find_elements(By.CLASS_NAME, "l1ovpqvx")[-1]
        # click to navigate to the next page
        next_button.click()
        
        # Retrieve the current URL
        url_actuel = driver.current_url
        
        # Check if the URL is already in the list
        if url_actuel in urls_pages:
            print("URL already present, loop ended.")
            break  # Stop the loop if the URL is duplicated
        
        # Add the URL to the list if it is not a duplicate
        urls_pages.append(url_actuel)

    return urls_pages
