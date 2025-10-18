from email.mime.multipart import MIMEMultipart
import streamlit as st
import smtplib
from email.mime.text import MIMEText


def create_email_html(ingredients: dict, dishes):
    # Inline CSS for email compatibility
    
    ingre_list = list(set(x for v in ingredients.values() for x in v))
    
    html = f"""
    <html>
    <head>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background-color: #f7f9fc;
          color: #333;
          margin: 0;
          padding: 20px;
        }}
        .container {{
          background: #ffffff;
          border-radius: 10px;
          padding: 25px;
          box-shadow: 0 2px 8px rgba(0,0,0,0.05);
          max-width: 600px;
          margin: auto;
        }}
        h2 {{
          color: #2c3e50;
          text-align: center;
        }}
        ul {{
          list-style-type: none;
          padding: 0;
        }}
        li {{
          background: #ecf0f1;
          margin: 8px 0;
          padding: 10px 15px;
          border-radius: 6px;
        }}
        .section-title {{
          color: #27ae60;
          border-bottom: 2px solid #27ae60;
          padding-bottom: 5px;
          margin-bottom: 10px;
          font-size: 18px;
        }}
        .footer {{
          text-align: center;
          font-size: 12px;
          color: #888;
          margin-top: 20px;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h2>🍳 Koiduck - Lunch Idea</h2>

        <div>
          <h3 class="section-title">🧂 Ingredients</h3>
          <ul>
            {''.join(f'<li>{ingredient}</li>' for ingredient in ingre_list)}
          </ul>
        </div>

        <div>
          <h3 class="section-title">🍽️ Suggested Dishes</h3>
          <ul>
            {''.join(f'<li>{dish["name"]}</li>' for dish in dishes)}
          </ul>
        </div>

        <div class="footer">
          <p>Bon Appétit!<br>Sent by RAQKOI.</p>
        </div>
      </div>
    </body>
    </html>
    """
    
    plain = f"""🧂 Ingredients: \n{''.join(f'- {ingredient}\n' for ingredient in ingredients)} \n🍽️ Suggested Dishes: \n{''.join(f'- {dish["name"]}\n' for dish in dishes)}"""
    
    return html, plain

def send(ingredients, recipes):
    
    EMAIL_SENDER = st.secrets['email_auth']["gmail"]
    EMAIL_RECEIVER = st.user['email']

    html, text = create_email_html(ingredients, recipes)

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg = MIMEMultipart('alternative')
    msg.attach(part1)
    msg.attach(part2)
    
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = "Koiduck - Lunch Idea"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_SENDER, st.secrets["email_auth"]["password"])
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    server.sendmail(EMAIL_SENDER, st.secrets["email_auth"]["chef"], msg.as_string())
    server.quit()
