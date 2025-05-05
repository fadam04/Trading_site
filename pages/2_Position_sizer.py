import streamlit as st

st.title("📐 Position Sizing Calculator")

balance = st.number_input("Account Balance ($)", value=5000.0, step=50.0)
risk_percent = st.slider("Risk (%)", min_value=0.5, max_value=5.0, value=2.0)

stop_loss_mode = st.radio("Stop Loss mode:", ("Price", "Percentage"))

if stop_loss_mode == "Percentage":
    stop_loss_percent = st.number_input("Stop Loss (%) relative to entry price", value=2.0, step=0.01)
    risk_amount = balance * (risk_percent / 100)
    position_size = risk_amount / (stop_loss_percent / 100)
    st.success(f"📊 Maximum position size: **{position_size:.2f} USD** | Max loss: **{risk_amount:.2f} USD**")
else:
    if 'symbol' in st.session_state and 'latest_price' in st.session_state:
        symbol = st.session_state['symbol']
        symbol = st.text_input("Enter asset name (e.g. GOLD):", value=symbol)
        latest_price = st.session_state['latest_price']

        entry_price = st.number_input("Entry price ($)", value=latest_price, step=0.01)
        stop_loss_price = st.number_input("Stop Loss price ($)", value=(latest_price - 1), step=0.01)

        if symbol:
            st.session_state['symbol'] = symbol

        if entry_price != stop_loss_price:
            risk_amount = balance * (risk_percent / 100)
            risk_per_unit = abs(entry_price - stop_loss_price)
            position_size = risk_amount / risk_per_unit
            position_value_in_usd = position_size * entry_price

            st.success(f"📊 Maximum position size: **{position_value_in_usd:.2f} USD** | Max loss: **{risk_amount:.2f} USD**")
        else:
            st.warning("⚠️ Entry and Stop Loss price cannot be the same.")
    else:
        st.warning("⚠️ Please select a symbol first on the Trend Panel page!")

        entry_price = st.number_input("Entry price ($)", value=100.0)
        stop_loss_price = st.number_input("Stop Loss price ($)", value=98.0)

        if entry_price != stop_loss_price:
            risk_amount = balance * (risk_percent / 100)
            risk_per_unit = abs(entry_price - stop_loss_price)
            position_size = risk_amount / risk_per_unit
            position_value_in_usd = position_size * entry_price

            st.success(f"📊 Maximum position size: **{position_value_in_usd:.2f} USD** | Max loss: **{risk_amount:.2f} USD**")
        else:
            st.warning("⚠️ Entry and Stop Loss price cannot be the same.")
