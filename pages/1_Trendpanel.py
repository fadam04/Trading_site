from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Log in as guest (or provide your TradingView credentials)
tv = TvDatafeed()

symbols_list = [
    "XAUUSD", "BTCUSD", "NAS100USD", "GBPJPY"
]

timeframes = [
    ("1m", Interval.in_1_minute),
    ("5m", Interval.in_5_minute),
    ("15m", Interval.in_15_minute),
    ("30m", Interval.in_30_minute),
    ("1h", Interval.in_1_hour),
    ("4h", Interval.in_4_hour),
    ("1d", Interval.in_daily),
    ("1w", Interval.in_weekly)
]

# --- Set default symbol
if 'symbol' not in st.session_state:
    st.session_state['symbol'] = 'XAUUSD'

# --- Dropdown (Selectbox)
selected_symbol = st.selectbox("Select an instrument:", symbols_list, index=symbols_list.index(st.session_state['symbol']) if st.session_state['symbol'] in symbols_list else 0)

# --- Manual input
symbol = st.text_input("Or enter a custom instrument:", value=selected_symbol)

# --- Save to session
if symbol:
    st.session_state['symbol'] = symbol
    st.success(f"Saved: {symbol}")

# --- Fixed exchange
exchange = 'OANDA'

st.title("📊 SMA(200) Trend Status")

for label, tf in timeframes:
    # Fetch data for the selected symbol (via OANDA), specific timeframe, 200 candles
    df = tv.get_hist(symbol=symbol, exchange=exchange, interval=tf, n_bars=200)

    if df is not None and not df.empty and 'close' in df.columns:
        df['sma_200'] = df['close'].rolling(window=200).mean()

        latest_price = df['close'].iloc[-1]
        latest_sma = df['sma_200'].iloc[-1]

        st.session_state['latest_price'] = latest_price

        color = "🟩" if latest_price > latest_sma else "🟥"
        st.write(f"{label}: {color} ({latest_price:.2f} vs SMA {latest_sma:.2f})")
    else:
        st.warning(f"⚠️ No data available for {label} timeframe.")
