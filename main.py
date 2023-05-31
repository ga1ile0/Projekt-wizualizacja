import pandas as pd

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.booking.com/searchresults.pl.html?ss=Polska&ssne=Polska&ssne_untouched=Polska&efdco=1&label=Booking-PL-GokG1qZQBGAqiSCE_k2kpgS411092421248%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9067410%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf5EcukO1MOGv2VrE6ywbUM&sid=aa1380238aafa1ecda0d47d7b198ad2a&aid=376384&lang=pl&sb=1&src_elem=sb&src=searchresults&dest_id=170&dest_type=country&checkin=2023-07-01&checkout=2023-07-09&ltfd=1%3A7%3A7-2023%3A1&group_adults=2&no_rooms=2&group_children=2&age=10&sb_travel_purpose=leisure&fbclid=IwAR0iG1OgBR7-uR07H0f2WZ1hf7Isf5JhkWzh41B0WWr4Xo6jx7yR3flGb0s')
sleep(2)

city_table = []
cost_table = []
rating_tab = []
comfort_tab = []


for i in range(1, 41):

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


info = list(zip(city_table, cost_table, rating_tab, comfort_tab))

df = pd.DataFrame(info, columns=['City', 'Cost', 'Rating', 'Comfort'])
print(df)

df.to_csv('2plus2.csv')

#print(df['Cost'])

sleep(580)