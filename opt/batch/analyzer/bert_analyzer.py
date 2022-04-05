from transformers import AutoModelForSequenceClassification, BertJapaneseTokenizer,pipeline

class BertAnalyzer:

    def word_bert_analyzer(self, tweet_list):
        # 学習済みモデルの読込み
        model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
        tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
        nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

        # 感情分析
        score_neg, score_pos = 0, 0
        tweet_list = [tweet['text'] for tweet in tweet_list]
        analyzed_list = nlp(tweet_list)
        for analyzed in analyzed_list:
            if analyzed['label'] == 'ポジティブ':
                score_pos += analyzed['score']
            elif analyzed['label'] == 'ネガティブ':
                score_neg -= analyzed['score']
        
        count = len(tweet_list)
        result = {
            'neg': score_neg/count,
            'pos': score_pos/count,
            'count': count
        }

        return result


