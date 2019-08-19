import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Instance created for the Chrome driver
driver = webdriver.Chrome(executable_path = "/Users/stephanie/Downloads/chromedriver")
#driver.open

def scrapy(url):

    # Directing the page to ORS Amazon reviews page
    driver.get(url)
    time.sleep(2)

    # Scrolling pause time and cycle time
    SCROLL_PAUSE_TIME = 1
    CYCLES = 1

    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(SCROLL_PAUSE_TIME * 2)

    # For loop to run until cycles have been ran
    for i in range(CYCLES):
        html.send_keys(Keys.END)
        time.sleep(SCROLL_PAUSE_TIME)

    # Find div with class "review-views"
    # Reviews_view = driver.find_element_by_class_name('review-views')

    # In review_view find div with class "reviews"
    reviews_elem = driver.find_elements_by_class_name("review")

    # Loop into all reviews
    for r in reviews_elem:

        #Get rating from review
        rating = r.find_element_by_class_name('a-icon-alt').get_attribute("innerHTML")
        #print('Rating is:', rating)

        #Get name from review
        name = r.find_element_by_class_name('a-profile-name').text
        #print('Name is:', name)

        #Get dates from review
        date = r.find_element_by_class_name("review-date").text
        #print('Date is:', date)

        #Get titles from review
        title = r.find_element_by_class_name("review-title-content").text
        #print('Title is:', title)

        #Get flavors from review
        flavor = r.find_element_by_class_name("a-size-mini").text
        #print('Flavor is:', flavor)

        #Get descriptions from review
        description = r.find_element_by_class_name("review-text-content").text
        #print('Description is:', description)

        reviews.append([rating, name, date, title, flavor, description])

reviews = []
# To scrape all the pages
# Be sure to check how many pages there are prior to running code and changing "range" as needed
# "Range" for UK Amazon below
#for i in range(1,30):
# "Range" for US Amazon below
for i in range(1,2):
    # United States O.R.S Amazon reviews
    #url = 'https://www.amazon.com/ORS-Rehydration-Flavour-Soluble-Tablets/product-reviews/B0098YY6BI/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(i)
    # United Kingdom O.R.S Amazon reviews
    #url = 'https://www.amazon.co.uk/R-S-Hydration-Electrolyte-Tablets-Blackcurrant/product-reviews/B00NGTCKWS/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(i)
    # United Kingdom Wayk Amazon reviews
    url = 'https://www.amazon.co.uk/WAYK-Energy-Alertness-Flavoured-Tablets/product-reviews/B06XW4GL94/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(i)

    scrapy(url)

# Clean up and close browser once task is completed
driver.close()

header = ['Rating', 'Name', 'Date', 'Title', 'Purchase Info', 'Description']
with open('amazon_reviews.csv', 'wt', newline ='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(i for i in header)
    for j in reviews:
        writer.writerow(j)
