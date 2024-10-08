import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

page = st.sidebar.selectbox(":blue[Выберите страницу]", ['Чаевые в ресторане', 'Котировки компании Apple'])

if page == 'Чаевые в ресторане':
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
    plt.bar(df['day'],df['tip'])
    plt.savefig('image1.png')
    plt.close()


    st.title('Соотношение чаевых и стоимости заказов')
    df['index_list']=list(range(len(df.index)))
    st.bar_chart(data=df,
                x='index_list',
                y=['tip','total_bill'],
                x_label='Заказы',
                y_label='Стоимость заказа и чаевые',
                color=[(180, 232, 143),(3, 25, 100)],
                horizontal=False,
                width=500,
                height=600,
                use_container_width=True)
    plt.bar(df['index_list'], df['total_bill'], color='orange')
    plt.bar(df['index_list'], df['tip'], width=1, color='blue')
    plt.savefig('image2.png')
    plt.close()
    with open('image1.png', 'rb') as file1:
        st.sidebar.download_button('Скачать график *Объём чаевых по дням недели*',
                                    data=file1,
                                    file_name='image1.png',
                                    key='download_btn_1')
    with open('image2.png', 'rb') as file2:
        st.sidebar.download_button('Скачать график *Соотношение чаевых и стоимости заказов*',
                                    data=file2,
                                    file_name='image2.png',
                                    key='download_btn_2')
elif page == 'Котировки компании Apple':
    st.title('Котировки компании Apple')
    st.write('Данные за последние 10 лет')

    st.title('Динамика акций на торгах')
    apple = yf.Ticker("AAPL")
    apple_historical_data = apple.history(period="10y")
    apple_historical_data.index=apple_historical_data.index.date
    st.bar_chart(data=apple_historical_data, 
                y='Volume',
                y_label='Объём акций на торгах', 
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