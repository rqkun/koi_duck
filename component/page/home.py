import streamlit as st
import component.card.horizontal as horizontal
import streamlit as st
from datetime import datetime, timezone
import pytz
from PIL import Image

st.set_page_config(
    page_title="Koiduck",
    layout="centered",
    page_icon=Image.open("static/logo.png")
)

try:
    tz = st.context.timezone
    tz_obj = pytz.timezone(tz)
except Exception:
    tz_obj = pytz.timezone("UTC")

DATEIME = st.secrets["variable"]["anniversary"]

ANNIVERSARY_DATE = datetime(DATEIME[0], DATEIME[1], DATEIME[2], tzinfo=tz_obj) 

st.markdown("""
<style>
.anniversary-card {
    background: linear-gradient(135deg, #ff4e50, #f9d423);
    padding: 2rem;
    border-radius: 0.5rem;
    text-align: center;
    color: white;
    box-shadow: 0 4px 20px rgba(0,0,0,0.25);
}
.main-count {
    font-size: 4em;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

def navto(page):
    st.switch_page(f"component/page/{page}.py")

def add_months(date, months, tz_obj):
    month = date.month - 1 + months
    year = date.year + month // 12
    month = month % 12 + 1
    day = min(date.day, [31,
        29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
        31,30,31,30,31,31,30,31,30,31][month-1])
    return datetime(year, month, day, tzinfo=tz_obj)

def calc_years_months(start, end):
    years = end.year - start.year
    months = end.month - start.month
    if end.day < start.day:
        months -= 1
    if months < 0:
        years -= 1
        months += 12
    return years, months

def format_duration(years, months):
    parts = []
    if years > 0:
        parts.append(f"{years} year{'s' if years > 1 else ''}")
    if months > 0:
        parts.append(f"{months} month{'s' if months > 1 else ''}")
    return " ".join(parts) if parts else "—"

now = datetime.now(timezone.utc).astimezone(tz_obj)

years_since, months_since = calc_years_months(ANNIVERSARY_DATE, now)
months_since_total = years_since * 12 + months_since
days_since = (now - ANNIVERSARY_DATE).days

subcount_text = format_duration(years_since, months_since)

next_month_total = months_since_total + 1
next_milestone_date = add_months(ANNIVERSARY_DATE, next_month_total, tz_obj)
if next_milestone_date < now:
    next_month_total += 1
    next_milestone_date = add_months(ANNIVERSARY_DATE, next_month_total, tz_obj)

days_until_next_milestone = (next_milestone_date - now).days
next_years, next_months = divmod(next_month_total, 12)
next_milestone_label = format_duration(next_years, next_months)

this_year_anniv = ANNIVERSARY_DATE.replace(year=now.year)
if this_year_anniv < now:
    next_year_anniv = this_year_anniv.replace(year=now.year + 1)
else:
    next_year_anniv = this_year_anniv
days_until_next_year = (next_year_anniv - now).days


home_l, home_r = st.columns([1,1], width="stretch")

with home_l:

    st.markdown(f"""
    <div class='anniversary-card'>
        <div class='main-count'>{days_since:,} 💖</div>
    </div><br>""", unsafe_allow_html=True)
    
    
    st.info(f"{subcount_text}", icon= ":material/calendar_month:")
    
    st.caption("Days until next anniversary:")
    with st.container(horizontal=True, gap=None):
    
        st.badge(f"⏳Month: {days_until_next_milestone} days")
        st.badge(f"📅Year: {days_until_next_year} days")

with home_r.container(border=False,
                    width="stretch",
                    horizontal_alignment="center",
                    vertical_alignment="top"):
    with st.container(border=True):
        horizontal.show("static/1/0.png",None,"The page for rewatching the confession")
        if st.button("Confession", key="nav_to_confession", use_container_width=True, type="primary", icon=":material/heart_plus:"):
            navto("confession")

    with st.container(border=True):
        horizontal.show("static/cook.png",None,"The page for lunch ingredient picking")
        if st.button("Cooking", key="nav_to_cook", use_container_width=True, type="primary", icon=":material/fork_spoon:"):
            navto("cooking")