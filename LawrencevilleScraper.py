import requests
from bs4 import BeautifulSoup
import json


# Function to scrape website content
def scrape_website(url):
    try:
        # Send HTTP GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes (e.g., 404, 500)

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract headings and paragraphs
        content = {
            "headings": [],
            "paragraphs": []
        }

        # Get all headings (h1, h2, h3)
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            content['headings'].append(heading.get_text(strip=True))

        # Get all paragraphs
        for paragraph in soup.find_all('p'):
            content['paragraphs'].append(paragraph.get_text(strip=True))

        return content

    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None


# Store scraped data to a JSON file
def store_content_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)  # Store in pretty JSON format
        print(f"Content successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


# Read data back from the JSON file
def read_content_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def answer_question_from_file(question, filename):
    content = read_content_from_file(filename)

    if content:
        # Combine all text into a single searchable string
        combined_text = ' '.join(content['headings'] + content['paragraphs'])

        # Search for the question in the combined text
        if question.lower() in combined_text.lower():
            return "Yes, relevant information is available."
        else:
            return "Sorry, I couldn't find relevant information."
    else:
        return "Content not available."




# Main execution
if __name__ == '__main__':
    #website_url = 'https://www.lawrenceville.org/'  # Replace with your website URL
    website_url = "https://issuu.com/thelawrencevilleschool/docs/underformers_guide_2023_24_single_pages?fr=sZmFjMDYzNDA0MTQ"
    content = scrape_website(website_url)

    if content:
        # Store the scraped content into a JSON file
        file_name = 'lawrenceville_college_counselling.json'
        store_content_to_file(content, file_name)

        # Optionally, read the file back to verify
        loaded_content = read_content_from_file(file_name)
        print("Loaded Content:", loaded_content)

        # Example usage
        response = answer_question_from_file("Lawrenceville", "vihaan-homepage.json")
        print(response)