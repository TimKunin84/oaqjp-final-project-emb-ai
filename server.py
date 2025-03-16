"""
Flask server for the Emotion Detection API.

This server provides an endpoint to analyze emotions from text input
using the EmotionDetection package.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_api():
    """
    API endpoint to analyze emotions from a given text input.

    Returns:
        JSON response containing emotion scores and the dominant emotion.
        If input text is empty, an error message is returned.
    """
    data = request.json
    if 'text' not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400

    text_to_analyze = data['text']
    emotion_result = emotion_detector(text_to_analyze)

    if emotion_result["dominant_emotion"] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    response = {
        "anger": emotion_result["anger"],
        "disgust": emotion_result["disgust"],
        "fear": emotion_result["fear"],
        "joy": emotion_result["joy"],
        "sadness": emotion_result["sadness"],
        "dominant_emotion": emotion_result["dominant_emotion"]
    }

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return jsonify({"message": formatted_response, "raw_response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
