import streamlit as st

def register_page():
    pages = {
        "Toolbar": [
            st.Page("component/page/main.py", title="Home", icon=":material/home:"),
            st.Page("component/page/confession.py", title="Confession", icon=":material/heart_plus:"),
            st.Page("component/page/xmas.py", title="Xmas", icon=":material/featured_seasonal_and_gifts:"),
            st.Page("component/page/logout.py", title="Logout", icon=":material/logout:")
        ]
    }
    pg = st.navigation(pages, position="top")
    pg.run()

def navto(page):
    st.switch_page(f"component/page/{page}.py")