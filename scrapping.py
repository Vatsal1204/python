import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

def scrape_products(url):
    print("Scraping product data...")
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch data")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    for item in soup.select('.product-item'):  
        name = item.select_one('.product-name').text.strip()
        price = item.select_one('.product-price').text.strip()
        rating = item.select_one('.product-rating').text.strip()
        products.append({'Name': name, 'Price': price, 'Rating': rating})

    print("Scraped", len(products), "products successfully!")
    with open("products.json", "w") as f:
        json.dump(products, f, indent=4)
    print("Data saved to products.json")

def google_search(query):
    print("Automating Google search...")
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    links = [res.find_element(By.XPATH, "..").get_attribute("href") for res in results[:5]]
    print("Captured", len(links), "results successfully!")
    with open("search_results.json", "w") as f:
        json.dump(links, f, indent=4)
    driver.quit()
    print("Results saved to search_results.json")
def main():
    while True:
        print("\nChoose an option:")
        print("1. Scrape E-commerce Products")
        print("2. Automate Google Search")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            url = input("Enter e-commerce URL: ")
            scrape_products(url)
        elif choice == "2":
            query = input("Enter search query: ")
            google_search(query)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
if __name__ == "__main__":
    main()
