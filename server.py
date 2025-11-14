# Import necessary libraries and emotion_detector ()
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("'Emotion Detector") # Instaniate Flask app

@app.route("/emotionDetector")
def emo_detector() :
    # Retrieve the text to analyze from the request arguments
    text_to_analyse = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyse)
    # Parse the resulting dictionary to seperate the emotions list and dominant emotion
    emotions = {k: v for k, v in response.items() if k != 'dominant_emotion'}
    dominant = response["dominant_emotion"]

    if response["dominant_emotion"] == None:
        return ("Invalid text! Please try again!")

    emotions_str = ", ".join([f"'{k}': {v}" for k, v in emotions.items()])
    return (
    "For the given statement, the system response is {}. "
    "The dominant emotion is <b>{}</b>."
    ).format(emotions_str, dominant.strip('"'))

# Render template route
@app.route("/")
def render_index_page():
    return render_template('index.html')

# Set host/port information
if __name__ == "__main__":
    app.run(host='localhost', port=5000)