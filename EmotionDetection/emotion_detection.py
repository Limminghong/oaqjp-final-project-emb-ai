import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = { "raw_document": { "text": text_to_analyse } }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers=header)

    formatted_response = json.loads(response.text)
    formatted_response = formatted_response['emotionPredictions'][0]

    anger_score = formatted_response['emotion']['anger']
    disgust_score = formatted_response['emotion']['disgust']
    fear_score = formatted_response['emotion']['fear']
    joy_score = formatted_response['emotion']['joy']
    sadness_score = formatted_response['emotion']['sadness']

    emotion_scores = {
                        'anger': anger_score,
                        'disgust': disgust_score,
                        'fear': fear_score,
                        'joy': joy_score,
                        'sadness': sadness_score
                    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    output = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }

    return output