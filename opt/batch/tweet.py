import pathlib, json
from analyzer.vader_analyzer import VaderAnalyzer
from tqdm import tqdm

class Tweet:
    def create_tweet(self):
        data_paths = pathlib.Path("tweets")
        json_dict = {}
        for dir in data_paths.iterdir():
            
            # ディレクトリ名から検索単語名取得
            search_word = str(dir).split("/")[-1]
            print(f"検索単語: {search_word}")
            
            dir_paths = pathlib.Path(dir)
            for fname in dir_paths.iterdir():
                
                # ファイル名から断面取得
                timepoint = str(fname).split(".")[0].split("/")[-1]
                print(f"断面: {timepoint}")

                # search_word.jsonからprimary_keyを取得
                with open("/workspace/opt/json/search_word.json", encoding="utf8", mode="r") as f:
                    search_word_json = json.load(f)
                for primary_key, v in search_word_json.items():
                    if v["timepoint"] == timepoint and v["word"] == search_word:
                        search_word_id = primary_key
                        break
                    else:
                        search_word_id = None

                # ツイート取得
                with open(str(fname), encoding="utf8", mode="r") as f:
                    tweets = json.load(f)
                
                # 断面毎の検索単語に関するツイートからjsonを作成
                search_word_data = {}
                for tweet_id, tweet_detail in tweets.items():
                    tweet_data = {
                        tweet_id: {
                            "text": tweet_detail["text"],
                            "author_id": tweet_detail["author_id"],
                            "conversation_id": tweet_detail["conversation_id"],
                            "created_at": tweet_detail["created_at"],
                            "search_word_id": search_word_id
                        }
                    }
                    search_word_data |= tweet_data
                json_dict |= search_word_data

        # json出力
        with open("/workspace/opt/json/tweet.json", encoding="utf8", mode="w") as f:
            json.dump(json_dict, f, ensure_ascii=False, indent=4)

    def create_vader_sentiment(self):
        analyzer = VaderAnalyzer()
        with open("/workspace/opt/json/tweet.json", encoding="utf8", mode="r") as f:
            tweets = json.load(f)
            tweet_sentiment_vader_data = {}
            for k, v in tqdm(tweets.items()):
                # vaderによる感情分析
                tweet_sentiment_vader_data |= {
                    k: analyzer.tweet_vader_analyzer(v["text"])
                }

        # json出力
        with open("/workspace/opt/json/tweet_sentiment_vader.json", encoding="utf8", mode="w") as f:
            json.dump(tweet_sentiment_vader_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Tweet().create_tweet()
    Tweet().create_vader_sentiment()
