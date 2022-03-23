import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setting the environment path
os.environ['PATH'] += "/usr/local/bin/chromedriver"
driver = webdriver.Chrome()
driver.get("https://www.netflix.com/in/browse/genre/839338")

# Printing the heading
columns = shutil.get_terminal_size().columns
print("NETFLIX TRAILER AUTOMATION".center(columns))

# Getting the movie name and clicking on the movie
movie_name = driver.find_element(By.CLASS_NAME, "nm-collections-title-name")
Name = movie_name.get_attribute("textContent")
print("The name of the movie is ", Name)
movie_name.click()

# Clicking on the trailer video
video_element = driver.find_element(By.CLASS_NAME, 'additional-video-image-wrapper')
video_element.click()

# Getting the synopsis text
synopsis = driver.find_element(By.CLASS_NAME,'title-info-synopsis')
summary = synopsis.get_attribute("textContent")
print("The synopsis of the moview is - ", summary)

# Getting the actors name
Starring = driver.find_element(By.CLASS_NAME, 'title-data-info-item-list')
actors = Starring.get_attribute("textContent")
print("The actors of this movie is as follows ", actors)
