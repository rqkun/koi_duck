import streamlit as st

def logout():
    st.logout()
    st.cache_data.clear()
    st.cache_resource.clear()
    st.session_state.clear()
    st.rerun()