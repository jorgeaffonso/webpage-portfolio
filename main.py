import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\B&W.jpg", width=440)

with col2:
    st.title("Jorge Luis Affonso")
    content = """ Hi, i am Jorge, ..."""
    st.info(content)

content2 = """ Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)
