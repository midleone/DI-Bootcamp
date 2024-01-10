
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.bbc.co.uk/weather/293397"
driver.get(url)

wait = WebDriverWait(driver, 10)

page_source = driver.page_source


driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

weather_data = []

for day in soup.find_all(class_='weather-day'):
    date = day.find(class_='date-class').get_text()  # Update with correct class
    temperature = day.find(class_='temperature-class').get_text()  # Update with correct class
    condition = day.find(class_='condition-class').get_text()  # Update with correct class
    weather_data.append({'date': date, 'temperature': temperature, 'condition': condition})

df = pd.DataFrame(weather_data)