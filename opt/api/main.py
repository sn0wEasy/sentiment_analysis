from logic.get_tweet import GetTweet
from logic.bert_analyzer import BertAnalyzer
from logic.vader_analyzer import VaderAnalyzer
from logic.pymlask_analyzer import PyMLAskAnalyzer

class AnalyzeAPI:

    def main(self, request):
        """
        Request: dict
            word: 検索単語
            start_time: 検索期間始点
            end_time: 検索期間終点

        Response: dict
            word: 検索単語
            start_time: 検索期間始点
            end_time: 検索期間終点
            bert: dict
                neg: ネガティブスコア
                pos: ポジティブスコア
                count: 集計ツイート数
            vader: dict
                neg: ネガティブスコア
                neu: ニュートラルスコア
                pos: ポジティブスコア
                compound: 複合スコア
                count: 集計ツイート数
        """
        word = request['word']
        start_time = request['start_time']
        end_time = request['end_time']

        tweet_dict = GetTweet().get_tweets(word, start_time, end_time)
        res_bert = BertAnalyzer().bert_analyzer(tweet_dict)
        res_vader = VaderAnalyzer().vader_analyzer(tweet_dict)
        # res_pymlask = PyMLAskAnalyzer().pymlask_analyzer(tweet_dict)

        # response = request | {'bert': res_bert} | {'vader': res_vader} | {'pymlask': res_pymlask}
        response = request | {'bert': res_bert} | {'vader': res_vader}
        return response

if __name__ == '__main__':
    api = AnalyzeAPI()
    request = {
        'word': 'Twitter',
        'start_time': '2022-03-12T00:00:00Z',
        'end_time': '2022-03-12T23:59:59Z',
    }
    result = api.main(request)
    print(result)
