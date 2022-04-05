import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
from tqdm import tqdm


class VaderAnalyzer:
    def __init__(self):
        self.tr = Translator()
        self.vader_analyzer = SentimentIntensityAnalyzer()

    def word_vader_analyzer(self, tweet_list):
        """
        特定単語を含むツイートを一括で分析
        """
        
        neg, neu, pos, compound = 0, 0, 0, 0
        for tweet in tqdm(tweet_list):
            # 英語ツイート時にNoneが返されるので無視する
            try:
                text_en = self.tr.translate(tweet['text'], src='ja', dest='en').text
            except Exception:
                text_en = tweet['text']

            # Vaderによる感情分析
            analyzed = self.vader_analyzer.polarity_scores(text_en)
            neg += analyzed['neg']
            neu += analyzed['neu']
            pos += analyzed['pos']
            compound += analyzed['compound']

        count = len(tweet_list)
        result = {
            'neg': neg/count,
            'neu': neu/count,
            'pos': pos/count,
            'compound': compound/count
        }

        return result
    
    def tweet_vader_analyzer(self, text):
        """
        単一のツイートを分析
        """
        try:
            text_en = self.tr.translate(text, src='ja', dest='en').text
        except Exception:
            text_en = text
        
        # Vaderによる感情分析
        analyzed = self.vader_analyzer.polarity_scores(text_en)
        result = {
            'neg': analyzed['neg'],
            'neu': analyzed['neu'],
            'pos': analyzed['pos'],
            'compound': analyzed['compound']
        }

        return result
