import json
import openai

# Set your OpenAI API key
openai.api_key = "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"


# Load the JSON file
def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)  # Load JSON content
        return data
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None


# Generate a response based on the question and JSON data
def ask_question_about_json(question, json_data):
    try:
        # Combine the relevant JSON data and the user's question into a prompt
        prompt = (
            "You are an AI assistant. This is the data:\n\n"
            f"{json.dumps(json_data, indent=2)}\n\n"
            "Based on this data, answer the question:\n"
            f"{question}"
        )

        # Use OpenAI API to generate a response
        response = openai.Completion.create(
            engine="gpt-4",  # Choose your desired model
            prompt=prompt,
            max_tokens=300,  # Adjust token limit as needed
            temperature=0.7  # Control creativity of the response
        )

        # Extract and return the response text
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return None


# Main function
if __name__ == "__main__":
    # Path to your JSON file
    json_file_path = "vihaan-homepage.json"  # Replace with your file path

    # Load JSON data
    json_data = load_json(json_file_path)
    if json_data:
        # User query
        user_question = "What is the name of the author in this data?"

        # Ask the LLM
        answer = ask_question_about_json(user_question, json_data)
        print("Answer:", answer)