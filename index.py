# I have a website called "http://bdlaws.minlaw.gov.bd/laws-of-bangladesh.html". In this website, there is a ul tag with a class name of "divider-2". Inside this ul tag, there are 49 li tags and inside each li tag, there is an "a" tag. Now, I want to click on all of the links after the 8th li tag. When I click on each link, a new page opens with a table of contents. Inside the table, there is a <tbody> tag, and within that <tbody> tag, there are several <tr> tags. I want to click on the <a> tag inside the 2nd <td> tag of each <tr> tag.

# Once I click on each link, a new page opens. Within this new page, there is a <a> tag with a class of "view-full-law-button". I want to click on that link as well. After clicking on the link, I want to read all of the content of the <div> tag with a class of "boxed-layout".

# After reading the content, I want to create an array of objects. Here's an example of what the array would look like:

# [
# {
# title: "বাংলা ভাষা প্রচলন আইন, ১৯৮৭",
# content: "নপ্রজাতন্ত্রী বাংলাদেশের সংবিধানের ৩নং অনুচ্ছেদের বিধানকে পূর্ণরূপে কার্যকর করিবার উদ্দেশ্যে প্রণীত আইন৷ যেহেতু সংবিধানের ৩ অনুচ্ছেদের বিধানাবলী পূর্ণরূপে কার্যকর করিবার এবং তৎসংক্রান্ত বিষয়ের জন্য বিধান প্রণয়ন করা সমীচীন ও প্রয়োজনীয়; সেহেতু এতদ্‌দ্বারা নিম্নরূপ আইন করা হইল:-"
# },
# ...
# ]

# After creating the array of objects, I want to loop through the <tr> tags of the <tbody> tag again. The title for each object in the array will be the title of the HTML page.

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