from mlask import MLAsk
from tqdm import tqdm
import re

class PyMLAskAnalyzer:

    def __init__(self):
        self.emotion_analyzer = MLAsk()

    def pymlask_analyzer(self, tweet_list):
        
        for tweet in tqdm(tweet_list):
            text = re.sub('\n', ' ', tweet.text)
            result = self.emotion_analyzer.analyze(text)

        return result
