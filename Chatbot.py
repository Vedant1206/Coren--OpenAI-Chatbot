import json

# Load JSON data
with open('data.json') as file:
    data = json.load(file)

def get_exercise_info(category, exercise):
    try:
        return data[category][exercise]
    except KeyError:
        return "Exercise not found."

# Example of interacting with the bot
user_input_category = "Cardio"
user_input_exercise = "Running"
response = get_exercise_info(user_input_category, user_input_exercise)
print(response)
