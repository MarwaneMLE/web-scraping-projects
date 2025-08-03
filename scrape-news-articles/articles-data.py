from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


def scraape_information(list_liens):
    """
    Function to extract information from the provided links
    Args:
        list_liens: list of links
    Returns: dataframe
    """
    # List to store the extracted information from each article
    artcles_informations = []

    # Loop through the list of provided links (here, only the first two)
    for i in range(len(list_liens[:2])):  
        # Initialize a new Chrome browser for each link
        driver = webdriver.Chrome()

        # Access the page using the current link
        driver.get(list_liens[i])
    
        # Pause to allow the page to load
        time.sleep(3)
        
        try:
            # Attempt to retrieve the 'article' element from the page
            articles = driver.find_element(By.TAG_NAME, "article")
        except:
            # If the 'article' element is not found, display an error message
            print("No article found")

        try:
            # Attempt to retrieve the article's category
            categorie = articles.find_element(By.CLASS_NAME, "breadcrumb").find_elements(By.TAG_NAME, "a")[1].text
        except:
            # If the category is not found, assign None
            categorie = None
        
        try:
            # Attempt to retrieve the article's title
            titre = articles.find_element(By.CLASS_NAME, "post-title").text
        except:
            # If the title is not found, assign None
            titre = None
        
        try:
            # Attempt to retrieve the article's date
            date = articles.find_element(By.CLASS_NAME, "date-post").text
        except:
            # If the date is not found, assign None
            date = None

        try: 
            # Attempt to retrieve the article's description
            description = articles.find_element(By.CLASS_NAME, "article-content").text
        except:
            # If the description is not found, assign None
            description = None

        # Gather the article's information in a list
        infos_article = [categorie, titre, date, description]

        # Add this article's information to the main list
        artcles_informations.append(infos_article)

    # Define the column names of the DataFrame
    variables = ["categorie", "titre", "date", "description"]

    # Create a DataFrame 
    df = pd.DataFrame(data=artcles_informations, columns=variables)
    df.to_csv("hespress-aricles.csv", index=False)
    # Return the DataFrame 
    return df
