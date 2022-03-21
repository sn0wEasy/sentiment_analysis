import pathlib, json

class AvailableWords:

    def create(self):    
        data_paths = pathlib.Path("tweets")
        str_data_dirs = [str(dir).replace("tweets/", "") for dir in data_paths.iterdir()]
        available_words = {
            "sentiment_analyzer": str_data_dirs
        }
        with open("/workspace/opt/json/available_words.json", encoding="utf8", mode="w") as f:
            json.dump(available_words, f, ensure_ascii=False, indent=4)
        
        return available_words


if __name__ == "__main__":
    print(AvailableWords().create())
