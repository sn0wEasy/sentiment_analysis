import tweepy
import os, re

class GetTweet:

    def __init__(self):
        # デフォルトパラメータの設定
        self.exclude_retweet = "-is:retweet"
        self.max_results = 100
        self.sort_order = "recency"
        self.limit = 1000
    
    def get_tweets(self, word, start_time, end_time):
        # Twitterオブジェクトの生成
        bearer = os.environ.get('BEARER_TOKEN')
        api = tweepy.Client(bearer)

        # 検索ワード作成
        self.query = f"{word} {self.exclude_retweet}"

        paginator = tweepy.Paginator(
            api.search_recent_tweets,
            query=self.query,
            max_results=self.max_results,
            sort_order=self.sort_order,
            start_time=start_time,
            end_time=end_time
        )

        tweets = []
        txt = ""
        for i, tweet in enumerate(paginator.flatten(limit=self.limit)):
            # URLを含むツイートを除外
            pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
            if not re.findall(pattern, tweet.text):
                tweets.append({
                    'author_id': tweet.author_id,
                    'created_at': tweet.created_at,
                    'text': tweet.text
                })
                txt += f"====={str(i).zfill(3)}==========================\n"
                txt += tweet.text
                txt += "\n\n"

        with open(f"/workspace/opt/api/tweets/tweet_{word}_{start_time}_{end_time}.txt", mode="w") as f:
            f.write(txt)
        
        return tweets
        