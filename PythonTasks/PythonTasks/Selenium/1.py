"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = '/path/to/chromedriver'
steam_store_url = 'https://store.steampowered.com/'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(steam_store_url)

search_box = driver.find_element(By.XPATH, '//input[@name="term"]')
search_box.submit()

game_titles = driver.find_elements(By.CLASS_NAME, 'title')
game_names = [title.text for title in game_titles]

for name in game_names:
    print(name)

driver.quit()