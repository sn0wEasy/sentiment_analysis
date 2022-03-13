import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
 

class VaderAnalyzer:

    def vader_analyzer(self, tweets):
        tr = Translator()
        vader_analyzer = SentimentIntensityAnalyzer()
        neg, neu, pos, compound = 0, 0, 0, 0
        for tweet in tweets:
            print("===============================")
            print(tweet['text'])
            try:
                text_en = tr.translate(tweet['text'], src="ja", dest="en").text
            except Exception as e:
                print(e)

            #VADERによる感情分析
            analyzed = vader_analyzer.polarity_scores(text_en)
            neg += analyzed['neg']
            neu += analyzed['neu']
            pos += analyzed['pos']
            compound += analyzed['compound']

        count = len(tweets)
        result = {
            'neg': neg/count,
            'neu': neu/count,
            'pos': pos/count,
            'compound': compound/count,
            'count': count
        }

        return result