import tweepy
import datetime as dt
import sys, re, os, json

class GetTweet:
    def main(self, search_word):
        #Twitterオブジェクトの生成
        bearer = os.environ.get('BEARER_TOKEN')
        api = tweepy.Client(bearer)

        # デフォルトパラメータの設定
        exclude_retweet = "-is:retweet"

        # パラメータの設定
        query = f"{search_word} {exclude_retweet}"
        max_results = 100
        sort_order = "recency"
        limit = 10000
        criterion_YYYY = 2022
        criterion_MM = 4
        criterion_DD = 2
        length = 3

        for i in range(length):
            date = str(
                (dt.datetime(criterion_YYYY, criterion_MM, criterion_DD) \
                + dt.timedelta(days=i)).date()
            )
            begin_time = f"{date}T00:00:00Z"
            end_time = f"{date}T23:59:59Z"
            paginator = tweepy.Paginator(
                api.search_recent_tweets,
                query=query,
                max_results=max_results,
                sort_order=sort_order,
                start_time=begin_time,
                end_time=end_time,
                tweet_fields="author_id,conversation_id,created_at"
            )

            json_dict = {}
            for i, tweet in enumerate(paginator.flatten(limit=limit)):
                json_dict[tweet.id] = {
                    "author_id": tweet.author_id,
                    "conversation_id": tweet.conversation_id,
                    "text": tweet.text,
                    "created_at": str(tweet.created_at)
                }

            search_word_replaced = search_word.replace(" ", "_")
            os.makedirs(f"/workspace/opt/tweets/{search_word_replaced}", exist_ok=True)
            with open(f"/workspace/opt/tweets/{search_word_replaced}/{date}.json", mode="w") as f:
                json.dump(json_dict, f, ensure_ascii=False)

if __name__ == '__main__':
    li_word1 = ['aupay', 'aupay クーポン', 'aupayマーケット', 'd払い', '楽天ペイ']
    li_word2 = ['ahamo', 'povo', 'linemo', '楽天モバイル']
    for word in li_word2:
        print("word: ", word)
        instance = GetTweet()
        instance.main(word)