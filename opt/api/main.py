from logic.get_tweet import GetTweet
from logic.bert_analyzer import BertAnalyzer
from logic.vader_analyzer import VaderAnalyzer
from logic.pymlask_analyzer import PyMLAskAnalyzer

class AnalyzeAPI:

    def __init__(self, limit):
        self.limit = limit

    def main(self, request):
        """
        Request: dict
            word: 検索単語
            start_timepoint: 検索期間始点断面
            end_timepoint: 検索期間終点断面

        Response: dict
            word: 検索単語
            start_timepoint: 検索期間始点断面
            end_timepoint: 検索期間終点断面
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
        start_time = request['start_time']
        end_time = request['end_time']

        tweet_dict = GetTweet(limit=self.limit).get_tweets(word, start_time, end_time)
        # res_bert = BertAnalyzer().bert_analyzer(tweet_dict)
        res_vader = VaderAnalyzer().vader_analyzer(tweet_dict)
        # res_pymlask = PyMLAskAnalyzer().pymlask_analyzer(tweet_dict)

        response = request | {'vader': res_vader}
        return response

if __name__ == '__main__':
    api = AnalyzeAPI(limit=1000)
    request = {
        'word': 'apex',
        'start_time': '2022-03-07T00:00:00Z',
        'end_time': '2022-03-12T23:59:59Z',
    }
    result = api.main(request)
    print(result)
