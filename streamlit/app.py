import streamlit as st

st.set_page_config(
    page_title="Chatacter",
    page_icon="🧑‍🎤",
    layout="wide",
)


st.title("😀 Chatacter Alpha Version")
st.write(
    "This is a simple character chatting app. Now we only support Napoleon Bonaparte"
)

if st.button("Start Chatting with Napoleon Bonaparte"):
    st.switch_page("pages/napoleon.py")
