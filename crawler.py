from selenium import webdriver
import time
import csv

# navigate to "Mua bán bất động sản"
driver = webdriver.Chrome()
url = "https://muaban.net/"
driver.get(url)
time.sleep(2)
driver.find_element_by_xpath('//a[@title="Bất động sản"]').click()
time.sleep(2)

# Get info off the posts
listPosts = driver.find_elements_by_class_name("list-item__link")
listItems = []
for post in listPosts:
    imageElement = post.find_element_by_class_name("list-item__image")
    imageSource = imageElement.get_attribute("data-src")
    titleElement = post.find_element_by_class_name("list-item__title")
    postTitle = titleElement.text
    try:
        priceElement = post.find_element_by_class_name("list-item__price")
        price = priceElement.text
    except:
        price = None
    try:
        locationElement = post.find_element_by_class_name(
            "list-item__location")
        location = locationElement.text
    except:
        location = None    
    item = {
        'image': imageSource,
        'title': postTitle,
        'price': price,
        'location': location
    }
    listItems.append(item)
print(listItems)
with open('data_crawler.csv', mode='w', encoding="utf-8") as csv_file:
    fieldnames = ['image', 'title', 'price', 'location']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for item in listItems:
        writer.writerow(item)
