import requests
from datetime import datetime

from dotenv import dotenv_values
env_vars = dotenv_values('.env')

BASE_URL = "https://api.openai.com/v1/models"
API_KEY = env_vars['OpenAIKey']

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
    models = list_models()
    sorted_models = sorted(models['data'], key=lambda x: x['created'])
    
    print("Available Models:")
    for i, model in enumerate(sorted_models):
        print(f"{i+1}. {model['id']}")
    
    selected_model = int(input("Select a model (enter the corresponding number): "))
    if 1 <= selected_model <= len(sorted_models):
        model_id = sorted_models[selected_model - 1]['id']
        model_details = get_model_details(model_id)
        
        created_timestamp = int(model_details['created'])
        created_date = datetime.fromtimestamp(created_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        
        # Convert the "created" field in model details to human-readable format
        model_details['created'] = created_date
        
        print("\nModel Details:")
        print(f"Model: {model_details['id']}")
        print(f"Created: {model_details['created']}")
        print(f"Owned By: {model_details['owned_by']}")
        print(f"Root: {model_details['root']}")
        print(f"Parent: {model_details['parent']}")
        print("Permissions:")
        for permission in model_details['permission']:
            print(f"  ID: {permission['id']}")
            print(f"  Created: {permission['created']}")
            print(f"  Allow Create Engine: {permission['allow_create_engine']}")
            print(f"  Allow Sampling: {permission['allow_sampling']}")
            print(f"  Allow Logprobs: {permission['allow_logprobs']}")
            print(f"  Allow Search Indices: {permission['allow_search_indices']}")
            print(f"  Allow View: {permission['allow_view']}")
            print(f"  Allow Fine Tuning: {permission['allow_fine_tuning']}")
            print(f"  Organization: {permission['organization']}")
            print(f"  Group: {permission['group']}")
            print(f"  Is Blocking: {permission['is_blocking']}")
    else:
        print("Invalid selection. Please choose a valid model number.")

