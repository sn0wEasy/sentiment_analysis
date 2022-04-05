from pathlib import Path
import json
from datetime import datetime
import emoji

LOG_DIR = "/workspace/opt/batch/logs"

class LoadTweet:
    def load_tweet(self, word, timepoint):
        search_word_replaced = word.replace(" ", "_")

        target_dir = Path(f"/workspace/opt/tweets/{search_word_replaced}")
        if target_dir.is_dir():
            files = list(target_dir.iterdir())
            tweet_list = []
            for file in files:
                csr_date = file.name.replace(".json", "")
                if csr_date == timepoint:
                    csr_fpath = f"/workspace/opt/tweets/{search_word_replaced}/{csr_date}.json"
                    with open(csr_fpath) as f:
                        tweets = json.load(f)
                        for tweet in tweets.values():
                            # URLを含むツイートを除外
                            pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
                            # ハッシュタグを2個以上含むツイートを除外
                            hashtag_cnt = tweet.text.count('#')
                            # 絵文字を3個以上含むツイートを除外
                            emoji_cnt = sum([1 if char in emoji.UNICODE_EMOJI else 0 for char in tweet.text])
                            tweet_list += tweet
                    with open(f"{LOG_DIR}/load_{datetime.now().date()}.log", encoding="utf8", mode="a+") as f:
                        f.write(f"{csr_fpath} is loaded.")
            return tweet_list
        else:
            return []

