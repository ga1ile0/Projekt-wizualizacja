import pandas as pd

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# Ta funkcja została stworzona do skrapowania strony booking.com
# argument nr1 -> liczba stron
# argument nr2 -> nazwa pliku do zapisania cvki
# argument nr3 -> link do strony
# argument nr4 -> czy chcesz czekać na koniec skrapowania (domyślnie False)


def web_scrapper(number_of_pages, file_to_save: str, link: str, wait_at_end=False):
    assert isinstance(link, str), 'Link must be string!'
    assert isinstance(file_to_save, str), 'file_to_save must be string!'

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(link)
    sleep(3)

    city_table = []
    cost_table = []
    rating_tab = []
    comfort_tab = []

    for i in range(1, number_of_pages + 1):

        if driver.find_element(By.ID, 'onetrust-accept-btn-handler').is_displayed():
            driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

        sleep(4)

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

    df.to_csv(file_to_save)

    if wait_at_end == True:
        sleep(60)
