import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title(':blue[Чаевые в ресторане] :cake:')
st.subheader('_Анализ чаевых вашего заведения_')
uploaded_file = st.sidebar.file_uploader(':blue[Загрузите CSV-файл]', type='csv')


if st.sidebar.button('Помощь', 
                  key=None,
                  help='Помощь в загрузке файла',
                  on_click=None,
                  args=None, 
                  kwargs=None,
                  type="secondary",
                  disabled=False, 
                  use_container_width=False):
    st.sidebar.write("Это программа принимает для обработки только файлы формата CSV с заданными параметрами столбцов. В ином случае просьба использовать программу FCD.Q1")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except:
        st.stop()
else:
    st.stop()

st.title('Объём чаевых по дням недели')
st.bar_chart(data=df,
             x='day',
             y='tip',
             x_label='День недели',
             y_label='Сумма полученных чаевых',
             color=(173, 216, 290),
             horizontal=False,
             width=None,
             height=None,
             use_container_width=True)
st.title('Соотношение чаевых и стоимости заказов')
df['index_list']=list(range(len(df.index)))
st.bar_chart(data=df,
             x='index_list',
             y=['tip','total_bill'],
             x_label='Заказы',
             y_label='Стоимость заказа и чаевые',
             color=[(180, 232, 143),(3, 25, 100)],
             horizontal=False,
             width=550,
             height=600,
             use_container_width=True)

st.sidebar.download_button('Скачать график *Объём чаевых по дням недели*','tips_by_week_day')
st.sidebar.download_button('Скачать график *Соотношение чаевых и стоимости заказов*','332')