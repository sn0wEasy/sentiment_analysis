from googletrans import Translator
 
tr = Translator()
text = """
適当なサンプルテキスト
"""
result = tr.translate(text, src="ja", dest="en").text
print(result)