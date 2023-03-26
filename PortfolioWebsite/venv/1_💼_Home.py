import streamlit as st
import pandas

st.set_page_config(layout="wide", page_title="My Portfolio", page_icon="💼")

col1, col2 = st.columns(2)

with col1:
    st.image('Scripts\g702ww6o.png')

with col2:
    st.title("Harshpreet Kaur")
    content = "Ever since I was introduced to programming, I've been fascinated by its ability to solve complex problems and make our lives easier. I'm excited to showcase my work and skills on this portfolio website and hope to connect with fellow programmers and enthusiasts."
    st.info(content)

content1 = "Below are the lists of projects I have worked on."
st.write(content1)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("details.csv", sep=";")

with col3:
    for index, row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("imagesonly/" + row['image'])
        st.write("[Source Code](" + row['url'] + ")")


with col4:
    for index, row in df[3:6].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("imagesonly/" + row['image'])
        st.write(f"[Source Code]({row['url']})")
