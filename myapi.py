from huggingface_hub import InferenceClient
from secret import APIKEY
class MyAPI:
    def __init__(self):

        self.hf_token=APIKEY

    def sentiment_analysis(self, text):
        self.client = InferenceClient(token=self.hf_token,model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
        response= self.client.text_classification(text)
        return response

    def NER(self, text):
        self.ner_client=InferenceClient(token=self.hf_token,model= "dslim/bert-base-NER")
        response = self.ner_client.token_classification(text)
        return response

    def Emotion(self, text):
        self.emotion_client = InferenceClient(token=self.hf_token,model="j-hartmann/emotion-english-distilroberta-base")
        response = self.emotion_client.text_classification(text)
        return response


