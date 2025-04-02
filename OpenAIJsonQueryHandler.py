import os
from openai import OpenAI
import json

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Load the JSON file
def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)  # Load JSON content
        return data
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None

def read_file(filename):
    """Reads the content of a text file."""
    with open(filename, 'r') as file:
        return file.read()

def answer_question(content, question):
    """Finds and answers a question from the file content."""
    # Convert content and question to lowercase for case-insensitive matching
    content = content.lower()
    question = question.lower()

    # Provide answers based on simple keyword-based logic
    if "who" in question:
        return "This is likely a question about a person. Here is a text snippet:\n" + content[:200]
    elif "what" in question:
        return "This question is about something specific. Try searching for:\n" + content[:200]
    elif "where" in question:
        return "This might be about a location. Here's the possible relevant part:\n" + content[:200]
    elif "why" in question or "how" in question:
        return "The text's explanation may help answer your 'why' or 'how' question:\n" + content[:200]
    else:
        return "Sorry, I couldn't find a direct answer. Try rephrasing your question."



def ask_question_about_json(question, json_data):
    try:
        # Combine the relevant JSON data and the user's question into a prompt
        prompt = (
            "You are an AI assistant. This is the data:\n\n"
            f"{json.dumps(json_data, indent=2)}\n\n"
            "Based on this data, answer the question:\n"
        )

        response = client.responses.create(
            model="gpt-4o",
            instructions=prompt,
            input= question,
        )

        # Extract and return the response text
        return response.output_text
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

def ask_chatgpt(file_content, question):
    """
    Sends the file content and user question to ChatGPT and returns the response.
    """
    prompt = f"""
The following is a text file content:

{file_content}

Based on this content, answer the following question:
{question}
    """
    try:
        # Use OpenAI's GPT model
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions=prompt,
            input=question,
         )
        return response.output_text
    except Exception as e:
        return f"Error: {e}"


def ask_json():
    # Path to your JSON file
    json_file_path = "lawrenceville.json"  # Replace with your file path

    # Load JSON data
    json_data = load_json(json_file_path)
    if json_data:
        # User query
        # user_question = "What is the name of the author in this data?"
        user_question = "tell me about community wellbeing?"

        # Ask the LLM
        answer = ask_question_about_json(user_question, json_data)
        print("Answer:", answer)

def ask_txt(question):
    # Path to the text file
    filename = "underformer_guide.txt"


    # Read file content
    try:
        content = read_file(filename)

        # Provide an answer
        answer = ask_chatgpt( content,question)
        return answer
    except Exception as e:
        print(f"Error reading file or processing question: {e}")
        return None


# Main function
if __name__ == "__main__":
    #ask_json()
    # Prompt user for the question
    question = "Most Popular Elective Classes this Year"  # what is community wellbeing" #input("Enter your question: ")
    ask_txt(question)

