from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


# Set up Selenium WebDriver
def set_up_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Path to your ChromeDriver
    driver_path = "/usr/local/bin/chromedriver"  # Replace with the path to your chromedriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver


def scrape_dynamic_content(url):
    # Initialize the driver
    driver = set_up_driver()

    try:
        # Open the target URL
        driver.get(url)

        # Wait for the dynamic elements to load (explicit sleep or WebDriverWait can be used)
        time.sleep(5)

        # Locate content on the page (use the appropriate locator for your page structure)
        # Example: Scraping text from an element with class "example-class"
        elements = driver.find_elements(By.CLASS_NAME, "example-class")  # Update class name as per the site structure

        # Extract and print the text from elements
        for element in elements:
            print(element.text)

        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph.text)


    finally:
        # Close the driver
        driver.quit()


# Entry point
if __name__ == "__main__":
    url = "https://www.lawrenceville.org/"  # Replace with your target website's URL
    scrape_dynamic_content(url)