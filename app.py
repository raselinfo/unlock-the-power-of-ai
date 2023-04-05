password='xiplodzhvjfytbjf'

results = []
for link in links:
    driver.get(link)
    table_body = driver.find_element(By.TAG_NAME,"tbody")
    tr_tags = table_body.find_elements(By.TAG_NAME,"tr")
    title = driver.title
    content = ""
    for tr in tr_tags:
        td_tags = tr.find_elements(By.TAG_NAME,"td")
        if len(td_tags) >= 3:
            a_tag = td_tags[2].find_element(By.TAG_NAME,"a")
            a_tag.click()
            driver.switch_to.window(driver.window_handles[-1])
            view_full_law_button = driver.find_element(By.CLASS_NAME,"view-full-law-button")
            view_full_law_button.click()
            boxed_layout = driver.find_element(By.CLASS_NAME,"boxed-layout")
            content += boxed_layout.text
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    results.append({"title": title, "content": content})

print(results)


# -------------
# list = list()
# for i in pageList:
#        url = i....
#        list.append(url)
# for index in list:
#     your code