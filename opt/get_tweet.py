import tweepy
import datetime as dt
import sys, re, os, json

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
limit = 10000
criterion_YYYY = 2022
criterion_MM = 3
criterion_DD = 11
length = 6

for i in range(length):
    date = str(
        (dt.datetime(criterion_YYYY, criterion_MM, criterion_DD) \
        + dt.timedelta(days=i)).date()
    )
    start_time = f"{date}T00:00:00Z"
    end_time = f"{date}T23:59:59Z"
    paginator = tweepy.Paginator(
        api.search_recent_tweets,
        query=query,
        max_results=max_results,
        sort_order=sort_order,
        start_time=start_time,
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
        
    start_date = start_time.split('T')[0].replace('-', '')
    end_date = end_time.split('T')[0].replace('-', '')
    search_word_replaced = search_word.replace(" ", "_")
    os.makedirs(f"/workspace/opt/tweets/{search_word_replaced}", exist_ok=True)
    with open(f"/workspace/opt/tweets/{search_word_replaced}/{start_time}_{end_time}.json", mode="w") as f:
        json.dump(json_dict, f, ensure_ascii=False)

