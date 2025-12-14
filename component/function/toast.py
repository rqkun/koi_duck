import streamlit as st

def run():
    if st.session_state.get("cooking_sent", False):
        st.toast("✅ Ingredients sent successfully!", duration=3)
        st.session_state.cooking_sent = False