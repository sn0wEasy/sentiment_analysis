from analyzer.load_tweet import LoadTweet
from analyzer.bert_analyzer import BertAnalyzer
from analyzer.vader_analyzer import VaderAnalyzer
from analyzer.pymlask_analyzer import PyMLAskAnalyzer
import datetime as dt
import pathlib

class SentimentAnalyzeBatch:

    def main(self, request):
        """
        Request: dict
            word: 検索単語
            begin_date: 検索期間始点断面
            end_date: 検索期間終点断面

        Response: dict
            word: 検索単語
            begin_date: 検索期間始点断面
            end_date: 検索期間終点断面
            count: ヒット件数
            bert: dict
                neg: ネガティブスコア
                pos: ポジティブスコア
            vader: dict
                neg: ネガティブスコア
                neu: ニュートラルスコア
                pos: ポジティブスコア
                compound: 複合スコア
        """
        word = request['word']
        timepoint = request['timepoint']

        tweet_list = LoadTweet().load_tweet(word, timepoint)
        print("Bert processing...")
        res_bert = BertAnalyzer().word_bert_analyzer(tweet_list)
        # print("Vader processing...")
        # res_vader = VaderAnalyzer().word_vader_analyzer(tweet_list)
        # res_pymlask = PyMLAskAnalyzer().pymlask_analyzer(tweet_list)

        # response = request | {'bert': res_bert} | {'vader': res_vader}
        response = request | {'bert': res_bert}
        return response

if __name__ == '__main__':
    batch = SentimentAnalyzeBatch()
    start_date = dt.datetime(2022, 3, 16)
    period = 20
    parent_dir = pathlib.Path('/workspace/opt/tweets')
    words = [str(itr).split('/')[-1] for itr in parent_dir.iterdir()]

    # for i in range(period):
    #     print(f"===== num_iter {i+1} ===============")
    #     csr_date = start_date + dt.timedelta(days=i)
    #     for word in words:
    #         print(f"===== processing word: {word} ===============")
    #         request = {
    #             'word': word,
    #             'begin_date': csr_date,
    #             'end_date': csr_date,
    #         }
    #         response = batch.main(request)
    
    request = {
        'word': 'd払い',
        'timepoint': '2022-03-16',
    }
    response = batch.main(request)

    print(response)
