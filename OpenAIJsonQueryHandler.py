import os
from openai import OpenAI
import json

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
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


# Main function
if __name__ == "__main__":
    # Path to your JSON file
    json_file_path = "lawrenceville.json"  # Replace with your file path

    # Load JSON data
    json_data = load_json(json_file_path)
    if json_data:
        # User query
        #user_question = "What is the name of the author in this data?"
        user_question = "tell me about Lawrenceville school?"

        # Ask the LLM
        answer = ask_question_about_json(user_question, json_data)
        print("Answer:", answer)
