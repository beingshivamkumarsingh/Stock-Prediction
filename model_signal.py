import pandas as pd

def generate_signal(df):

    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA50"] = df["Close"].rolling(50).mean()
    
    df = df.dropna()

    # last row
    last = df.iloc[-1:]

    ma20 = last["MA20"].values[0]
    ma50 = last["MA50"].values[0]

    if ma20 > ma50:
        return "BUY"

    elif ma20 < ma50:
        return "SELL"

    else:
        return "HOLD"