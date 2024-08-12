from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command
import time

def search_wallapop(search_term):
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")  # Run without sandboxing
    options.add_argument("--disable-dev-shm-usage")  # Disable dev-shm usage
    
    # Path to chromedriver executable
    service = Service('/opt/homebrew/bin/chromedriver')  # Replace with the path to your chromedriver
    
    driver = webdriver.Chrome(service=service, options=options)
    
    url = f"https://es.wallapop.com/app/search?keywords={search_term}&filters_source=quick_filters&latitude=41.391410618737&longitude=2.198727932851&distance=5000"
    driver.get(url)
    
    time.sleep(5)  # Wait for the page to load completely

    items = []

    # Extract item details
    cards = driver.find_elements(By.CLASS_NAME, 'ItemCard')
    for card in cards:
        try:
            title = card.find_element(By.CLASS_NAME, 'ItemCard__title').text.strip()
            price = card.find_element(By.CLASS_NAME, 'ItemCard__price').text.strip()
            image = card.find_element(By.TAG_NAME, 'img').get_attribute('src')
            
            items.append({
                'title': title,
                'price': price,
                'image_url': image,
            })
        except Exception as e:
            print(f"Error extracting data: {e}")
    
    driver.quit()
    return items

if __name__ == "__main__":
    search_term = "bicicleta"  # Replace with your search term
    results = search_wallapop(search_term)
    for item in results:
        print(f"Title: {item['title']}\nPrice: {item['price']}\nImage URL: {item['image_url']}\n")
