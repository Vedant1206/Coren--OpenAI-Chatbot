# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionGenerateWeightLossPlan(Action):

    def name(self) -> Text:
        return "action_generate_weight_loss_plan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        goal = tracker.get_slot('goal')
        diet = tracker.get_slot('diet')
        allergy = tracker.get_slot('allergy')

        # Simplified meal plan based on goal, diet, and allergy
        meal_plan = self.generate_meal_plan(goal, diet, allergy)

        dispatcher.utter_message(text=meal_plan)

        return []

    def generate_meal_plan(self, goal, diet, allergy):
        # Placeholder for a real database of meals
        meals_database = {
            'vegan': ['Vegan salad', 'Grilled tofu', 'Vegan curry'],
            'vegetarian': ['Vegetarian lasagna', 'Caprese salad', 'Vegetable stir fry'],
            'high-protein': ['Grilled chicken breast', 'Beef steak', 'Salmon with quinoa']
        }

        # Filter meals based on diet
        available_meals = meals_database.get(diet, [])

        # Avoid allergens - this is a simplified version
        if allergy == 'nuts':
            available_meals = [meal for meal in available_meals if 'nuts' not in meal]
        elif allergy == 'gluten':
            available_meals = [meal for meal in available_meals if 'bread' not in meal]
        elif allergy == 'dairy':
            available_meals = [meal for meal in available_meals if 'cheese' not in meal]

        # Select meals based on the user's goal
        if goal == 'weight loss':
            selected_meals = available_meals[:3]  # Simplified selection logic
        elif goal == 'muscle gain':
            selected_meals = available_meals[-3:]
        else:  # For general fitness or other goals
            selected_meals = available_meals

        meal_plan = "Your meal plan: " + ", ".join(selected_meals)
        return meal_plan


class ActionAdjustMealPlan(Action):

    def name(self) -> Text:
        return "action_adjust_meal_plan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_feedback = tracker.latest_message.get('text')
        original_meal_plan = tracker.get_slot('meal_plan')  # Assuming the original plan is stored in a slot

        # Adjust the meal plan based on feedback
        adjusted_meal_plan = self.adjust_meal_plan_based_on_feedback(user_feedback, original_meal_plan)

        dispatcher.utter_message(text=adjusted_meal_plan)

        return []

    def adjust_meal_plan_based_on_feedback(self, feedback, meal_plan):
        # Placeholder for real logic to adjust meal plan
        if "more protein" in feedback.lower():
            # Logic to add more protein-rich meals
            meal_plan += ", Added protein shake"
        elif "less carbs" in feedback.lower():
            # Logic to reduce carbohydrate-rich meals
            meal_plan += ", Reduced carb meals"
        elif "variety" in feedback.lower():
            # Logic to add more variety
            meal_plan += ", Added new variety meals"
        elif "simpler" in feedback.lower():
            # Logic to simplify the meal plan
            meal_plan += ", Simplified meal recipes"
        # ... additional conditions based on possible feedback
        else:
            meal_plan += ", General adjustments made"

        adjusted_meal_plan = "Your adjusted meal plan: " + meal_plan
        return adjusted_meal_plan

