from datetime import datetime, timezone
import pytz
import streamlit as st

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

def calc_days_until():
    
    try:
        tz = st.context.timezone
        tz_obj = pytz.timezone(tz)
    except Exception:
        tz_obj = pytz.timezone("UTC")
    
    DATEIME = st.secrets["variable"]["anniversary"]

    ANNIVERSARY_DATE = datetime(DATEIME[0], DATEIME[1], DATEIME[2], tzinfo=tz_obj) 
    
    now = datetime.now(timezone.utc).astimezone(tz_obj)

    years_since, months_since = calc_years_months(ANNIVERSARY_DATE, now)
    months_since_total = years_since * 12 + months_since
    

    next_month_total = months_since_total + 1
    next_milestone_date = add_months(ANNIVERSARY_DATE, next_month_total, tz_obj)
    if next_milestone_date < now:
        next_month_total += 1
        next_milestone_date = add_months(ANNIVERSARY_DATE, next_month_total, tz_obj)

    next_years, next_months = divmod(next_month_total, 12)

    this_year_anniv = ANNIVERSARY_DATE.replace(year=now.year)
    if this_year_anniv < now:
        next_year_anniv = this_year_anniv.replace(year=now.year + 1)
    else:
        next_year_anniv = this_year_anniv
        
    days_since = (now - ANNIVERSARY_DATE).days
    subcount_text = format_duration(years_since, months_since)    
    days_until_next_year = (next_year_anniv - now).days
    next_milestone_label = format_duration(next_years, next_months)
    days_until_next_milestone = (next_milestone_date - now).days
    
    return days_since, subcount_text, days_until_next_year, next_milestone_label, days_until_next_milestone
