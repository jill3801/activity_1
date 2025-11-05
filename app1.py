import streamlit as st

st.title("🌟 My First Streamlit App")

name = st.text_input("Enter your name:")

if st.button("Say Hello"):
    st.write(f"Hello, {name or 'there'}! 👋")
