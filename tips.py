import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

# Название 
# Описание 
st.header('_Исследование по чаевым_', divider=True)
st.write("""
    #### 1. Загрузи свой датафрейм
         """)

## Шаг 1. Загрузка CSV файла


uploaded_file = st.sidebar.file_uploader('Загрузи CSV файл', type='csv')

df = pd.read_csv(uploaded_file)
st.write(df.head(5))

## Шаг 2. Графики
st.write('#### 2. Гистограмма total_bill')
g = sns.displot(data = df, x = "total_bill")
st.pyplot(g)

if st.sidebar.button('Скачать гистограмму'):
    g.savefig('hist.png')

st.write('#### 3. Диаграмма рассеивания, связывающий total_bill, tip, и size')
fig, ax = plt.subplots(figsize = (10, 6))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="size", size="size")
st.pyplot(fig)

if st.sidebar.button('Скачать диаграмму рассеивания'):
    plt.savefig('scatterplot.png')

st.write('#### 4. Диаграмма распределения всех счетов за каждый день, разбитый по time (Dinner/Lunch)')
fig, ax = plt.subplots(figsize = (10, 6))
sns.stripplot(
    data=df, x="total_bill", y="day", hue="time",
    jitter=False, s=20, marker="D", linewidth=1, alpha=.1,)
st.pyplot(fig)

if st.sidebar.button('Скачать диаграмму распределения'):
    plt.savefig('stripplot.png')

st.write('#### 5. Тепловая карта зависимостей численных переменных')
fig, ax = plt.subplots(figsize = (10, 6))
tips_corr = df.corr(method = 'pearson', numeric_only = True)
sns.heatmap(tips_corr, annot = True, cmap = 'flare')
st.pyplot(fig)

if st.sidebar.button('Скачать тепловую карту'):
    plt.savefig('heatmap.png')

st.write('#### 6. Визуальная разница между обедами и ужинами')
fig, ax = plt.subplots(figsize = (10, 6))
sns.set_style("whitegrid")
v = df['time'].value_counts().to_list()
plt.pie(v, labels = ['Dinner', 'Lunch'])
st.pyplot(fig)

if st.sidebar.button('Скачать пиццу'):
    plt.savefig('pie.png')

#Пример графика без использования pyplot
st.write('#### 7. Количество чаевых, которые оставили курящие/некурящие с разбиванием по полу')
fig, ax = plt.subplots(figsize = (10, 6))
fig = st.bar_chart(df, x = 'smoker', y = 'tip', color = 'sex')


