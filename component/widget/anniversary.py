import streamlit as st

from component.function import anniversary

def show():
    days_since, subcount_text, days_until_next_year, next_milestone_label, days_until_next_milestone = anniversary.calc_days_until()

    left, right = st.columns([2,1])
    
    left.markdown(f"""
    <div class='anniversary-card'>
        <div class='main-count'>{days_since:,} 💖</div>
    </div><br>""", unsafe_allow_html=True)
    
    right.info(f"{subcount_text}", icon= ":material/calendar_month:")
    
    right.caption("Days until next anniversary:")
    with right.container(horizontal=True):
    
        st.badge(f"⏳Month: {days_until_next_milestone} days")
        st.badge(f"📅Year: {days_until_next_year} days")