# i have this website "http://bdlaws.minlaw.gov.bd/laws-of-bangladesh.html" in this website it has a ul tag with "divider-2" class name.
# and inside this ul there has 49 li tags and inside li tag it has "a" tag. So now i want to click all of link after 8 li tags. after click the links new page come with a table of content. inside the table it's has <tbody> tag and insid that <tbody> tag there is a "<a"> tag of third <td> of <tabody>. so i want again clik all the link inside third number of td of <tbody>. 
# after clik the link there are new page open. and in this page here a "<a>" tag with class "view-full-law-button", and i want to click that link . after click i want to read all the content of the  div of "boxed-layout" class and also create an array of object. here are the example of the array.
# [
# 	{
# 	title: "বাংলা ভাষা প্রচলন আইন, ১৯৮৭",
# 	content:ণপ্রজাতন্ত্রী বাংলাদেশের সংবিধানের ৩নং অনুচ্ছেদের বিধানকে পূর্ণরূপে কার্যকর করিবার উদ্দেশ্যে প্রণীত আইন৷

# যেহেতু সংবিধানের ৩ অনুচ্ছেদের বিধানাবলী পূর্ণরূপে কার্যকর করিবার এবং তৎসংক্রান্ত বিষয়ের জন্য বিধান প্রণয়ন করা সমীচীন ও প্রয়োজনীয়;
# সেহেতু এতদ্‌দ্বারা নিম্নরূপ আইন করা হইল:-
# }
	
# ]

# here title will be the html page title content


import requests
from bs4 import BeautifulSoup


url="http://bdlaws.minlaw.gov.bd/laws-of-bangladesh.html"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")

links=[]

ul_tag=soup.find("ul",{"class":"divider-2"})
li_tags=ul_tag.find_all("li")[26:]

for li in li_tags:
    link=li.find("a")["href"]
    links.append(link)




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome

service = Service('/path/to/chromedriver')
driver = Chrome(service=service)
# driver_path = "/path/to/chromedriver"
# driver = webdriver.Chrome(driver_path)

result=[]
for link in links:
    newLink="http://bdlaws.minlaw.gov.bd"+link
    driver.get(newLink)
    table_body = driver.find_element(By.TAG_NAME, "tbody")
    tr_tags = table_body.find_elements(By.TAG_NAME,"tr")

    title=driver.title
    content=""
    
    for tr in tr_tags:
        td_tags = tr.find_elements(By.TAG_NAME, "td")
        if len(td_tags) >= 2:
            a_tag = td_tags[1].find_element(By.TAG_NAME, "a")
            a_tag.click()
            
            # Wait for the new page to load
            # wait = WebDriverWait(driver, 10)
            # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "view-full-law-button")))
            
            driver.switch_to.window(driver.window_handles[-1])
            
            view_full_law_button = driver.find_element(By.CLASS_NAME,"view-full-law-button")
            view_full_law_button.click()
            boxed_layout = driver.find_element(By.CLASS_NAME,"boxed-layout")
            content += boxed_layout.text
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            title=driver.title
            print(title)

        results.append({"title": title, "content": content})

