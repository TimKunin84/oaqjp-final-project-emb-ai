import requests
import json

def emotion_detector(text_to_analyze):
    # Check if the input is empty or None
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400  # Indicate a bad request
        }

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

        if "emotionPredictions" in response_json and len(response_json["emotionPredictions"]) > 0:
            emotions = response_json["emotionPredictions"][0]["emotion"]

            emotion_scores = {
                'anger': emotions.get('anger', None),
                'disgust': emotions.get('disgust', None),
                'fear': emotions.get('fear', None),
                'joy': emotions.get('joy', None),
                'sadness': emotions.get('sadness', None)
            }

            dominant_emotion = max(emotion_scores, key=lambda k: emotion_scores[k] if emotion_scores[k] is not None else -1)

            return {
                **emotion_scores,
                'dominant_emotion': dominant_emotion,
                'status_code': 200
            }
    
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None,
        'status_code': response.status_code
    }
