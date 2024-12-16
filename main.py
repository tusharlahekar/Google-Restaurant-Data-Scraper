from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape_google_restaurants(region):
    driver = webdriver.Chrome()
    driver.get(f"https://www.google.com/search?q=restaurants+in+{region}")

    # Wait for page to load
    time.sleep(5)

    # Scroll down to load more results
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Parse HTML content
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find restaurant elements
    restaurants = soup.find_all('div', {'class': 'g'})

    # Extract data from each restaurant element
    data = []
    for restaurant in restaurants:
        name = restaurant.find('h3').text.strip()
        rating_element = restaurant.find('span', {'class': 'Aq16ib'})
        rating = rating_element.text.strip() if rating_element else 'N/A'
        address_element = restaurant.find('span', {'class': 'LfrN7'})
        address = address_element.text.strip() if address_element else 'N/A'
        phone_element = restaurant.find('span', {'class': 'LfrN7', 'data-attrid': 'kc:/business/phone'})
        phone = phone_element.text.strip() if phone_element else 'N/A'

        data.append({'Name': name, 'Rating': rating, 'Address': address, 'Phone': phone})

    driver.quit()

    return pd.DataFrame(data)

# Example usage
region = "Downtown Toronto"
df = scrape_google_restaurants(region)
df.to_csv('restaurants.csv', index=False)
print("Data scraped and saved to restaurants.csv")
