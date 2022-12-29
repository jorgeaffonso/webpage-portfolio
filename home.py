import pandas
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\B&W.jpg", width=340)

with col2:
    st.title("Jorge Luis Affonso")
    content = """ Hi, i am Jorge, ..."""
    st.info(content)

content2 = """ Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
        #st.write("[Source code](https://pythonhow.com)")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")