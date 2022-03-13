import tweepy
import datetime
import sys, re, os

#Twitterオブジェクトの生成
bearer = os.environ.get('BEARER_TOKEN')
api = tweepy.Client(bearer)

# デフォルトパラメータの設定
exclude_retweet = "-is:retweet"

# パラメータの設定
search_word = " ".join([word for word in sys.argv[1:]])
query = f"{search_word} {exclude_retweet}"
max_results = 100
sort_order = "recency"
limit = 100
start_time = "2022-03-10T00:00:00Z"
end_time = "2022-03-10T23:59:59Z"

paginator = tweepy.Paginator(
    api.search_recent_tweets,
    query=query,
    # expansions="attachments.media_keys",
    max_results=max_results,
    sort_order=sort_order,
    start_time=start_time,
    # end_time=end_time
)

txt = ""
for i, tweet in enumerate(paginator.flatten(limit=limit)):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    if not re.findall(pattern, tweet.text):
        print(f"====={str(i).zfill(3)}==========================")
        print(tweet.text)
        print()
        txt += f"====={str(i).zfill(3)}==========================\n"
        txt += tweet.text
        txt += "\n\n"

now = int(datetime.datetime.now().timestamp())
with open(f"/workspace/opt/tweets/tweet_{now}.txt", mode="w") as f:
    f.write(txt)

