from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app:
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    test_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    preds = formatted_response['emotionPredictions'][0]['emotion']
    emo = max(preds, key + preds.get)
    return "For the given statement, the system response is {}. The dominant emotion: {}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)