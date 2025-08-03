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
