
# 指定可能対象
- api/available_words
    - Request:
    - Response:
        - available_words: dict
            - Key: word
            - Value: {start_date: date, end_date: date}

# 集約
- api/vader_sentiment_agg
    - Request:
        - start_date: date
        - end_date: date
    - Response:
        - neg: float
        - neu: float
        - pos: float
        - compound: float

- api/bert_sentiment_agg
    - Request:
        - start_date: date
        - end_date: date
    - Response:
        - neg: float
        - pos: float

- api/pymlask_sentiment_agg

# 時系列
- api/bert_sentiment_seq
- api/vader_sentiment_seq

