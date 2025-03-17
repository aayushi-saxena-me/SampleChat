import requests
from bs4 import BeautifulSoup

url = "https://sites.google.com/view/vihaan-saxena"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

text_content = soup.get_text()  # Extract all text from the page
print(text_content) 
