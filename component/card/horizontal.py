import streamlit as st

def show(image_path=None, title=None, description=None, border=False):
    with st.container(border=border,
                  width="stretch",
                  height="stretch",
                  horizontal_alignment="center",
                  vertical_alignment="center"):
        
        noti_l, noti_r = st.columns([1,2], gap="medium", vertical_alignment="center")
        
        if image_path != None:
            noti_l.image(image_path)
        
        if title != None:
            noti_r.markdown(f"### {title}")
        
        if description != None:
            noti_r.markdown(f"*{description}*", unsafe_allow_html=True)