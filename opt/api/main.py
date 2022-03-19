from logic.analyzer.load_tweet import LoadTweet
from logic.analyzer.bert_analyzer import BertAnalyzer
from logic.analyzer.vader_analyzer import VaderAnalyzer
from logic.analyzer.pymlask_analyzer import PyMLAskAnalyzer

class SentimentAnalyzeAPI:

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
        begin_date = request['begin_date']
        end_date = request['end_date']

        tweet_list = LoadTweet().load_tweet(word, begin_date, end_date)
        # res_bert = BertAnalyzer().bert_analyzer(tweet_list)
        res_vader = VaderAnalyzer().vader_analyzer(tweet_list)
        # res_pymlask = PyMLAskAnalyzer().pymlask_analyzer(tweet_list)

        response = request | {'vader': res_vader}
        return response

if __name__ == '__main__':
    api = SentimentAnalyzeAPI()
    request = {
        'word': 'aupay',
        'begin_date': '2022-03-09',
        'end_date': '2022-03-12',
    }
    response = api.main(request)
    print(response)
