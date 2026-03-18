from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.metrics import mean_squared_error

from utils import create_dataset, scale_data
from model import ANN_model, LSTM_model, RNN_model, CNN_model
from model_signal import generate_signal


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ==============================
# STOCK PREDICTION API
# ==============================

@app.get("/predict/{stock}")
def predict(stock: str):

    symbol_map = {
        "apple": "AAPL",
        "google": "GOOGL",
        "msft": "MSFT"
    }

    symbol = symbol_map.get(stock, "AAPL")

    df = yf.download(symbol, period="10y", auto_adjust=True)

    if df is None or df.empty:
        return {"error": "Stock data not available"}

    close = df["Close"].dropna().values.reshape(-1, 1)

    scaled, scaler = scale_data(close)

    X, y = create_dataset(scaled)

    if len(X) == 0:
        return {"error": "Not enough training data"}

    train_size = int(len(X) * 0.8)

    X_train = X[:train_size]
    X_test = X[train_size:]

    y_train = y[:train_size]
    y_test = y[train_size:]

    # =========================
    # ANN MODEL
    # =========================

    ann = ANN_model(X_train.shape[1])
    ann.fit(X_train, y_train, epochs=3, verbose=0)

    ann_pred = ann.predict(X_test)

    ann_rmse = np.sqrt(mean_squared_error(y_test, ann_pred))

    # reshape for deep learning models

    X_train_dl = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_test_dl = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    # =========================
    # LSTM
    # =========================

    lstm = LSTM_model(X_train.shape[1])
    lstm.fit(X_train_dl, y_train, epochs=3, verbose=0)

    lstm_pred = lstm.predict(X_test_dl)

    lstm_rmse = np.sqrt(mean_squared_error(y_test, lstm_pred))

    # =========================
    # RNN
    # =========================

    rnn = RNN_model(X_train.shape[1])
    rnn.fit(X_train_dl, y_train, epochs=3, verbose=0)

    rnn_pred = rnn.predict(X_test_dl)

    rnn_rmse = np.sqrt(mean_squared_error(y_test, rnn_pred))

    # =========================
    # CNN
    # =========================

    cnn = CNN_model(X_train.shape[1])
    cnn.fit(X_train_dl, y_train, epochs=3, verbose=0)

    cnn_pred = cnn.predict(X_test_dl)

    cnn_rmse = np.sqrt(mean_squared_error(y_test, cnn_pred))

    errors = {
        "ANN": float(ann_rmse),
        "LSTM": float(lstm_rmse),
        "RNN": float(rnn_rmse),
        "CNN": float(cnn_rmse)
    }

    best_model = min(errors, key=errors.get)

    # =========================
    # 30 DAY FORECAST
    # =========================

    if len(X_test_dl) == 0:
        return {"error": "Not enough test data"}

    future_days = 30

    last_sequence = X_test_dl[-1]

    future = []

    for i in range(future_days):

        time_step = X_train.shape[1]
        pred = lstm.predict(last_sequence.reshape(1, time_step, 1))

        future.append(float(pred[0][0]))

        last_sequence = np.vstack((last_sequence[1:], pred))

        last_sequence = last_sequence.reshape(60, 1)

    actual = scaler.inverse_transform(
        y_test.reshape(-1, 1)).flatten().tolist()

    predicted = scaler.inverse_transform(
        lstm_pred).flatten().tolist()
    
    future = scaler.inverse_transform(
    np.array(future).reshape(-1,1)
    ).flatten().tolist()

    return {

        "actual": actual[:100],
        "predicted": predicted[:100],
        "errors": errors,
        "best_model": best_model,
        "forecast": future

    }



# ==============================
# BUY / SELL SIGNAL
# ==============================

@app.get("/signal/{stock}")
def signal(stock: str):

    symbol_map = {
        "apple": "AAPL",
        "google": "GOOGL",
        "msft": "MSFT"
    }

    symbol = symbol_map.get(stock, "AAPL")

    df = yf.download(symbol, period="1y", auto_adjust=True)

    if df is None or df.empty:
        return {"signal": "HOLD"}

    signal = generate_signal(df)

    return {"signal": signal}