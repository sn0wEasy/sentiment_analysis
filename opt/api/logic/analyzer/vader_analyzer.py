import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
from tqdm import tqdm


class VaderAnalyzer:

    def vader_analyzer(self, tweet_list):
        tr = Translator()
        vader_analyzer = SentimentIntensityAnalyzer()
        neg, neu, pos, compound = 0, 0, 0, 0
        for tweet in tqdm(tweet_list):
            # 英語ツイート時にNoneが返されるので無視する
            try:
                text_en = tr.translate(tweet['text'], src="ja", dest="en").text
            except Exception as e:
                print(e)
                continue

            #VADERによる感情分析
            analyzed = vader_analyzer.polarity_scores(text_en)
            neg += analyzed['neg']
            neu += analyzed['neu']
            pos += analyzed['pos']
            compound += analyzed['compound']

        count = len(tweet_list)
        result = {
            'neg': neg/count,
            'neu': neu/count,
            'pos': pos/count,
            'compound': compound/count,
            'count': count
        }

        return result