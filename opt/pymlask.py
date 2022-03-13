from mlask import MLAsk
from pprint import pprint
emotion_analyzer = MLAsk()

import MeCab, re

text = """
適当なサンプルテキスト
"""

text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
text=re.sub('RT', "", text)
# 改行文字
text=re.sub('\n', " ", text)
res = emotion_analyzer.analyze(text)
pprint(res)
