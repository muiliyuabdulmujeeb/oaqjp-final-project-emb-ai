import requests
import json

def emotion_detector(text_to_analyse: str):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url= URL, headers= header, json= input_json)
    response_dict = json.loads(response.text)
    response_dict_emotion = response_dict["emotionPredictions"][0]["emotion"]
    reversed_response_dict_emotion = {v: k for k, v in response_dict_emotion.items()}
    to_return = {
        'anger': response_dict_emotion['anger'],
        'disgust': response_dict_emotion['disgust'],
        'fear': response_dict_emotion['fear'],
        'joy': response_dict_emotion['joy'],
        'sadness': response_dict_emotion['sadness'],
        'dominant_emotion': reversed_response_dict_emotion[max(response_dict_emotion.values())]
    }
    return to_return

"""
{"emotionPredictions":[
    {"emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}, "target":"",
    "emotionMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"}, "emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}}]}],
     "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}} """