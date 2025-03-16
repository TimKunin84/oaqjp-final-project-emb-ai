from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_api():
    data = request.json
    if 'text' not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400
    
    text_to_analyze = data['text']
    emotion_result = emotion_detector(text_to_analyze)

    response = {
        "anger": emotion_result["anger"],
        "disgust": emotion_result["disgust"],
        "fear": emotion_result["fear"],
        "joy": emotion_result["joy"],
        "sadness": emotion_result["sadness"],
        "dominant_emotion": emotion_result["dominant_emotion"]
    }

    # Formatting the response for display
    formatted_response = f"For the given statement, the system response is 'anger': {response['anger']}, " \
                         f"'disgust': {response['disgust']}, 'fear': {response['fear']}, " \
                         f"'joy': {response['joy']} and 'sadness': {response['sadness']}. " \
                         f"The dominant emotion is {response['dominant_emotion']}."

    return jsonify({"message": formatted_response, "raw_response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
