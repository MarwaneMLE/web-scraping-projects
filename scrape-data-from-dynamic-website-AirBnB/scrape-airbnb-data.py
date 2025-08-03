def scrape_detail_infos(urls_pages):
    """
    This function extracts characteristics from all the pages.
    Args:
        urls_pages: list of page links.
    Returns:
        DataFrame: a DataFrame containing the extracted characteristics.
    """ 

    urls = list(set(urls_pages))

    list_informations = []
    for i in range(len(urls)):
        # Initialize Chrome driver with defined options
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()
        # Open the link specified in the 'lien' variable
        driver.get(urls[i])
        # pause for 10 seconds
        time.sleep(10) 

        # Now extract the content
        #contents = driver.find_element(By.CLASS_NAME, "dmzfgqv")
        time.sleep(10)
        # Extract all the cards
        #cartes = contents.find_elements(By.CLASS_NAME, "g1qv1ctd")

        # Find the element containing the main content
        contenu = driver.find_element(By.CLASS_NAME, "dmzfgqv")

        # Find all the cards inside the content
        cartes = contenu.find_elements(By.CLASS_NAME, "g1qv1ctd")

        list_infos = []
        for i in range(len(cartes)):
            try:
                place = cartes[i].find_element(By.CLASS_NAME, "t1jojoys").text
            except:
                place = None
            try:
                location = cartes[i].find_elements(By.CLASS_NAME, "fb4nyux")[0].text
            except:
                location = None
            #try:
            #    distance = cartes[i].find_element(By.CLASS_NAME, "a8jt5op").text
            #except:
            #    distance=None
            try:
                disponible_periode = cartes[i].find_elements(By.CLASS_NAME, "fb4nyux")[1].find_element(By.CLASS_NAME, "a8jt5op").text
            except:
                disponible_periode = None
            try:
                prix = cartes[i].find_element(By.CLASS_NAME, "_11jcbg2").text
            except:
                prix = None
            try:
                journee_nuit = cartes[i].find_element(By.CLASS_NAME, "_1w7bwz8").text
            except:
                journee_nuit = None
            # unpacking
            try:
                rate = cartes[i].find_element(By.CLASS_NAME, "t1a9j9y7").text.split(",")[0]
            except:
                rate = None
            try:
                num_comment = cartes[i].find_element(By.CLASS_NAME, "t1a9j9y7").text.split(",")[1]
            except:
                num_comment = None

            # list of characteristics
            infos = [place, location, disponible_periode, prix, journee_nuit, rate, num_comment]
            list_infos.append(infos)

        #list_informations.extend(infos)
        #all_info_rows = list(list_informations)
            list_informations.append(list_infos)
        #all_info_rows = list(list_informations)
        # list of variables
        variables = ["place", "location", "disponible_periode", "prix", "journee_nuit", "rate", "num_comment"]

        # create a dataframe
        df = pd.DataFrame(data=list_informations, columns=variables)
        # save the data in a "csv" or "xlsx" file
        df.to_csv("airbnb-offres-maroc.csv", index=False)
        df.to_excel("airbnb-offres-maroc.xlsx", index=False)
        
    return df

time.sleep(30)
# Close the browser session and the opened page
driver.quit()
