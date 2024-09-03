import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

st.title('Data analysis application')
st.write('Загрузки CSV-файл')

apple = yf.Ticker("AAPL")

uploaded_file = st.file_uploader('Загрузи файл', type='pkl')
if uploaded_file is not None:
    df = pd.read_pickle(uploaded_file)
    st.write(df.head(5))
else:
    st.stop()



missed_values = df.isna().sum()
missed_values = missed_values[missed_values > 0]
st.write(missed_values)