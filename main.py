import pandas as pd

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.booking.com/searchresults.pl.html?ss=Polska&ssne=Polska&ssne_untouched=Polska&efdco=1&label=gog235jc-1DCAEoggI46AdIHlgDaLYBiAEBmAEeuAEXyAEM2AED6AEB-AECiAIBqAIDuALX8dOjBsACAdICJDg5YTRiMDRhLTE4MzItNGI5MS1hZjIwLTE0MDA3MmM3ZDI5YdgCBOACAQ&sid=35537ceeb07a63ac4659b5f44dbddc84&aid=397594&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=170&dest_type=country&checkin=2023-07-01&checkout=2023-07-10&group_adults=2&no_rooms=2&group_children=2&age=10&age=10')
sleep(2)
#print(driver.title)

city_table = []
cost_table = []
rating_tab = []
comfort_tab = []

for i in range(1, 2):

    sleep(3)

    if driver.find_element(By.ID, 'onetrust-accept-btn-handler').is_displayed():
        driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

    city = driver.find_elements(By.CSS_SELECTOR, '.b4273d69aa')
    cost = driver.find_elements(By.CSS_SELECTOR, '.fbd1d3018c')
    rating = driver.find_elements(By.CSS_SELECTOR, '.d10a6220b4')
    comfort = driver.find_elements(By.CSS_SELECTOR, "span[class='f9afbb0024']")

    for c in city:
        if c.text != 'Pokaż na mapie':
            city_table.append(c.text)

    for c in cost:
        cost_table.append(int(c.text[:len(c.text) - 2].replace(" ", "")))

    for r in rating:
        rating_tab.append(float(r.text.replace(",", ".")))

    for c in comfort:
        comfort_tab.append(float(c.text[-3:].replace(",", ".")))

    button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Następna strona']")
    button.click()
    sleep(2)


info = list(zip(city_table, cost_table, rating_tab, comfort_tab))

df = pd.DataFrame(info, columns=['City', 'Cost', 'Rating', 'Comfort'])
print(df)
#print(df['Cost'])

sleep(180)