import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {"text": text_to_analyze}
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        response_json = response.json()
        
        # Print the response to understand its structure (for debugging)
        print("API Response:", response_json)
        
        # Extract and return the relevant emotion analysis
        if "emotion_predictions" in response_json:
            return response_json["emotion_predictions"]
        else:
            return "Unexpected response structure: " + str(response_json)
    else:
        return f"Error: {response.status_code}, {response.text}"
