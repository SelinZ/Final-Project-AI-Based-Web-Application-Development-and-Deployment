import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = headers)
    #return response.text 
    formatted_res = json.loads(response.text)
    preds = formatted_res['emotionPredictions'][0][‘emotion’]
    #return (preds, type(preds))
    return (preds,max(preds, key = preds.get))