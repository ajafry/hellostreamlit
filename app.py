import streamlit as st

st.set_page_config(page_title="Hello streamlit", page_icon=":ninja", layout="wide")

# ---- Header Section -----
with st.container():
    st.subheader("Hi, I am a simple app :wave:")
    st.title("Streamlit is fun")
    st.write("Streamlit enables you to create a website quickly")
    st.write("[Learn more about Streamlit >](https://streamlit.io/)")