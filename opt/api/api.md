
# 対象選択
- api/available_words
    - Request:
    - Response:
        - available_words: list

- api/available_timepoints
    - Request:
        - word: string
    - Response:
        - begin_date: date
        - end_date: date

# 集約
- api/vader_sentiment_agg
    - Request:
        - word: string
        - begin_date: date
        - end_date: date
    - Response:
        - neg: float
        - neu: float
        - pos: float
        - compound: float
        - count: int

- api/bert_sentiment_agg
    - Request:
        - word: string
        - begin_date: date
        - end_date: date
    - Response:
        - neg: float
        - pos: float
        - count: int

- api/pymlask_sentiment_agg

# 時系列
- api/bert_sentiment_seq
- api/vader_sentiment_seq

