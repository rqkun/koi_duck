import streamlit as st

def show(image_path=None, title=None, description=None, border=False):
    with st.container(border=border,
                  width="stretch",
                  height="stretch",
                  horizontal_alignment="center",
                  vertical_alignment="center"):
        
        if image_path != None:
            st.image(image_path)
        
        if title != None:
            st.markdown(f"### {title}")
        
        if description != None:
            st.markdown(f"*{description}*", unsafe_allow_html=True)