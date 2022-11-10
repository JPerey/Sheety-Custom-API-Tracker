from datetime import datetime
import requests
import os

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

exercise_stat_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_input = input("What exercise did you do today? ")

exercise_params = {
    "query": f"{user_input}",

}

headers = {
    "x-app-id": f"{APP_ID}",
    "x-app-key": f"{API_KEY}",
}

exercise_response = requests.post(url=exercise_stat_endpoint, json=exercise_params, headers=headers)
user_activity_post = exercise_response.json()["exercises"][0]["user_input"]
calories_post = round(exercise_response.json()["exercises"][0]["nf_calories"])
duration_post = round(exercise_response.json()["exercises"][0]["duration_min"])
current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")


print(f"user input: {user_activity_post}")
print(exercise_response.text)

# Sheety API Stuff

headers= {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

workout = {
    "workout": {
        "date": f"{current_date}",
        "time": f"{current_time}",
        "exercise": f"{user_activity_post.title()}",
        "duration": f"{duration_post}",
        "calories": f"{calories_post}"},

}

sheety_get_endpoint = "https://api.sheety.co/eec27fdcbfd9a3eb7c5570d0b46911a6/myWorkouts100DaysOfCode/workouts"
sheety_post_endpoint = "https://api.sheety.co/eec27fdcbfd9a3eb7c5570d0b46911a6/myWorkouts100DaysOfCode/workouts"

sheety_get_response = requests.get(url=sheety_get_endpoint, headers=headers)
print(sheety_get_response.text)

sheety_post_response = requests.post(url=sheety_post_endpoint, json=workout, headers=headers)
print(sheety_post_response.text)

