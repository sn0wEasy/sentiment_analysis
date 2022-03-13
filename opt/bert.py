from transformers import AutoModelForSequenceClassification, BertJapaneseTokenizer,pipeline
from googletrans import Translator

# 学習済みモデルの読込み
model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
nlp = pipeline("sentiment-analysis",model=model,tokenizer=tokenizer)

# 日本語の感情分析
text_jp = """
適当なサンプルテキスト
"""
print(nlp(text_jp))

# 英語翻訳語の感情分析
tr = Translator()
text_en = tr.translate(text_jp, src="ja", dest="en").text
print(nlp(text_en))

