import json

class AvailableWords:    
    def available_words(self):
        with open("/workspace/opt/json/available_words.json") as f:
            json_data = f.read()
            available_words_dict = json.loads(json_data)
            available_words = available_words_dict["sentiment_analyzer"]
        return available_words
