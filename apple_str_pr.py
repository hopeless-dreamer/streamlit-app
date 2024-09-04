import streamlit as st 
import pandas as pd
import yfinance as yf

st.title('Котировки компании Apple')
st.write('Данные за последние 10 лет')

apple = yf.Ticker("AAPL")
apple_historical_data = apple.history(period="10y")
apple_historical_data.index=apple_historical_data.index.date
st.bar_chart(data=apple_historical_data, 
             y='Volume',
             y_label='Стоимость компании', 
             color=(88,88,3), 
             horizontal=False, 
             stack=None, 
             width=None, 
             height=None)
st.title('Изменение цены при закрытии торгов')
st.line_chart(apple_historical_data,
              y='Close',
              y_label='Цена на момент закрытия',
              color=(267,205,74),
              width=300,
              height=400)
st.title('Изменение амплитуды торгов в течение дня')
apple_historical_data['ampli']=apple_historical_data['High']-apple_historical_data['Low']   
st.line_chart(apple_historical_data,
              y='ampli',
              y_label='Разность между самым низким и самым высоким предложением в день',
              color=(108,63,99),
              width=300,
              height=600)
st.sidebar.title('Как вы оцениваете динамику компании Apple?')
selected = st.sidebar.feedback(options="faces", key=None, disabled=False)
if selected is not None:
    st.sidebar.markdown(f"Спасибо за информацию, мы её передадим компании!")



 
