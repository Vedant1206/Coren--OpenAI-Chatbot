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
        json_file = "data.JSON"

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
    # Iterate over the keys in the data
    for key in data.keys():
        # Check if any of the user's words match the key
        if any(word in key.lower() for word in words):
            # Return the information associated with the matched key
            return "Here's some information about {}: {}".format(key, data[key])

    # If no match is found, provide a default response
    return "I couldn't find specific information related to your query. Could you please specify more?"


if __name__ == "__main__":
    main()
