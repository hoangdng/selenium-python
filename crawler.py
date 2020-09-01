from selenium import webdriver
import time
import csv

# Navigate to "Mua bán bất động sản"
driver = webdriver.Chrome("C:/Program Files/Google/Chrome/Application/chromedriver.exe")
url = "https://muaban.net/"
driver.get(url)
time.sleep(1)
driver.find_element_by_xpath('//a[@title="Bất động sản"]').click()
time.sleep(1)

# Define function to get posts' detail in a page


def getPostDetail():
    listPosts = driver.find_elements_by_class_name("list-item__link")
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
            'Image': imageSource,
            'Title': postTitle,
            'Price': price,
            'Location': location
        }
        listItems.append(item)


# Get posts' detail to a list
listItems = []
pages = 2
for page in range(1, pages):
    getPostDetail()
    driver.find_element_by_xpath(
        '//a[contains(text(),' + str(page + 1) + ')]').click()
    time.sleep(1)

# Write data to .csv file
with open('data_crawler.csv', mode='w', encoding="utf-8") as csv_file:
    fieldnames = ['Image', 'Title', 'Price', 'Location']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for item in listItems:
        writer.writerow(item)
