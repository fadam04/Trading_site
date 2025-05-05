# 📊 Trading Panel – Streamlit-based Trading Assistant

This is a simple trading assistant web application built with Python and Streamlit. It helps with basic trend analysis and risk management for traders.

## 🔧 Features

### 1. **Trend Panel**
- Retrieves and displays the SMA(200) trend across multiple timeframes (1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w).
- Compares the current price with the 200-period Simple Moving Average.
- Symbols and timeframes are customizable.
- Data is fetched using the [`tvDatafeed`](https://github.com/StreamAlpha/tvdatafeed) library from TradingView.

### 2. **Position Size Calculator**
- Calculates optimal position size based on your account balance and chosen risk.
- Supports two stop-loss modes:
  - Based on a percentage of the entry price.
  - Based on an exact price level.
- Pulls the latest price from the Trend Panel automatically if available.

## 💡 How to Use

1. Launch the app with Streamlit:
   ```bash
   streamlit run home.py
2. Use the sidebar to navigate between:

Trend Panel: Select or enter an instrument to view trend status.

Position Size Calculator: Enter your balance and risk to calculate position size.

⚙️ Dependencies
streamlit

pandas

matplotlib

tvDatafeed

Install them using:
```
pip install streamlit pandas matplotlib tvDatafeed
```

📎 Example Symbols
Here are some commonly used instrument symbols with tvDatafeed:

Symbol	Exchange	Description
XAUUSD	OANDA	Gold
BTCUSD	BINANCE	Bitcoin
NAS100USD	OANDA	Nasdaq 100 (CFD)
NDX	NASDAQ	Official Nasdaq 100 Index
USTEC	TICKMILL	Nasdaq 100 (alt. name on brokers)

🧠 Author
Created by Földes Ádám András
📧 adamfoldes00@gmail.com
🐙 GitHub: fadam04


