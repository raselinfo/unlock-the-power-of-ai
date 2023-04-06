from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import json

driver=webdriver.Chrome()


def scrape(links):
    result=[]
    for index,link in enumerate(links):
        driver.get(link)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
        table_element=driver.find_element(By.TAG_NAME,'tbody')
        tr_elements=table_element.find_elements(By.TAG_NAME,'tr')
        for tr in tr_elements:
            td_elements=tr.find_elements(By.TAG_NAME,'td')
            a_element=td_elements[1].find_element(By.TAG_NAME,'a')
            a_element.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "boxed-layout")))
            view_full_law_button = driver.find_element(By.CLASS_NAME,"view-full-law-button")
            view_full_law_button.click()
            content = driver.find_element(By.CLASS_NAME, "boxed-layout").text
            data_dict={"title":driver.title,"content":content}
            result.append(data_dict)
            driver.execute_script("window.history.go(-2)")  
    return result  
    
result=scrape(['http://bdlaws.minlaw.gov.bd/volume-27.html'])
driver.close()
print(result[0])

def save_to_file(data):
   result_josn= json.dumps(data,ensure_ascii=False)
   with open('result.json','w',encoding="utf-8") as f:
    f.write(result_josn)

save_to_file(result)