from pathlib import Path
import json
from datetime import datetime

LOG_DIR = "/workspace/opt/api/logs/"

class LoadTweet:
    def load_tweet(self, word, start_date, end_date):
        search_word_replaced = word.replace(" ", "_")

        target_dir = Path(f"/workspace/opt/tweets/{search_word_replaced}")
        if target_dir.is_dir():
            files = list(target_dir.iterdir())
            tweet_list = []
            for file in files:
                csr_date = file.name.split('T')[0]
                if start_date <= csr_date and csr_date <= end_date:
                    start_time = csr_date + 'T00:00:00Z'
                    end_time = csr_date + 'T23:59:59Z'
                    csr_fpath = f"/workspace/opt/tweets/{search_word_replaced}/{start_time}_{end_time}.json"
                    with open(csr_fpath) as f:
                        tweets = json.load(f)
                        tweet_list += tweets.values()
                    with open(f"{LOG_DIR}/load_{datetime.now()}") as f:
                        f.write(f"{csr_fpath} is loaded.")
            return tweet_list
        else:
            return []

