"""Flask app that exposes an /emotionDetector endpoint and a home page."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("'Emotion Detector") # Instaniate Flask app

@app.route("/emotionDetector")
def emo_detector() :
    """Handle GET /emotionDetector, call emotion_detector(), and render a response."""
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    emotions = {k: v for k, v in response.items() if k != 'dominant_emotion'}

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    dominant = response["dominant_emotion"].strip('"')

    emotions_str = ", ".join([f"'{k}': {v}" for k, v in emotions.items()])
    return (
    f'For the given statement, the system response is {emotions_str}. '
    f'The dominant emotion is <b>{dominant}</b>.'
    )

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

# Set host/port information
if __name__ == "__main__":
    app.run(host='localhost', port=5000)
