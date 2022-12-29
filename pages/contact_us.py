import streamlit as st

st.title("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email:")
    user_message = st.text_area("Your message:")
    button = st.form_submit_button("Submit")
    if button:
        print("Button was pressed")

