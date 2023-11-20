from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup


def get_vacancy_links(url):
    driver = webdriver.Chrome()
    driver.get(url)

    while True:
        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='more-btn']/a"))
            )
            load_more_button.click()
        except (NoSuchElementException, TimeoutException):
            break

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    return [a['href'] for a in soup.find_all('a', class_='vt')]


if __name__ == "__main__":
    test_url = "https://jobs.dou.ua/vacancies/?category=Python"
    test_links = get_vacancy_links(test_url)
    print(f"Found links: {len(test_links)}")
    print("First 5 links:", test_links[:5])
