import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    formatted_res = json.loads(response.text)
    
    if response.status_code == 400:
        preds = None
        emo = None
    elif response.status_code == 500:
        preds = formatted_res['emotionPredictions'][0]['emotion']
        emo = max(preds, key = preds.get)
    return (preds, emo)