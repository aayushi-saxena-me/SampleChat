from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


# Function to scrape content from the website
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract relevant sections (e.g., headings and paragraphs)
        data = ""
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            data += heading.get_text(strip=True) + "\n"
        for paragraph in soup.find_all('p'):
            data += paragraph.get_text(strip=True) + "\n"

        return data
    except Exception as e:
        return str(e)


# API endpoint for chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_question = request.json.get('question')
    website_url = "https://sites.google.com/view/vihaan-saxena"

    # Scrape content from the website
    site_content = scrape_website(website_url)

    # Use a logic to generate response (simple example here)
    if user_question.lower() in site_content.lower():
        return jsonify({"answer": "I found something relevant: " + user_question})
    else:
        return jsonify({"answer": "Sorry, I don't have information on that."})


# Run the application
if __name__ == '__main__':
    app.run(debug=True)