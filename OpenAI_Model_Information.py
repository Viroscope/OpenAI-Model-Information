import json
import requests
from datetime import datetime

from dotenv import dotenv_values

BASE_URL = "https://api.openai.com/v1/models"
API_KEY = "Key"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def list_models():
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to get models: {}".format(response.status_code))

def get_model_details(model_id):
    response = requests.get(f"{BASE_URL}/{model_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to get model details: {}".format(response.status_code))


if __name__ == "__main__":
    try:
        models = list_models()
        
        print("Available Models:")
        for i, model in enumerate(models['data']):
            print(f"{i+1}. {model['id']}")
        
        selected_model_input = input("Select a model (enter the corresponding number): ")
        
        # No messing around here - straight to business.
        selected_model = int(selected_model_input)
        if not 1 <= selected_model <= len(models['data']):
            print("Invalid selection. Did I stutter? Numbers within range.")
            exit()

        model_id = models['data'][selected_model - 1]['id']
        model_details = get_model_details(model_id)

        print("\nModel Details:")
        print(json.dumps(model_details, indent=4)) # Behold the prettified JSON!

    except ValueError:
       print("Numbers, genius. It’s not rocket science.")
    except Exception as e:
       print(f"Caught an oopsie: {str(e)}")