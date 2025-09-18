from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector   # <-- make sure this path exists

app = Flask(__name__)

@app.route('/')
def index():
    # Renders your index.html page
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    text_to_analyze = request.values.get('textToAnalyze', '').strip()

    if not text_to_analyze:
        return "No text provided.", 400

    # Call the actual detector function
    result = emotion_detector(text_to_analyze)

    if isinstance(result, dict):
        dominant_emotion = result.get("dominant_emotion", "unknown")
        return f"Dominant emotion: {dominant_emotion}<br><pre>{result}</pre>"
    else:
        return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
