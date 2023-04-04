from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# create a webdriver instance
driver = webdriver.Chrome()

# navigate to the website
driver.get("http://bdlaws.minlaw.gov.bd/laws-of-bangladesh.html")

# find the ul tag with class "divider-2"
ul_element = driver.find_element(By.CLASS_NAME, "divider-2")

# get all the li tags inside the ul tag
li_elements = ul_element.find_elements(By.TAG_NAME, "li")

# loop through the li tags starting from index 8
for li in li_elements[26:]:
    # find the a tag inside the li tag and click it
    a_element = li.find_element(By.TAG_NAME, "a")
    a_element.click()

    # wait for the table of content to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))

    # get all the tr tags inside the tbody tag
    tbody_element = driver.find_element(By.TAG_NAME, "tbody")
    tr_elements = tbody_element.find_elements(By.TAG_NAME, "tr")

    # create an empty list to store the data
    data_list = []

    # loop through the tr tags
    num_pages_visited = 0

    for tr in tr_elements:
        try:
            # get the 2nd td tag inside the tr tag
            td_element = tr.find_elements(By.TAG_NAME, "td")[1]

            # find the a tag inside the td tag and click it
            a_element = td_element.find_element(By.TAG_NAME, "a")
            a_element.click()

            # wait for the content to appear
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "boxed-layout")))

            # get the title and content of the page
            title = driver.title
            view_full_law_button = driver.find_element(By.CLASS_NAME,"view-full-law-button")
            view_full_law_button.click()
            content = driver.find_element(By.CLASS_NAME, "boxed-layout").text

            # create a dictionary to store the data
            data_dict = {"title": title, "content": content}

            # add the dictionary to the list
            data_list.append(data_dict)

            # increase the count of the number of pages visited
            num_pages_visited += 1
            driver.execute_script("window.history.go(-2)")
            print(title)
        except StaleElementReferenceException:
            WebDriverWait(driver, 10).until(EC.staleness_of(a_element))
            driver.execute_script("window.history.go(-2)")
            print("2",driver.title,li)
            continue
        # go back to the previous page
        # if num_pages_visited == len(tr_elements):
        #     print("Root Page",len(tr_elements),num_pages_visited)
        #     # if this is the last page, go back to the root page
        #     # driver.execute_script("window.history.go(-" + str(num_pages_visited) + ")")          
            
            
        # else:
        #     # WebDriverWait(driver, 10).until(EC.staleness_of(a_element))
        #     # if there are more pages to visit, go back to the previous page         
          
       
       
       
    
# close the webdriver instance
driver.quit()
