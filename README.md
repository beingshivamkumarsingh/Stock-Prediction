# 📊 AI Stock Prediction Dashboard

A web-based stock prediction system built using **FastAPI** and **Deep Learning models (LSTM, RNN, CNN, ANN)**.
It predicts stock prices, compares model performance, and generates trading signals.

---

## 🚀 Features

* 📈 Stock Price Prediction (Apple, Google, Microsoft)
* 🤖 Multiple Models (ANN, LSTM, RNN, CNN)
* 📊 Model Comparison using RMSE
* 🔮 30-Day Future Forecast
* 💹 Buy / Sell / Hold Signal
* 🌐 Interactive Dashboard (HTML, CSS, JS)

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* TensorFlow / Keras
* NumPy, Pandas
* Scikit-learn
* yFinance

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

---

## 📂 Project Structure

```
stock_prediction_project/
│
├── app.py
├── model.py
├── model_signal.py
├── utils.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/beingshivamkumarsingh/Stock-prediction.git
cd Stock-Prediction
```

### 2️⃣ Install dependencies

```
pip install fastapi uvicorn numpy pandas scikit-learn yfinance tensorflow jinja2
```

### 3️⃣ Run the server

```
uvicorn app:app --reload
```

---

## 🌐 Usage

Open your browser and go to:

```
http://127.0.0.1:8000
```

---

## 📊 API Endpoints

* `/predict/{stock}` → Prediction + Forecast
* `/signal/{stock}` → Buy/Sell signal

### Example:

```
/predict/apple
/signal/google
```

---

## ⚠️ Notes

* First run may take time (model training)
* Internet required (for stock data via yFinance)

---

## 🔥 Future Improvements

* Save & reuse trained models
* Add more stocks
* Deploy online (Render / Railway)
* Improve UI (trading dashboard style)

---

## 👨‍💻 Author

**Shivam Kumar Singh**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
# Stock-Prediction
