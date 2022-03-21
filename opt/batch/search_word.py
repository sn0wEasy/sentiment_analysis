import pathlib, json, uuid

class SeaarchWord:
    def create(self):
        data_paths = pathlib.Path("tweets")
        json_dict = {}
        for dir in data_paths.iterdir():
            
            # ディレクトリ名から検索単語名取得
            search_word = str(dir).split("/")[-1]
            
            dir_paths = pathlib.Path(dir)
            for fname in dir_paths.iterdir():
                with open(str(fname), encoding="utf8", mode="r") as f:
                    tweets = json.load(f)
                    # 件数取得
                    count = len(tweets)
                
                # uuid生成
                primary_key = str(uuid.uuid4())
                # ファイル名から断面取得
                timepoint = str(fname).split(".")[0].split("/")[-1]
                
                partial_data = {
                    primary_key: {
                        "timepoint": timepoint,
                        "word": search_word,
                        "count": count
                    }
                }
                json_dict = json_dict | partial_data

        # json出力
        with open("/workspace/opt/json/search_word.json", encoding="utf8", mode="w") as f:
            json.dump(json_dict, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    SeaarchWord().create()
