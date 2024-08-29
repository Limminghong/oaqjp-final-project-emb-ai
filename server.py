from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    if response is None:
        output = 'Invalid text! Please try again.'
    else:       
        output = f"For the given statement, the system response is 'anger' : {response['anger']}, 'disgust' : {response['disgust']}, 'fear' : {response['fear']}, 'joy' : {response['joy']} and 'sadness' : {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

