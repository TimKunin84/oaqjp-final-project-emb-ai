import requests
import json

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

        # Print API response for debugging
        print("API Response:", json.dumps(response_json, indent=2))

        # Navigate the correct response structure
        if "emotionPredictions" in response_json and len(response_json["emotionPredictions"]) > 0:
            emotions = response_json["emotionPredictions"][0]["emotion"]  # Extract emotions

            # Store emotion scores
            emotion_scores = {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0),
            }

            # Determine the dominant emotion
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Return the formatted response
            return {
                **emotion_scores,
                'dominant_emotion': dominant_emotion
            }
        else:
            return "Unexpected response structure: " + str(response_json)
    else:
        return f"Error: {response.status_code}, {response.text}"
