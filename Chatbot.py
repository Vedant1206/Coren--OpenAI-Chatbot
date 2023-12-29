import json
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Make sure to download these resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to load JSON data
def load_data(file_name):
    with open(file_name) as file:
        return json.load(file)

# Main function to handle user interaction
def main():
    print("Welcome to the Gym Bot! Tell me about your fitness goals or ask a question.")

    # Main interaction loop
    while True:
        user_input = input("\nWhat would you like to know? (Type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        # Process user input
        processed_input = process_input(user_input)

        # Determine the relevant JSON file
        json_file = "JSON_data/data.JSON"

        # Load data from the selected JSON file
        data = load_data(json_file)

        # Generate and display response
        response = generate_response(processed_input, data)
        print(response)

# Function to process user input
def process_input(user_input):
    tokens = word_tokenize(user_input.lower())
    filtered_words = [word for word in tokens if word not in stopwords.words('english')]
    return filtered_words

def generate_response(words, data):
    response = ""

    for key in data.keys():
        # Check if the user's words match the category key
        if any(word in key.lower() for word in words):
            category_data = load_json_file_if_needed(data[key])
            if isinstance(category_data, dict):
                response += f"{key} Exercises:\n"
                for exercise, details in category_data.items():
                    response += f"  {exercise}:\n"
                    for detail_key, detail_value in details.items():
                        if isinstance(detail_value, list):  # For list items, such as 'variations'
                            detail_value = ', '.join(detail_value)
                        response += f"    {detail_key.capitalize()}: {detail_value}\n"
            else:
                response += "Data not available for this category.\n"
            response += "\n"  # Add an extra line for spacing between categories

    return response.strip() if response else "I couldn't find specific information related to your query. Could you please specify more?"

def load_json_file_if_needed(file_path_or_data):
    if isinstance(file_path_or_data, str):
        return load_data(file_path_or_data)
    return file_path_or_data

if __name__ == "__main__":
    main()
