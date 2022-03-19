import tweepy
import emoji
import os, re

class GetTweet:

    def __init__(self, limit):
        # デフォルトパラメータの設定
        self.exclude_retweet = "-is:retweet"
        self.max_results = 100
        self.sort_order = "recency"
        self.limit = limit
    
    def get_tweets(self, word, begin_time, end_time):
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
            begin_time=begin_time,
            end_time=end_time
        )

        tweets = []
        txt = ""
        for i, tweet in enumerate(paginator.flatten(limit=self.limit)):
            # URLを含むツイートを除外
            pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
            # ハッシュタグを2個以上含むツイートを除外
            hashtag_cnt = tweet.text.count('#')
            # 絵文字を3個以上含むツイートを除外
            emoji_cnt = sum([1 if char in emoji.UNICODE_EMOJI else 0 for char in tweet.text])
            if not re.findall(pattern, tweet.text) \
                and hastag_cnt <= 1 \
                and emoji_cnt <= 2:
                tweets.append({
                    'author_id': tweet.author_id,
                    'created_at': tweet.created_at,
                    'text': tweet.text
                })
                txt += f"====={str(i).zfill(3)}==========================\n"
                txt += tweet.text
                txt += "\n\n"

        with open(f"/workspace/opt/api/tweets/tweet_{word}_{begin_time}_{end_time}.txt", mode="w") as f:
            f.write(txt)
        
        return tweets
        