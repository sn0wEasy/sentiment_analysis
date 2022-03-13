import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
 
tr = Translator()
text = """
適当なサンプルテキスト
"""
text_en = tr.translate(text, src="ja", dest="en").text
print(text_en)

#VADERによる感情分析
vader_analyzer = SentimentIntensityAnalyzer()
res = vader_analyzer.polarity_scores(text_en)
print(res)
